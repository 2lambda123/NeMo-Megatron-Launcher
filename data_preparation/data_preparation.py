import sys
import os
import subprocess

import hydra
import omegaconf

from . import utils, download, extract, preprocess


def create_slurm_file(
    new_script_path,
    code_path,
    log_dir="./",
    flags="",
    hydra_args="",
    dependency=None,
    time="04:00:00",
    exclusive=True,
    requeue=True,
    file_numbers="0",
    nodes=1,
    partition="batch",
    account=None,
    mem=0,
    overcommit=False,
    job_name="",
):
    task = code_path.split("/")[-1].split(".")[0]
    with open(new_script_path, "w") as f:
        f.writelines("#!/bin/bash\n")
        f.writelines("#SBATCH --nodes=1\n")
        if dependency is not None:
            f.writelines(f"#SBATCH --dependency=aftercorr:{dependency}\n")
        f.writelines(f"#SBATCH -p {partition}\n")
        if job_name is None or job_name == "":
            job_name = "slurm_job"
        f.writelines(f"#SBATCH --job-name={job_name}\n")
        if account is not None:
            f.writelines(f"#SBATCH -A {account}\n")
        if requeue:
            f.writelines("#SBATCH --requeue\n")
        if exclusive:
            f.writelines("#SBATCH --exclusive\n")
        f.writelines(f"#SBATCH --time={time}\n")
        if mem:
            f.writelines(f"#SBATCH --mem={mem}\n")
        if overcommit:
            f.writelines(f"#SBATCH --overcommit\n")
        f.writelines(f"#SBATCH --array={file_numbers}%{nodes}\n")
        f.writelines(f"#SBATCH -o {log_dir}/log-{task}-%j_%a.out\n")
        f.writelines(f"srun {flags} python3 {code_path} {hydra_args} &\n")
        f.writelines("wait\n")


def convert_file_numbers_to_list(file_numbers_str):
    final_list = []
    split_comma = file_numbers_str.split(",")
    for elem in split_comma:
        if "-" in elem:
            split_dash = elem.split("-")
            final_list += list(range(int(split_dash[0]), int(split_dash[1]) + 1))
        else:
            final_list.append(int(elem))
    return final_list


def run_data_preparation(cfg, hydra_args="", dependency=None):
    # Read config
    bignlp_path = cfg.bignlp_path
    container = cfg.container
    container_mounts = cfg.container_mounts
    data_dir = cfg.data_dir
    base_results_dir = cfg.base_results_dir
    data_cfg = cfg.data_preparation

    # Data preparation config
    download_the_pile = data_cfg.download_the_pile
    file_numbers = data_cfg.file_numbers
    preprocess_data = data_cfg.preprocess_data
    download_vocab_url = data_cfg.download_vocab_url
    download_merges_url = data_cfg.download_merges_url
    vocab_save_dir = data_cfg.vocab_save_dir
    merges_save_dir = data_cfg.merges_save_dir
    log_dir = data_cfg.log_dir
    nodes = data_cfg.nodes
    time_limit = data_cfg.time_limit

    file_numbers_list = convert_file_numbers_to_list(str(file_numbers))

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Download vocab
    if download_vocab_url is not None:
        assert vocab_save_dir is not None, "vocab_save_dir must be a valid path."
        utils.download_single_file(
            url=download_vocab_url, save_dir=vocab_save_dir, file_name="vocab.json"
        )

    # Download merges
    if download_merges_url is not None:
        assert merges_save_dir is not None, "merges_save_dir must be a valid path."
        utils.download_single_file(
            url=download_merges_url,
            save_dir=merges_save_dir,
            file_name="merges.txt",
        )

    
    # BCM config
    if cfg.cluster_type == "bcm":
        partition = cfg.cluster.partition
        account = cfg.cluster.account
        exclusive = cfg.cluster.exclusive
        mem = cfg.cluster.mem
        overcommit = cfg.cluster.overcommit
        job_name_prefix = cfg.cluster.job_name_prefix

        # Process container-mounts.
        mounts_str = f"{bignlp_path}:{bignlp_path},{data_dir}:{data_dir},{base_results_dir}:{base_results_dir}"
        if container_mounts is not None:
            assert isinstance(container_mounts, omegaconf.listconfig.ListConfig), "container_mounts must be a list."
            for mount in container_mounts:
                if mount is not None and isinstance(mount, str):
                    mounts_str += f",{mount}:{mount}"

        flags = f"--container-image {container} --container-mounts {mounts_str}"

        assert isinstance(download_the_pile, bool), "download_the_pile must be bool."
        if download_the_pile:
            # Download The Pile dataset files
            download_script_path = os.path.join(
                bignlp_path, "data_preparation/download_script.sh"
            )
            download_code_path = os.path.join(bignlp_path, "data_preparation/download.py")
            create_slurm_file(
                new_script_path=download_script_path,
                code_path=download_code_path,
                log_dir=log_dir,
                flags=flags,
                hydra_args=hydra_args,
                dependency=dependency,
                time=time_limit,
                file_numbers=file_numbers,
                nodes=nodes,
                partition=partition,
                account=account,
                mem=mem,
                overcommit=overcommit,
                job_name=f"{job_name_prefix}download",
            )
            job_id_1 = subprocess.check_output(
                [f"sbatch --parsable {download_script_path}"], shell=True
            )
            dependency = job_id_1.decode("utf-8")
            print(f"Submitted Download script with job id: {dependency}")


            # Extract The Pile dataset files
            extract_script_path = os.path.join(
                bignlp_path, "data_preparation/extract_script.sh"
            )
            extract_code_path = os.path.join(bignlp_path, "data_preparation/extract.py")
            create_slurm_file(
                new_script_path=extract_script_path,
                code_path=extract_code_path,
                log_dir=log_dir,
                flags=flags,
                hydra_args=hydra_args,
                dependency=dependency,
                time=time_limit,
                file_numbers=file_numbers,
                nodes=nodes,
                partition=partition,
                account=account,
                mem=mem,
                overcommit=overcommit,
                job_name=f"{job_name_prefix}extract",
            )
            job_id_2 = subprocess.check_output(
                [f"sbatch --parsable {extract_script_path}"], shell=True
            )
            dependency = job_id_2.decode("utf-8")
            print(f"Submitted Extract script with job id: {dependency}")


        assert isinstance(preprocess_data, bool), "preprocess_data must be bool."
        if preprocess_data:
            # Preprocess the dataset
            preprocess_script_path = os.path.join(
                bignlp_path, "data_preparation/preprocess_script.sh"
            )
            preprocess_code_path = os.path.join(
                bignlp_path, "data_preparation/preprocess.py"
            )
            create_slurm_file(
                new_script_path=preprocess_script_path,
                code_path=preprocess_code_path,
                log_dir=log_dir,
                flags=flags,
                hydra_args=hydra_args,
                dependency=dependency,
                time=time_limit,
                file_numbers=file_numbers,
                nodes=nodes,
                partition=partition,
                account=account,
                mem=mem,
                overcommit=overcommit,
                job_name=f"{job_name_prefix}preprocess",
            )
            job_id_3 = subprocess.check_output(
                [f"sbatch --parsable {preprocess_script_path}"], shell=True
            )
            dependency = job_id_3.decode("utf-8")
            print(f"Submitted Preprocessing script with job id: {dependency}")

        return dependency

    if cfg.cluster_type == "bcp":
        assert isinstance(download_the_pile, bool), "download_the_pile must be bool."
        if download_the_pile:
            download.download_bcp(cfg, file_numbers_list)
            extract.extract_bcp(cfg, file_numbers_list)

        assert isinstance(preprocess_data, bool), "preprocess_data must be bool."
        if preprocess_data:
            preprocess.preprocess_bcp(cfg, file_numbers_list)

        return None
