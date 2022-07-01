from omegaconf import OmegaConf


class TestClusterConfig:
    def test_cluster_bcm_config(self):
        conf = OmegaConf.load("conf/cluster/bcm.yaml")
        s = """
        cluster:
          type: pyxis
          account: null
          partition: null
          srun_args: ["--mpi", "pmix"]
          support_gpus_allocation: True
        env:
          job_name_prefix: "bignlp_hp_tool:"
          training_container_image: nvcr.io/ea-bignlp/ea-participants-kt/bignlp-training:22.06.rc2-py3
          inference_container_image: nvcr.io/ea-bignlp/bignlp-inference:22.05-py3
        
        exclusive: True
        gpus_per_task: null
        gpus_per_node: 8
        mem: 0
        overcommit: False
        
        partition: ${cluster.cluster.partition}
        account: ${cluster.cluster.account}
        job_name_prefix: ${cluster.env.job_name_prefix}
        """
        expected = OmegaConf.create(s)
        assert (
            expected == conf
        ), f"conf/cluster/bcm.yaml must be set to {expected} but it currently is {conf}."
