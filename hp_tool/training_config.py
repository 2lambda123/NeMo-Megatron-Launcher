import os
import yaml
import subprocess

import omegaconf
from omegaconf import OmegaConf

from hp_tool import utils, train


def search_training_config(base_cfg, model_size, model_name, cfg):
    # Generate candidate configs.
    base_dir, results_cfgs = generate_grid_search_configs(base_cfg, model_size, model_name, cfg)
    # Launch candidate configs.
    job_ids = launch_grid_search_configs(base_dir, results_cfgs, cfg)
    #job_ids = None
    # Measure and compare throughputs for each config.
    launch_throughput_measure(job_ids, model_size, cfg)


def generate_grid_search_configs(base_cfg, model_size_in_b, model_name, cfg):
    num_layers = base_cfg["model"]["num_layers"]
    results_cfgs = [[] for _ in range(num_layers + 1)]

    tp_list, pp_list, mbs_list = _calculate_tp_pp_mbs_grid(
        model_size_in_b=model_size_in_b, num_layers=num_layers
    )

    base_dir = f"{cfg.search_config.train_settings.logs}/candidate_configs"
    os.makedirs(base_dir, exist_ok=True)

    max_minutes = cfg.search_config.train_settings.max_minutes_per_run

    valid_pp_list = []
    for tp in tp_list:
        for pp in pp_list:
            if model_name == "gpt3":
                act_ckpt_layers = [x for x in range(num_layers // pp + 1)]
            elif model_name == "t5":
                # TODO: @yuya to check.
                # 2 * num_layers is needed because of encoder/decoder architecture.
                act_ckpt_layers = [x for x in range(2 * num_layers // pp + 1)]
            else:
                raise NotImplementedError("Model name not implemented.")

            for act in act_ckpt_layers:
                for mbs in mbs_list:
                    num_gpus = base_cfg["trainer"]["num_nodes"] * base_cfg["trainer"]["devices"]
                    gbs = base_cfg["model"]["global_batch_size"]
                    att_heads = base_cfg["model"]["num_attention_heads"]
                    num_layers = base_cfg["model"]["num_layers"]
                    mod_gbs = gbs % (mbs * num_gpus / (tp * pp))
                    mod_att_heads = att_heads % tp
                    mod_layers = num_layers % pp
                    if mod_gbs == 0 and mod_att_heads == 0 and mod_layers == 0:
                        valid_pp_list.append(pp)

    # Generate grid search configs.
    for tp in tp_list:
        for pp in pp_list:
            if model_name == "gpt3":
                act_ckpt_layers = [x for x in range(num_layers // pp + 1)]
            elif model_name == "t5":
                act_ckpt_layers = [x for x in range(2 * num_layers // pp + 1)]
            else:
                raise NotImplementedError("Model name not implemented.")

            for act in act_ckpt_layers:
                for mbs in mbs_list:
                    new_cfg = utils.modify_cfg(
                        base_cfg, act, tp, pp, mbs, max_minutes, max(valid_pp_list)
                    )
                    if new_cfg:  # Save candidate cfg.
                        file_name = (
                            f"{model_name}_{model_size_in_b}b_tp_{tp}_pp_{pp}_mbs_{mbs}_act_ckpt_{act}.yaml"
                        )
                        results_cfgs[act].append(file_name)
                        with open(f"{base_dir}/{file_name}", "w") as f:
                            yaml.dump(new_cfg, f)
    print("\nAll candidate configurations created correctly.\n")
    return base_dir, results_cfgs


def _calculate_tp_pp_mbs_grid(model_size_in_b, num_layers, model_name="gpt3"):
    # TODO: @mausin add support for T5, ask @yuya for guidance.
    valid_pp = [
        x for x in range(1, num_layers + 1) if num_layers % x == 0
    ]  # Only divisors of num_layers are possible.
    if model_name == "gpt3":
        tp = [1, 2, 4, 8]
        pp = [1]
        mbs = [1, 2, 4, 8]
        if model_size_in_b <= 1.0:
            tp = [1, 2]
        elif 1.0 < model_size_in_b <= 4.0:
            tp = [1, 2, 4]
        elif 4.0 < model_size_in_b <= 8.0:
            tp = [2, 4, 8]
        elif 8.0 < model_size_in_b <= 13.0:
            tp = [4, 8]
        elif 13.0 < model_size_in_b <= 23.0:
            tp = [8]
            pp = [x for x in valid_pp if x < 6]
        elif 23.0 < model_size_in_b <= 45.0:
            tp = [8]
            pp = [x for x in valid_pp if 1 < x < 7]
        elif 45.0 < model_size_in_b <= 95:
            tp = [8]
            pp = [x for x in valid_pp if 3 < x < 11]
            mbs = [1, 2, 4]
        elif 95.0 < model_size_in_b <= 130.0:
            tp = [8]
            pp = [x for x in valid_pp if 5 < x < 21]
            mbs = [1, 2, 4]
        elif 130.0 < model_size_in_b <= 195.0:
            tp = [8]
            pp = [x for x in valid_pp if 7 < x < 29]
            mbs = [1, 2]
        elif 195.0 < model_size_in_b <= 395.0:
            tp = [8]
            pp = [x for x in valid_pp if 15 < x < 65]
            mbs = [1, 2]
        elif 395.0 < model_size_in_b <= 790.0:
            tp = [8]
            pp = [x for x in valid_pp if 23 < x < 71]
            mbs = [1, 2]
        elif 790.0 < model_size_in_b <= 1100.0:
            tp = [8]
            pp = [x for x in valid_pp if 29 < x < 131]
            mbs = [1, 2]
    elif model_name == "t5":
        # TODO: @yuya to check.
        tp = [1, 2, 4, 8]
        pp = [1]
        mbs = [1, 2, 4, 8]
        if model_size_in_b <= 1.0:
            tp = [1]
        elif 1.0 < model_size_in_b <= 2.0:
            tp = [1, 2]
        elif 4.0 < model_size_in_b <= 8.0:
            tp = [2, 4, 8]
        elif 8.0 < model_size_in_b <= 11.5:
            tp = [4, 8]
    else:
        raise NotImplementedError("Model name not implemented.")
    return tp, pp, mbs


def launch_grid_search_configs(base_dir, results_cfgs, cfg):
    """Launches training jobs for the grid search in parallel. The limit of how many 
    jobs to launch is specified by limit_search_runs.

    Arguments:
        base_dir: str, location where the configs are stored.
        results_cfgs: list, list of config names.
        cfg: OmegaConf, the general config object.
    Output:
        job_ids: list, list of job ids for all the training jobs.
    """
    limit = cfg.search_config.train_settings.limit_search_runs
    job_ids = []
    for cfg_list in results_cfgs:
        for config in cfg_list:
            conf = OmegaConf.load(f"{base_dir}/{config}")
            new_cfg = create_bignlp_config(cfg)
            # Add the training config (conf) to the new_cfg.training, which is the bignlp-scripts format.
            new_cfg.training = conf
            # Add cluster config to new_cfg.
            new_cfg.cluster = cfg.cluster
            job_id = train.run_training(new_cfg, cfg.bignlp_hp_tool_path)
            if job_id is not None:
                job_ids.append(job_id[:-1])
            if len(job_ids) == limit:
                return job_ids
    return job_ids


def create_bignlp_config(cfg):
    """Creates a basic config for bignlp-scripts to train the model correctly.

    Arguments:
        cfg: OmegaConf, base configuration object.
    Output:
        new_cfg: OmegaConf, new config object ready for bignlp-scripts.
    """
    results_dir = os.path.join(cfg.search_config.train_settings.logs, "training_logs")
    training_container = cfg.training_container
    data_dir = cfg.data_dir
    model_size = cfg.search_config.train_settings.model_size_in_b

    s = f"""
    training: null
    cluster: null

    run_data_preparation: False
    run_training: True
    run_conversion: False
    run_finetuning: False
    run_evaluation: False

    cluster_type: bcm
    training_config: gpt3/5b
    bignlp_path: /opt/bignlp/bignlp-scripts
    data_dir: {data_dir}
    base_results_dir: {results_dir}
    container_mounts:
      - {results_dir}:/opt/bignlp/bignlp-scripts/results
    container: {training_container}
    """
    new_cfg = OmegaConf.create(s)
    return new_cfg


def launch_throughput_measure(dependency_list, model_size, cfg):
    """Launch job that measures the throughput of each run in the grid search. This 
    job will get scheduled with dependencies on all the job ids in dependency_list, 
    so it will only start running once all the jobs are finished.

    Arguments:
        dependency_list: list, list of all the job_ids this job will depend on.
        model_size_in_b: float, model size in billions of parameters.
        cfg: OmegaCOnf, general config object.
    Output:
        dependency: str, job_id of the current job.
    """
    # Read config
    bignlp_hp_tool_path = cfg.get("bignlp_hp_tool_path")
    container_mounts = cfg.get("container_mounts")
    container = cfg.get("training_container")
    hp_cfg = cfg.get("search_config")

    # CLUSTER parameters
    cluster_cfg = cfg.get("cluster")
    partition = cluster_cfg.get("partition")
    account = cluster_cfg.get("account")
    time_limit = "30:00"
    nodes = 1
    exclusive = cluster_cfg.get("exclusive")
    mem = cluster_cfg.get("mem")
    overcommit = cluster_cfg.get("overcommit")
    ntasks_per_node = 1
    gpus_per_task = None
    dependency = None
    if dependency_list is not None and len(dependency_list) > 0:
        dependency = ":".join(dependency_list)
    job_name = f"{cluster_cfg.get('job_name_prefix')}latency_measure"

    # Settings parameters
    train_settings = hp_cfg.get("train_settings")
    final_log_dir = os.path.join(train_settings.get("logs"), "final_result")
    os.makedirs(final_log_dir, exist_ok=True)

    # Process container-mounts.
    mounts_str = f"{bignlp_hp_tool_path}:{bignlp_hp_tool_path}"
    if container_mounts is not None:
        assert isinstance(
            container_mounts, omegaconf.listconfig.ListConfig
        ), "container_mounts must be a list."
        for mount in container_mounts:
            if mount is not None and isinstance(mount, str):
                mounts_str += f",{mount}:{mount}"

    flags = (
        f"--container-image {container} "
        f"--container-mounts {mounts_str} "
        f"-o {final_log_dir}/compare_throughput_{model_size}b-%j.log "
        f"-e {final_log_dir}/compare_throughput_{model_size}b-%j.error "
    )
    new_script_path = os.path.join(bignlp_hp_tool_path, "hp_tool/scripts/compare_throughput.sh")
    code_path = os.path.join(bignlp_hp_tool_path, "hp_tool/scripts/compare_throughput_results.py")
    train_cmd = f"HYDRA_FULL_ERROR=1 python3 -u {code_path} search_config.train_settings.model_size_in_b={model_size}"
    utils.create_slurm_file(
        new_script_path=new_script_path,
        train_cmd=train_cmd,
        job_name=job_name,
        flags=flags,
        dependency=dependency,
        exclusive=exclusive,
        mem=mem,
        overcommit=overcommit,
        time=time_limit,
        nodes=nodes,
        ntasks_per_node=ntasks_per_node,
        gpus_per_task=gpus_per_task,
        partition=partition,
        account=account,
    )

    job_id = subprocess.check_output([f"sbatch --parsable {new_script_path}"], shell=True)
    dependency = job_id.decode("utf-8")
    print(f"Submitted job to select optimal throughput with job id: {dependency}")
    return dependency