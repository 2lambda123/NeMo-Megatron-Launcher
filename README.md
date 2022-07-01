# BigNLP-Scripts

Scripts and code to provide end-to-end data preparation and training for
NeMo-Megatron.

The most recent version of the README can be found at [https://ngc.nvidia.com/containers/ea-bignlp:bignlp-training](https://ngc.nvidia.com/containers/ea-bignlp:bignlp-training).

## Table of contents
- [1. Model Overview](#1-model-overview)
- [2. Feature Matrix](#2-feature-matrix)
  * [2.1. GPT-3 Models](#21-gpt-3-models)
  * [2.2. T5/mT5 Models](#22-t5-mt5-models)
- [3. Setup](#3-setup)
  * [3.1. Support Matrix](#31-support-matrix)
- [4. Cloud Service Providers](#4-cloud-service-providers)
  * [4.1. Azure](#41-azure)
    + [4.1.1 Cluster Bring-Up](#411-cluster-bring-up)
    + [4.1.2 Cluster Validation](#412-cluster-validation)
      - [4.1.2.1 Validation Script Usage](#4121-validation-script-usage)
    + [4.1.3 Config Modifications](#413-config-modifications)
      - [4.1.3.1 Generate NCCL Topology](#4131-generate-nccl-topology)
      - [4.1.3.2 Environment Variables](#4132-environment-variables)
- [5. Quick Start Guide](#5-quick-start-guide)
  * [5.1. Training BigNLP Models](#51-training-bignlp-models)
    + [5.1.1. Prepare Environment](#511-prepare-environment)
      - [5.1.1.1. Slurm](#5111-slurm)
      - [5.1.1.2. Base Command Platform](#5112-base-command-platform)
      - [5.1.1.3. General Configuration](#5113-general-configuration)
    + [5.1.2. Data Preparation](#512-data-preparation)
      - [5.1.2.1. Data Preparation for GPT-3 Models](#5121-data-preparation-for-gpt-3-models)
        * [5.1.2.1.1. Slurm](#51211-slurm)
        * [5.1.2.1.2. Base Command Platform](#51212-base-command-platform)
        * [5.1.2.1.3. Common](#51213-common)
      - [5.1.2.2. Data Preparation for T5 Models](#5122-data-preparation-for-t5-models)
        * [5.1.2.2.1. Slurm](#51221-slurm)
        * [5.1.2.2.2. Base Command Platform](#51222-base-command-platform)
        * [5.1.2.2.3. Common](#51223-common)
      - [5.1.2.3. Data Preparation for mT5 Models](#5123-data-preparation-for-mt5-models)
        * [5.1.2.3.1. Slurm](#51231-slurm)
        * [5.1.2.3.2. Base Command Platform](#51232-base-command-platform)
        * [5.1.2.3.3. Common](#51233-common)
  * [5.2. Training with Predefined Configurations](#52-training-with-predefined-configurations)
    + [5.2.1. Predefined Configurations of GPT-3 Models](#521-predefined-configurations-of-gpt-3-models)
    + [5.2.2. Predefined Configurations of T5 Models](#522-predefined-configurations-of-t5-models)
    + [5.2.3. Predefined Configurations of mT5 Models](#523-predefined-configurations-of-mt5-models)
    + [5.2.4. Training Logs with TensorBoard and Weights & Biases](#524-training-logs-with-tensorboard-and-weights---biases)
  * [5.3. Using the HP Tool to Find the Optimal Configuration](#53-using-the-hp-tool-to-find-the-optimal-configuration)
    + [5.3.1. HP Tool Capabilities](#531-hp-tool-capabilities)
      - [5.3.1.1. Model Size Recommendation](#5311-model-size-recommendation)
      - [5.3.1.2. Base Config Generation](#5312-base-config-generation)
      - [5.3.1.3. Training HP Search](#5313-training-hp-search)
      - [5.3.1.4. Inference HP Search](#5314-inference-hp-search)
    + [5.3.2. Usage](#532-usage)
      - [5.3.2.1. General Configuration](#5321-general-configuration)
      - [5.3.2.2. Running Predefined Configs](#5322-running-predefined-configs)
        * [5.3.2.2.1. Model Config](#53221-model-config)
        * [5.3.2.2.2. Base Config Generation](#53222-base-config-generation)
        * [5.3.2.2.3. Training HP Search](#53223-training-hp-search)
        * [5.3.2.2.4. Inference HP Search](#53224-inference-hp-search)
      - [5.3.2.3. Running Custom Model Size Configs](#5323-running-custom-model-size-configs)
      - [5.3.2.4. Interpreting the Results](#5324-interpreting-the-results)
      - [5.3.2.5. Logging Runs with Weights and Biases](#5325-logging-runs-with-weights-and-biases)
  * [5.4. Training with Custom Configurations](#54-training-with-custom-configurations)
    + [5.4.1 Example: Changing Embedding Type for T5 models](#541-example-changing-embedding-type-for-t5-models)
  * [5.5. Bring Your Own Dataset](#55-bring-your-own-dataset)
      - [5.5.1. Slurm](#551-slurm)
      - [5.5.2. Base Command Platform](#552-base-command-platform)
      - [5.5.3. Common](#553-common)
  * [5.6. Model Training](#56-model-training)
    + [5.6.1. GPT-3 Training](#561-gpt-3-training)
      - [5.6.1.1. Slurm](#5611-slurm)
      - [5.6.1.2. Base Command Platform](#5612-base-command-platform)
    + [5.6.2. T5 Training](#562-t5-training)
      - [5.6.2.1. Slurm](#5621-slurm)
      - [5.6.2.2. Base Command Platform](#5622-base-command-platform)
    + [5.6.3. mT5 Training](#563-mt5-training)
      - [5.6.3.1. Slurm](#5631-slurm)
      - [5.6.3.2. Base Command Platform](#5632-base-command-platform)
  * [5.7. Resuming Training with Different Number of Nodes](#57-resuming-training-with-different-number-of-nodes)
  * [5.8. Checkpoint Conversion](#58-checkpoint-conversion)
    + [5.8.1. GPT-3 Conversion](#581-gpt-3-conversion)
      - [5.8.1.1. Common](#5811-common)
      - [5.8.1.2. Slurm](#5812-slurm)
      - [5.8.1.3. Base Command Platform](#5813-base-command-platform)
    + [5.8.2. T5 Conversion](#582-t5-conversion)
      - [5.8.2.1. Common](#5821-common)
      - [5.8.2.2. Slurm](#5822-slurm)
      - [5.8.2.3. Base Command Platform](#5823-base-command-platform)
    + [5.8.3. mT5 Conversion](#583-mt5-conversion)
      - [5.8.3.1. Common](#5831-common)
      - [5.8.3.2. Slurm](#5832-slurm)
      - [5.8.3.3. Base Command Platform](#5833-base-command-platform)
  * [5.9. Model Finetuning](#59-model-finetuning)
    + [5.9.1. T5 Finetuning](#591-t5-finetuning)
      - [5.9.1.1. Common](#5911-common)
      - [5.9.1.2. Slurm](#5912-slurm)
      - [5.9.1.3. Base Command Platform](#5913-base-command-platform)
    + [5.9.2. mT5 Finetuning](#592-mt5-finetuning)
      - [5.9.2.1. Common](#5921-common)
      - [5.9.2.2. Slurm](#5922-slurm)
      - [5.9.2.3. Base Command Platform](#5923-base-command-platform)
    + [5.9.3. Finetuning on Custom Tasks](#593-finetuning-on-custom-tasks)
  * [5.10. Model Prompt Learning](#510-model-prompt-learning)
    + [5.10.1. GPT-3 Prompt Learning](#5101-gpt-3-prompt-learning)
      - [5.10.1.1. Common](#51011-common)
      - [5.10.1.2. Slurm](#51012-slurm)
      - [5.10.1.3. Base Command Platform](#51013-base-command-platform)
  * [5.11. Model Evaluation](#511-model-evaluation)
    + [5.11.1. GPT-3 Evaluation](#5111-gpt-3-evaluation)
      - [5.11.1.1. Common](#51111-common)
      - [5.11.1.2. Slurm](#51112-slurm)
      - [5.11.1.3. Base Command Platform](#51113-base-command-platform)
    + [5.11.2. T5 Evaluation](#5112-t5-evaluation)
      - [5.11.2.1. Common](#51121-common)
      - [5.11.2.2. Slurm](#51122-slurm)
      - [5.11.2.3. Base Command Platform](#51123-base-command-platform)
    + [5.11.3. mT5 Evaluation](#5113-mt5-evaluation)
      - [5.11.3.1. Common](#51131-common)
      - [5.11.3.2. Slurm](#51132-slurm)
      - [5.11.3.3. Base Command Platform](#51133-base-command-platform)
    + [5.11.4. Prompt Learnt GPT-3 Evaluation](#5114-prompt-learnt-gpt-3-evaluation)
      - [5.11.4.1. Common](#51141-common)
      - [5.11.4.2. Slurm](#51142-slurm)
      - [5.11.4.3. Base Command Platform](#51143-base-command-platform)
- [6. Deploying the BigNLP Model](#6-deploying-the-bignlp-model)
  * [6.1. Model Inference Deployment Process](#61-model-inference-deployment-process)
  * [6.2. Prepare Environment](#62-prepare-environment)
    + [6.2.1. Slurm](#621-slurm)
    + [6.2.2. Base Command Platform](#622-base-command-platform)
  * [6.3. Provide Model and Inference Configuration](#63-provide-model-and-inference-configuration)
    + [6.3.1. Predefined Configuration for Selected Models](#631-predefined-configuration-for-selected-models)
    + [6.3.2. Optimal Configuration Search](#632-optimal-configuration-search)
      - [6.3.2.1. Random Weights Checkpoint Benchmark](#6321-random-weights-checkpoint-benchmark)
      - [6.3.2.2. Trained Checkpoint Benchmark](#6322-trained-checkpoint-benchmark)
  * [6.4. Review Deployment Search Results](#64-review-deployment-search-results)
  * [6.5. Prepare NVIDIA Triton Model Repository and Run Accuracy/Performance Tests](#65-prepare-nvidia-triton-model-repository-and-run-accuracy-performance-tests)
  * [6.6. Run NVIDIA Triton Server with Selected Model Repository](#66-run-nvidia-triton-server-with-selected-model-repository)
  * [6.7. Text generation](#67-text-generation)
    + [6.7.1. Setup](#671-setup)
    + [6.7.2. Basic Text Generation](#672-basic-text-generation)
    + [6.7.3. Longer Text Generation](#673-longer-text-generation)
    + [6.7.4. Dialogue Text Generation](#674-dialogue-text-generation)
    + [6.7.5. Inference Parameters](#675-inference-parameters)
- [7. Performance](#7-performance)
  * [7.1. GPT-3 Results](#71-gpt-3-results)
    + [7.1.1. Training Accuracy Results](#711-training-accuracy-results)
    + [7.1.2. Training Performance Results](#712-training-performance-results)
    + [7.1.3. Inference Performance](#713-inference-performance)
      - [7.1.3.1. 5B Model](#7131-5b-model)
      - [7.1.3.2. 5B Chatbot for Question Answering](#7132-5b-chatbot-for-question-answering)
      - [7.1.3.3. 5B: Translation and Style Transfer](#7133-5b--translation-and-style-transfer)
      - [7.1.3.4. Summary for 5B Results](#7134-summary-for-5b-results)
      - [7.1.3.5. 20B Model](#7135-20b-model)
      - [7.1.3.6. 20B: Chatbot for Question Answering](#7136-20b--chatbot-for-question-answering)
      - [7.1.3.7. 20B: Translation and Style Transfer](#7137-20b--translation-and-style-transfer)
      - [7.1.3.8. Summary for 20B Results](#7138-summary-for-20b-results)
      - [7.1.3.9. Model Size and Performance](#7139-model-size-and-performance)
        * [7.1.3.9.1. Online Scenario](#71391-online-scenario)
        * [7.1.3.9.2. Offline Scenario](#71392-offline-scenario)
  * [7.2. T5 Results](#72-t5-results)
    + [7.2.1. Training Accuracy Results](#721-training-accuracy-results)
    + [7.2.2. Training Performance Results](#722-training-performance-results)
  * [7.3. mT5 Results](#73-mt5-results)
    + [7.3.1. Training Accuracy Results](#731-training-accuracy-results)
    + [7.3.2. Training Performance Results](#732-training-performance-results)
- [8. Changelog](#8-changelog)
- [9. Known Issues](#9-known-issues)


<!-- /TOC -->

## 1. Model Overview
<a id="markdown-model-overview" name="model-overview"></a>

NeMo Megatron is a new version in the NeMo framework that allows developers to effectively train and scale language
models to billions of parameters. With NeMo Megatron, you can train different variants of GPT-3 and T5 style models,
and scale them to multiple nodes on NVIDIA DGX SuperPOD deployments. This deep learning (DL) software stack is optimized for DGX
SuperPOD configurations using NVIDIA InfiniBand technology to provide efficient on-premises compute for training
and inferring complex workloads.

<!-- Should this line be removed/replaced -->
Early access to NeMo Megatron is limited to enterprises that want to train and deploy GPT-3 and T5 style models on
NVIDIA DGX SuperPOD to perform tasks such as answering deep domain questions, translating languages,
comprehending and summarizing complex documents. 

The model parallelism techniques of NeMo Megatron enable the efficient training of large models that do not fit in
the memory of a single GPU. In the training tasks, tensor (intra-layer) and pipeline (inter-layer) model parallelism
are adopted. Tensor model parallelism partitions individual transformer layers over multiple devices. Pipeline
model parallelism stripes layers of a model over multiple devices. For more details, refer to
[this paper](https://arxiv.org/pdf/2104.04473.pdf).

**GPT-3 architecture**

<img src="img/model_overview.png"/>

Figure 1: The GPT-3 family architecture. The 5B variant includes 24 transformer layers, a hidden size of 4096, and 32 attention heads. The sequence length is 2048, and the optimizer is Adam. This variant uses tensor parallelism of 2.

## 2. Feature Matrix
<a id="markdown-feature-matrix" name="feature-matrix"></a>

### 2.1. GPT-3 Models
<a id="markdown-gpt-3-models" name="gpt-3-models"></a>

| Feature                                                 | Training                             | Inference                                                                                                                                                                                                                                                                                                                 |
| ------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data parallelism                | Yes                    | N/A                                                                                                                                                                  |
| Tensor parallelism              | Yes                    | Yes                                                                                                                                                               |
| Pipeline parallelism            | Yes                     | Yes (Megatron-LM checkpoints)                                                                                                                          |
| Gradient checkpointing          | Yes                    | N/A                                                                                                                                                                  |
| Partial gradient checkpointing  | Yes                    | N/A                                                                                                                                                                  |
| FP32/TF32                       | Yes                    | Yes (FP16 enabled by default)                                                                                                                                     |
| AMP/FP16                        | No | Yes                                                                                                                                                               |
| BF16                            | Yes  | Yes                                                                                                                                                                |
| Multi-GPU                       | Yes                    | Yes                                                                                                                                                               |
| Multi-Node                      | Yes                    | Yes                                                                                                                                                               |
| Inference deployment            | N/A                    | [NVIDIA Triton supported](https://github.com/triton-inference-server/backend#where-can-i-find-all-the-backends-that-are-available-for-triton), Faster Transformer |
| SW stack support                | Slurm DeepOps/Base Command Manager/Base Command Platform          | Slurm DeepOps/Base Command Manager/Base Command Platform                                                                                                                                                     |
| Distributed data preprocessing | Yes (the Pile only)       | N/A                                                                                                                                                                  |
| NVfuser                         | No             | N/A                                                                                                                                                                  |
| P-Tuning and Prompt Tuning                | Yes (Tensor Parallelism only)             | N/A                                                                                                                                                                  |

### 2.2. T5/mT5 Models
<a id="markdown-t5-mt5-models" name="t5-mt5-models"></a>

| Feature                          | Training                                                 | Inference |
|----------------------------------|----------------------------------------------------------|:---------:|
| Data parallelism                 | Yes                                                      |    N/A    |
| Tensor parallelism               | Yes                                                      |    No     |
| Pipeline parallelism             | Yes                                                      |    No     |
| Gradient checkpointing           | Yes                                                      |    N/A    |
| Partial gradient checkpointing   | Yes                                                      |    N/A    |
| FP32/TF32                        | Yes                                                      |    No     |
| AMP/FP16                         | No                                                       |    No     |
| BF16                             | Yes                                                      |    No     |
| Multi-GPU                        | Yes                                                      |    No     |
| Multi-Node                       | Yes                                                      |     No    |
| Inference deployment             | N/A                                                      |    No     |
| SW stack support                 | Slurm DeepOps/Base Command Manager/Base Command Platform |    No     |
| Distributed data preprocessing   | Yes (the Pile dataset for T5, mC4 dataset for mT5)       |    N/A    |
| NVfuser                          | No                                                       |    N/A    |
| Hyperparameter tool                         | Yes                                                       |    N/A    |


## 3. Setup
<a id="markdown-setup" name="setup"></a>

### 3.1. Support Matrix
<a id="markdown-support-matrix" name="support-matrix"></a>

| Software                | EA               |
|-------------------------|------------------|
| NVIDIA Triton           | 2.21.0           |
| FasterTransformer       | V5               |
| PyTorch                 | 1.12.0a0+8a1a93a |
| NeMo                    | 1.10.0           |
| PyTorch Lightning       | 1.6.4            |
| Hydra                   | 1.1.1            |
| CUDA                    | NVIDIA CUDA 11.7 |
| cuBLAS                  | 11.10.1.25       |
| cuDNN                   | 8.4.0.27         |
| NCCL                    | 2.12.10          |
| Container OS            | Ubuntu 20.04     |
| rdma-core               | 36.0             |
| GDRcopy                 | 2.3              |
| HPC-X                   | 2.10.0           |
| Base Command Manager    | 1.0.0            |
| DeepOps                 | 21.06            |

## 4. Cloud Service Providers
<a id="markdown-cloud-service-providers" name="cloud-service-providers"></a>

### 4.1 Azure
<a id="markdown-azure" name="azure"></a>

#### 4.1.1 Cluster Bring-Up
<a id="markdown-cluster-bring-up" name="cluster-bring-up"></a>
To set up a Slurm cluster for bignlp, we recommend using Azure CycleCloud with the following steps:

1. Follow the [cc-slurm-ngc](https://github.com/JonShelley/cc-slurm-ngc/blob/master/README.md) README to create the CycleCloud VM in the Azure portal. Complete all steps until "Download and setup the project", including creating a new storage account.
2. Create an Azure AD application using [this document](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal):
    1. Check both your AD and subscription [permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#permissions-required-for-registering-an-app) to ensure you can register an application and assign a role to it, or talk to your subscription administrator.
    2. Create the [app registration](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#register-an-application-with-azure-ad-and-create-a-service-principal).
    3. [Assign](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#assign-a-role-to-the-application) the contributor role to the application.
    4. Create and record an [application secret](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#option-2-create-a-new-application-secret) along with your application ID.
3. Go to \<cyclecloud vm ip\>/subscriptions. Name your subscription and enter your Tenant ID, Application ID, and Application Secret. Then choose a default location and the resource group and storage account you created in step 1 (leave the storage container field as is).
4. Continue with the [cc-slurm-ngc](https://github.com/JonShelley/cc-slurm-ngc#download-and-setup-the-project) README to add the cc-slurm-ngc cluster type and deploy your cluster.

Once your cluster is up and running, continue with the cluster validation steps.

#### 4.1.2 Cluster Validation
<a id="markdown-cluster-validation" name="cluster-validation"></a>

Before running the cluster validation script, ensure your NGC credentials have been added to `~/.config/enroot/.credentials` on all nodes.
Also make sure to download this benchmarking repo to `/shared/data`:
```
cd /shared/data
git clone https://github.com/JonShelley/azure.git
```
**NOTE:** If you choose to download this repo to another path, please change the `AZURE_NCCL_PATH` variable at the top of `cluster_validation.sh`.

The cluster validation script at `csp/azure/cluster_validation.sh` will run GPU diagnostics and test NCCL node-to-node bus bandwidth.
The logs from these tests will be stored at `results/cluster_validation`. The script will list any nodes that fail these tests.
These nodes should be replaced or restarted through the CycleCloud UI.

##### 4.1.2.1 Validation Script Usage
<a id="markdown-validation-script-usage" name="validation-script-usage"></a>

The script has 3 required parameters:
- `--nodes`: the number of nodes
- `--nodelist`: the list of node names
- `--partition`: the Slurm partition the nodes are assigned to

The values for these parameters should be in the same format that is found in `sinfo`.
With the following example:
```
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
hpc          up   infinite      8   idle hpc-pg0-[1-8]
```
To test all 8 idle nodes, the script would be run as:
```
bash cluster_validation.sh --nodes=8 --nodelist=hpc-pg0-[1-8] --partition=hpc
```

By default, the script will run both the GPU diagnostics and the NCCL test. You can choose to run only one or the other by specifying:
- `--dcgm`: run GPU diagnostics only
- `--nccl`: run NCCL test only

See `bash cluster_validation.sh -h` for more information.

#### 4.1.3 Config Modifications
<a id="markdown-config-modifications" name="config-modifications"></a>
Before launching jobs, the NCCL topology file needs to be created, and some changes to the config files must be made.

##### 4.1.3.1 Generate NCCL Topology
<a id="markdown-generate-nccl-topology" name="generate-nccl-topology"></a>

To generate the NCCL topology file, run the following (use path for wherever `JonShelley/azure` was downloaded):
```
sbatch -N 1 -o ndv4-topo.xml /shared/data/azure/benchmarking/NDv4/cc-slurm-ngc/nccl/scripts/gentopo.sh
mv ndv4-topo.xml /opt/microsoft/ndv4-topo.xml
```

In `conf/config.yaml`, mount the directory containing the topology file, and set where the topology file will be located:
```
container_mounts:
  - /opt/microsoft:/opt/microsoft

env_vars:
    NCCL_TOPO_FILE: /opt/microsoft/ndv4-topo.xml
```

##### 4.1.3.2 Environment Variables
<a id="markdown-environment-variables" name="environment-variables"></a>
Set these environment variables in `config.yaml` (in addition to `NCCL_TOPO_FILE` as defined above):
```
env_vars:
  UCX_IB_PCI_RELAXED_ORDERING: auto
  NCCL_IB_PCI_RELAXED_ORDERING: 2
  NCCL_IB_TIMEOUT: 22
  NCCL_DEBUG: INFO
```

Once all these steps have been completed, BigNLP jobs can be launched on your Azure cluster.

## 5. Quick Start Guide
<a id="markdown-quick-start-guide" name="quick-start-guide"></a>

### 5.1. Training BigNLP Models
<a id="markdown-training-bignlp-models" name="training-bignlp-models"></a>

#### 5.1.1. Prepare Environment
<a id="markdown-prepare-environment" name="prepare-environment"></a>

<!--
The whole solution uses a set of Docker containers executed at the Slurm
cluster using the pyxis plug-in Base Command Platform cluster. The training
container also includes conversion scripts and NVIDIA Triton Model Navigator.
The inference container is just the NVIDIA Triton Inference Server with the
FasterTransformer backend installed.    For Base Command Platform, the BigNLP
scripts repository (bcp branch) will be part of the container image. It is
recommended to create a bignlp_ws_scripts_<username> workspace in your ace and
copy the bignlp-scripts directory there    either from the container image or
from git clone of the above repository if you have access.    Install the BigNLP
scripts dependencies on the head node of your cluster. Base Command Platform
clusters do not have a head login node. We're currently running these scripts
on a DGX node in the Base Command Platform cluster. Once the cluster has
cpu-only nodes then we can use those. Till then we can run on DGX node or in a
local conda environment.    To be able to call the necessary scripts from the
login node on a cluster, some packages must be installed there using the
requirements.txt file:
```
cd bignlp-scripts
pip install -r requirements.txt
```
You can use virtualenv to prevent polluting your head node environment for
other Python projects. If your Slurm configuration environment lacks pip, then
you can use get_pip.py with just python3.
 -->
**NOTE:** Ensure the high-speed filesystem is mounted on the job submission
node(s) at the same path as on the compute nodes.

The whole solution uses a set of Docker containers executed on a Slurm
cluster (using the [pyxis](https://github.com/NVIDIA/pyxis) plug-in) or
a Base Command Platform cluster. The training container also includes 
conversion scripts and NVIDIA Triton Model Navigator. The inference container
comprises the NVIDIA Triton Inference Server with the FasterTransformer 
backend installed.

##### 5.1.1.1. Slurm
<a id="markdown-slurm" name="slurm"></a>

The bignlp codebase is included as part of the training container. To
copy it to a local directory in the cluster, it needs to be extracted from the
container. To copy the code to a directory named /path/to/local/dir the
following command can be executed. The BigNLP repository for 
Slurm has been verified on both Slurm-based DeepOps clusters as well as Base 
Command Manager. 


```
srun -p [partition] -N 1 --container-mounts=/path/to/local/dir:/workspace/mount_dir --container-image=[container_tag] bash -c "cp -r /opt/bignlp/bignlp-scripts /opt/bignlp/bignlp-hp-tool /workspace/mount_dir/"
```

Install the BigNLP scripts dependencies on the head node of the cluster:

```
pip install -r requirements.txt
```
You can use virtualenv to prevent polluting your head node environment for
other Python projects. If your configuration lacks pip, then you can
install pip using use [get_pip.py](https://github.com/pypa/get-pip) with just `python3`.

##### 5.1.1.2. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>

The bignlp-scripts codebase is included as part of the training
container. Before starting, set up the ngc cli and configuration as described 
in the Base Command Platform User Guide. In this guide, we will mainly 
use two Base Command Platform workspaces, one for storing the training dataset,
and another for storing the results, checkpoints and logs. Therefore, start by 
creating these workspaces (e.g. `bignlp_data_ws` and `bignlp_results_ws`). See 
the Base Command Platform User Guide for how to create and work with Base 
Command Platform workspaces.

##### 5.1.1.3. General Configuration
<a id="markdown-general-configuration" name="general-configuration"></a>

The first parameter that must be set is the `bignlp_path` parameter inside the
`conf/config.yaml` file.    This parameter must point to the absolute path where
the `bignlp-scripts` repository is stored in the file system.    
Additionally, if using a Slurm based 
cluster, the config file in the subfolder of `conf/cluster/bcm.yaml` has the 
parameters to set the generic cluster related information, such as the 
`partition` or `account` parameters.

The NUMA mapping can also be configured from the `conf/config.yaml` file. The 
mapping should be automatic; the code will read the number of CPU cores available 
in your cluster, and provide the best possible mapping, to maximize performance. 
The mapping is enabled by default, but it can be disabled by setting 
`enable: False` in the `numa_mapping` section of the `conf/config.yaml` file. 
The type of mapping can also be configured using the same file. See the full 
config parameters below:

```yaml
numa_mapping:
  enable: True  # Set to False to disable all mapping (performance will suffer).
  mode: unique_contiguous  # One of: all, single, single_unique, unique_interleaved or unique_contiguous.
  scope: node  # Either node or socket.
  cores: all_logical  # Either all_logical or single_logical.
  balanced: True  # Whether to assing an equal number of physical cores to each process.
  min_cores: 1  # Minimum number of physical cores per process.
  max_cores: 8  # Maximum number of physical cores per process. Can be null to use all available cores.
```


**Slurm**: The `bignlp_path` parameter will automatically be mounted to the
container at the same path as in the local file system. Any additional
directories that should be mounted must be specified using the
`container_mounts` parameter. If the paths contain the colon character (`:`), 
the code will assume both the source and destination paths are provided. 
Otherwise, the given paths will be mounted to the same path inside the container.
The `data_dir` parameter can also be
modified to point to where the dataset will be loaded from or saved. The 
`base_results_dir` can also be modified to point to where the results, 
checkpoints and logs will be stored. These last two parameters will be 
automatically mounted into the container. The parameters `cluster` and `cluster_type`
must be set to `bcm` for all the tasks.

**Base Command Platform**: The `bignlp_path` should be set to 
/opt/bignlp/bignlp-scripts , which is the default location where the scripts 
are located inside the container. The `data_dir` parameter can also be
modified to point to where the dataset will be loaded from or saved. The 
`base_results_dir` can also be modified to point to where the results, 
checkpoints and logs will be stored. In the case of Base Command Platform, we recommend 
that `data_dir` points to one of the workspaces, and `base_results_dir` 
points to the other. They should both be mounted in read and write (RW) 
mode. The parameter `cluster_type` must be set to `bcp` for all the tasks.

`main.py` is the main file that needs to be executed to run the data
preparation, training, conversion, fine-tuning, and evaluation pipelines. Each of these 
pipelines has a parameter in the `conf/config.yaml` file that decides whether 
to run that pipeline or not. In slurm based clusters, all of them can be set 
to `True` at the same time, and they will be executed in order. However, in Base Command Platform, 
only one of them should be set to `True` at a time.

[//]: # (##### 5.1.1.3.1. Settings for GPT-3 Models )

[//]: # (<a id="markdown-settings-for-gpt-3-models" name="settings-for-gpt-3-models"></a>)

**Settings for GPT-3 Models**: Default settings for GPT-3 models are in the `config/config.yaml` file:

```yaml
run_data_preparation: True
run_training: True
run_conversion: True
run_finetuning: False  # Fine-tuning is only supported in T5 models.
run_evaluation: True
```

[//]: # (##### 4.1.1.3.2. Settings for T5 Models )

[//]: # (<a id="markdown-settings-for-t5-models" name="settings-for-t5-models"></a>)

**Settings for T5 Models**: Default settings for T5 models are in the `config/config.yaml` file:
```yaml
# default values:
cluster: bcm  # Leave it as bcm even if using bcp. It will be ignored for bcp.
data_preparation: download_t5_pile
training: t5/220m
conversion: convert_t5
finetuning: t5/mnli
evaluation: t5/mnli_matched

run_data_preparation: True
run_training: True
run_conversion: True
run_finetuning: True
run_prompt_learning: False
run_evaluation: True
```

**Settings for mT5 Models**: Default settings for T5 models are in the `config/config.yaml` file:
```yaml
# default values:
cluster: bcm  # Leave it as bcm even if using bcp. It will be ignored for bcp.
data_preparation: download_mc4
training: mt5/390m
conversion: convert_mt5
finetuning: mt5/xnli
evaluation: mt5/xnli

run_data_preparation: True
run_training: True
run_conversion: True
run_finetuning: True
run_prompt_learning: False
run_evaluation: True
```

To run these pipelines execute:

```
python3 main.py
```

The entire repository uses `hydra/omegaconf` to handle job configuration using
YAML files, so look at the documentation for those projects to learn more.

#### 5.1.2. Data Preparation
<a id="markdown-data-preparation" name="data-preparation"></a>

**The Pile**: We provide utilities to download and prepare [the Pile](https://pile.eleuther.ai/)
dataset ([mirror](https://mystic.the-eye.eu/public/AI/pile/train/)),
which is formed by 22 smaller datasets. The dataset is already blended
by using the mix described in their [paper](https://arxiv.org/pdf/2101.00027.pdf).
It is recommended to store this repository and the datasets in a file system
shared by all the nodes (gpfs) in the case of Slurm based clusters, and in a shared 
workspace with RW permissions in the case of Base Command Platform based clusters.

The Pile dataset consists of 30 shards. Downloading, extracting, and
preprocessing each file takes approximately 1 hour assuming a 30 MB/s download
speed. The data preparation can be parallelized by using up to 30 nodes. 


**mC4**: We provide utilities to download and prepare [mC4](https://www.tensorflow.org/datasets/catalog/c4)
dataset ([allen-ai version](https://huggingface.co/datasets/allenai/c4)). Multilingual C4 (mC4) 
has 101 languages and is generated from 71 [Common Crawl](https://commoncrawl.org/) dumps. 
It is recommended to store this repository and the datasets in a file system
shared by all the nodes (gpfs) in the case of Slurm based clusters, and in a shared 
workspace with RW permissions in the case of Base Command Platform based clusters.

Our scripts give user options to choose any subset of 101 languages to download and preprocess.
We curated 24 languages as our default language list. The raw size of default languages is around 5 TB.
Parallelization is enabled in downloading and preprocessing scripts. It will help to automatically
distribute and balance the work on multi-node systems and provide significant speed up.
Downloading and preprocessing the default language list takes approximately 7 hours 
assuming a 30 MB/s download speed and parallelization by using 20 nodes. The preprocessed dataset has a size 
of around 12 TB. It's recommended to use a file system with larger than 20 TB storage to prepare the data.

Currently, we don't support training with more than 25 languages, see [Known Issues].

The configuration used for data preparation for the Pile dataset or mC4 dataset must be specified in the
`conf/config.yaml` file and `run_data_preparation` must be set to `True` to run it.


##### 5.1.2.1. Data Preparation for GPT-3 Models
<a id="markdown-data-preparation-for-gpt-3-model" name="data-preparation-for-gpt-3-model"></a>
The `data_preparation` parameter in `conf/config.yaml` specifies which file to use for data preparation
configuration purposes. The default value is set to `download_gpt3_pile`, which can be
found in `conf/data_preparation/download_gpt3_pile.yaml`. It is used to download, extract,
and preprocess the Pile dataset for GPT-3 model. The parameters can be
modified to perform the different tasks and to decide where to store the
datasets, vocab, and merge files.

To download a reduced portion of the dataset to run tests, the 
`file_numbers` parameter can be updated to download only one of the 
shards by changing “0-29” to “0” (the syntax must be a combination of
numbers separated by dashes "-" or commas ",") For example, 
`file_numbers`="0,3,5-7" will download and prepare 
files 0, 3, 5, 6, and 7.

###### 5.1.2.1.1. Slurm
<a id="markdown-41211-slurm" name="41211-slurm"></a>

First, ensure the cluster related configuration in the `conf/cluster/bcm.yaml` file is correct.
The `cluster` and `cluster_type` parameters in `conf/config.yaml` must be set to `bcm`.
Then, modify the `time_limit` or any other parameter related to the job in the `download_gpt3_pile.yaml`
file for GPT-3 models.
The data preparation can be parallelized by using up to 30 nodes to download all 30 files in parallel.

Example:

To run only the data preparation pipeline and not the training, evaluation or
inference pipelines, set the `conf/config.yaml` file to:
```yaml
run_data_preparation: True
run_training: False
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: False
```

And then run:
```
python3 main.py
```

###### 5.1.2.1.2. Base Command Platform
<a id="markdown-41212-base-command-platform" name="41212-base-command-platform"></a>

In order to run the data preparation script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. 
By default, the data preparation script will download the data into the `bignlp-scripts/data/` directory.
We recommend that the `data_dir` parameter is set to a workspace, so that the data 
is visible across multiple jobs later on. The vocab and merge files should also be 
stored to the same workspace as the dataset, for later usage. The data preparation code 
must be launched in a multi-node job. It can be parallelized to use between 2 and 30 nodes for faster preparation of the dataset.

With Base Command Platform, the 700+ GB dataset can be downloaded once and then
shared by multiple users in the same ACE by setting the permissions of the `bignlp_data_ws` workspace.

To run the data preparation pipeline for GPT-3 models, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py run_data_preparation=True run_training=False run_conversion=False run_finetuning=False    \
run_evaluation=False cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data/the_pile_gpt3 \
base_results_dir=/mount/results data_preparation.file_numbers='0-29' \
data_preparation.vocab_save_dir=/mount/data/bpe data_preparation.merges_save_dir=/mount/data/bpe >> /results/data_gpt3_log.txt 2>&1
```

The command above assumes you want to prepare the entire dataset (files 0-29), and you mounted the data 
workspace in `/mount/data`, and the results workspace in `/mount/results`. Stdout and stderr are redirected to the `/results/data_gpt3_log.txt` file, so it can be downloaded from NGC. 
Any other parameter can also be added to the command to modify its behavior.

###### 5.1.2.1.3. Common
<a id="markdown-41213-common" name="41213-common"></a>

Set the configuration for the data preparation job for GPT-3 models in the YAML file:
```yaml
dataset: pile    # Dataset name
download_the_pile: True    # Whether to download the Pile dataset from the internet.
the_pile_url: "https://mystic.the-eye.eu/public/AI/pile/train/"    # Source URL to download the Pile dataset from.
file_numbers: "0-29"    # The Pile dataset consists of 30 files (0-29), choose which ones to download.
preprocess_data: True    # True to preprocess the data from a jsonl file, False otherwise.
download_vocab_url: "https://huggingface.co/gpt2/resolve/main/vocab.json"    # URL to download the vocab from.
download_merges_url: "https://huggingface.co/gpt2/resolve/main/merges.txt"    # URL to download the merges from.
vocab_save_dir: ${data_dir}/bpe
merges_save_dir: ${data_dir}/bpe
tokenizer_type: GPT2BPETokenizer
log_dir: ${base_results_dir}/data_preparation/gpt3_pile_logs    # Where to save the logs
rm_downloaded: True # Extract script will remove downloaded zst after extraction
rm_extracted: True # Preprocess script will remove extracted files after preproc.
nodes: 30
time_limit: "4:00:00"
bcp_preproc_npernode: 2 # 2 should be safe to use and x2 times faster.
```

##### 5.1.2.2. Data Preparation for T5 Models
<a id="markdown-data-preparation-for-t5-models" name="data-preparation-for-t5-models"></a>
The `data_preparation` parameter in `conf/config.yaml` specifies which file to use for data preparation
configuration purposes. The `data_preparation` parameter needs to be specified as `download_t5_pile` for
preparing the Pile dataset for T5 models. The config file can be found in 
`conf/data_preparation/download_t5_pile.yaml`. GPT-3 models and T5 models use
different tokenizer and vocab files. The default parameters can be found in the
corresponding config files.

To download a reduced portion of the dataset to run tests, the 
`file_numbers` parameter can be updated to download only one of the 
shards by changing `“0-29”` to `“0”` (the syntax must be a combination of
numbers separated by dashes "-" or commas ",").
 For example, `file_numbers`=`"0,3,5-7"` will download and prepare 
files 0, 3, 5, 6, and 7.

###### 5.1.2.2.1. Slurm
<a id="markdown-41221-slurm" name="41221-slurm"></a>

First, ensure the cluster configuration settings in the `conf/cluster/bcm.yaml` file are correct.
The `cluster` and `cluster_type` parameters in `conf/config.yaml` must be set to `bcm`.
Then, modify the `time_limit` or any other parameter related to the job in the `download_t5_pile.yaml`
file for T5 models.
The data preparation can be parallelized by using up to 30 nodes to download all 30 files in parallel.

Example:

To run only the data preparation pipeline and not the training, evaluation or
inference pipelines, set the `conf/config.yaml` file to:
```yaml
run_data_preparation: True
run_training: False
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: False
```

And then run:
```
python3 main.py
```

###### 5.1.2.2.2. Base Command Platform
<a id="markdown-41222-base-command-platform" name="41222-base-command-platform"></a>

In order to run the data preparation script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. 
By default, the data preparation script will download the data into the `bignlp-scripts/data/` directory.
We recommend that the `data_dir` parameter is set to a workspace, so that the data 
is visible across multiple jobs later on. The vocab and merge files should also be 
stored to the same workspace as the dataset. The data preparation code 
must be launched in a multi-node job, and can be parallelized to use between 2 and 30 nodes, 
for faster parallel preparation of the dataset.

With Base Command Platform, the 700+ GB dataset can be downloaded once and then
shared by multiple users in the same ACE by setting the permissions of the `bignlp_data_ws` workspace.

To run the data preparation pipeline for T5 models, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py data_preparation=download_t5_pile run_data_preparation=True \
run_training=False run_conversion=False run_finetuning=False run_evaluation=False run_finetuning=False \
cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data/the_pile_t5 \
base_results_dir=/mount/results data_preparation.file_numbers='0-29' \
data_preparation.vocab_save_dir=/mount/data/bpe >> /results/data_t5_log.txt 2>&1
```

The command above assumes you want to prepare the entire dataset (files 0-29), and you mounted the data 
workspace in `/mount/data`, and the results workspace in `/mount/results`. The stdout and stderr outputs will
also be redirected to the `/results/data_t5_log.txt` file, to be able to download the logs from NGC. 
Any other parameter can also be added to the command to modify its behavior.

###### 5.1.2.2.3. Common
<a id="markdown-41223-common" name="41223-common"></a>

Set the configuration for the data preparation job for T5 models in the YAML file:
```yaml
dataset: pile
download_the_pile: True    # Whether to download the pile dataset from the internet.
the_pile_url: "https://mystic.the-eye.eu/public/AI/pile/train/"    # Source URL to download The Pile dataset from.
file_numbers: "0-29"    # The pile dataset consists of 30 files (0-29), choose which ones to download.
preprocess_data: True    # True to preprocess the data from a jsonl file, False otherwise.
download_vocab_url: "https://s3.amazonaws.com/models.huggingface.co/bert/bert-large-cased-vocab.txt"    # URL to download the vocab from.
download_merges_url: null
vocab_save_dir: ${data_dir}/bpe
merges_save_dir: ${data_dir}/bpe
tokenizer_type: BertWordPieceCase # T5 models use BertWordPieceCase tokenizer
log_dir: ${base_results_dir}/data_preparation/t5_pile_logs    # Where to save the logs
rm_downloaded: True # Extract script will remove downloaded zst after extraction
rm_extracted: True # Preprocess script will remove extracted files after preproc.
nodes: 30
time_limit: "4:00:00"
bcp_preproc_npernode: 2 # 2 should be safe to use and x2 times faster.
```


##### 5.1.2.3. Data Preparation for mT5 Models
<a id="markdown-data-preparation-for-mt5-models" name="data-preparation-for-mt5-models"></a>
The `data_preparation` parameter in `conf/config.yaml` specifies which file to use for data preparation
configuration purposes. The `data_preparation` parameter needs to be specified as `download_mc4` for
preparing the mC4 dataset for mT5 models. The config file can be found in 
`conf/data_preparation/download_mc4.yaml`. mT5 models use SentencePiece multilingual tokenzier.

To download a reduced portion of the dataset to run tests, the 
`languages` parameter can be updated to download only one of the 
languages by changing it to `lv`. The list of all 101 languages can be
found in [mC4 dataset](https://www.tensorflow.org/datasets/catalog/c4#c4multilingual).

The data preparation can be parallelized by using multiple nodes (default 20 nodes) to download and preprocess 
all language files in parallel.


###### 5.1.2.3.1. Slurm
<a id="markdown-41231-slurm" name="41231-slurm"></a>

First, ensure the cluster configuration settings in the `conf/cluster/bcm.yaml` file are correct.
The `cluster` and `cluster_type` parameters in `conf/config.yaml` must be set to `bcm`.
Then, modify the `time_limit` or any other parameter related to the job in the `download_mc4.yaml`
file for mT5 models.

Example:

To run only the data preparation pipeline and not the training, evaluation or
inference pipelines, set the `conf/config.yaml` file to:
```yaml
run_data_preparation: True
run_training: False
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: False
```

And then run:
```
python3 main.py
```

###### 5.1.2.3.2. Base Command Platform
<a id="markdown-41232-base-command-platform" name="41232-base-command-platform"></a>

In order to run the data preparation script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. 
By default, the data preparation script will download the data into the `bignlp-scripts/data/` directory.
We recommend that the `data_dir` parameter is set to a workspace, so that the data 
is visible across multiple jobs later on. The tokenizer model file should also be 
stored to the same workspace as the dataset. The data preparation code 
must be launched in a multi-node job, and can be parallelized to use between 2 and 30 nodes, 
for faster parallel preparation of the dataset.

With Base Command Platform, the dataset can be downloaded once and then
shared by multiple users in the same ACE by setting the permissions of the `bignlp_data_ws` workspace.

To run the data preparation pipeline for mT5 models, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py data_preparation=download_mc4 run_data_preparation=True \
run_training=False run_conversion=False run_finetuning=False run_evaluation=False run_finetuning=False \
cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data \
base_results_dir=/mount/results data_preparation.languages=\'cs,da,de,el,en,es,fi,fr,hi,hu,it,ja,ko,lt,lv,nl,no,pl,pt,ro,ru,sk,sv,zh\' \
data_preparation.nodes=20 data_preparation.workers_per_node=4 >> /results/data_mt5_log.txt 2>&1
```

The command above assumes you want to prepare the mC4 dataset with 24 languages, and you mounted the data 
workspace in `/mount/data`, and the results workspace in `/mount/results`. The stdout and stderr outputs will
also be redirected to the `/results/data_mt5_log.txt` file, to be able to download the logs from NGC. The full dataset may not fit into BCP workspaces. We recommand using a smaller subset of languages (total size is 1TB, e.g. `cs,da,de,el,fr,hi`).
Any other parameter can also be added to the command to modify its behavior.

###### 5.1.2.3.3. Common
<a id="markdown-41233-common" name="41233-common"></a>

Set the configuration for the data preparation job for mT5 models in the YAML file:
```yaml
dataset: mc4
download_mc4: True  # Whether to download the mC4 dataset from the internet.
preprocess_data: True  # True to preprocess the data from a json.gz file, False otherwise.
mc4_dir: ${data_dir}/mc4 # Path to (m)C4 dataset repo.
git_lfs_dir: ${.mc4_dir}/lfs # Path to store git lfs files.
download_vocab_url: https://storage.googleapis.com/t5-data/vocabs/mc4.250000.100extra/sentencepiece.vocab # URL to download the vocab from.
download_tokenizer_url: https://storage.googleapis.com/t5-data/vocabs/mc4.250000.100extra/sentencepiece.model # URL to download tokenizer from
vocab_save_dir: ${.mc4_dir}/bpe
tokenizer_save_dir: ${.mc4_dir}/bpe
tokenizer_model: ${.tokenizer_save_dir}/mt5_tokenizer.model
languages: cs,da,de,el,en,es,fi,fr,hi,hu,it,ja,ko,lt,lv,nl,no,pl,pt,ro,ru,sk,sv,zh # language list in mC4 dataset to download and preprocess. Use `all` to download and preprocess all languages or specify language list as `en,es,ko,zh,...`
use_cleaned_english: True # whether to use cleaned version of english data
softlinks_dir: ${.mc4_dir}/softlinks # Path to languages soft links for preprocessing
preprocessed_dir: ${.mc4_dir}/preprocessed
download_worker_mapping: ${.mc4_dir}/download_mapping
preprocess_worker_mapping: ${.mc4_dir}/preprocess_mapping
log_dir: ${base_results_dir}/data_preparation/mc4_logs  # Where to save the logs
rm_downloaded: False # Script will not remove downloaded after preprocessing
nodes: 20
cpus_per_node: 256 # 256 cpus for A100(80G)
time_limit: "24:00:00"
workers_per_node: 4 # Number of workers per node in preprocessing step.
```


### 5.2. Training with Predefined Configurations
<a id="markdown-training-with-predefined-configurations" name="training-with-predefined-configurations"></a>

#### 5.2.1. Predefined Configurations of GPT-3 Models
<a id="markdown-predefined-configurations-of-gpt-3-models" name="predefined-configurations-of-gpt-3-models"></a>

We provide five configurations for several different GPT-3 model sizes: 126M, 5B, 20B, 
40B, and 175B parameters. These configurations include carefully selected
hyperparameters, which should be used as a guideline for any custom model
configurations. All these configurations are provided in the `conf/training/gpt3/`
directory. The desired configuration can be chosen by selecting the `training` 
parameter in the `conf/config.yaml` file.
For Base Command Platform, all jobs must be launched in multi-node mode.

**126M configuration:**

The 126M model uses the bf16 data type. It can be trained in about 1 day using 8 nodes with 8 GPUs per node. The model includes 12 transformer layers, a hidden size of 768,
and 12 attention heads. The sequence length is 2048, and the optimizer is
Adam. This model does not use any model parallelism. See the `gpt3/126m.yaml` config file for parameter details.

To train a 126M model on a Slurm cluster, modify the `conf/config.yaml` file to set:
```yaml
- training: gpt3/126m
run_training: True
```

And run:
```
python3 main.py
```

To train a 126M GPT-3 model on Base Command Platform cluster on 8 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=gpt3/126m run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_gpt3 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.json \
training.model.tokenizer.merge_file=/mount/data/bpe/merges.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively, and that the $NGC_ARRAY_SIZE will use the number of nodes selected when 
creating the job (number of replicas). 

To train with fewer or a different number of nodes, the relevant parameters 
can be adjusted either in the yaml config file or 
from the command line. More on this in [section 5.7](#57-resuming-training-from-fewer-nodes). 
For Base Command Platform, all jobs must be launched in multi-node mode.

**5B configuration:**

The 5B model uses the bf16 data type. It can be trained in about 7 days using 20 nodes with 8 GPUs per node. The model includes 24
transformer layers, a hidden size of 4096, and 32 attention heads. The
sequence length is 2048, and the optimizer is Adam. This model uses tensor
parallelism of 2. For the details on all the parameters, see the 5b.yaml
config file.

To train a 5B GPT-3 model, modify the `conf/config.yaml` file to set:
```yaml
- training: gpt3/5b
run_training: True
```

And run:
```
python3 main.py
```

To train a 5B GPT-3 model on Base Command Platform cluster on 20 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=gpt3/5b run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_gpt3 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.json \
training.model.tokenizer.merge_file=/mount/data/bpe/merges.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively, and that the $NGC_ARRAY_SIZE will use the number of nodes selected when 
creating the job (number of replicas).


**20B configuration:**

The 20B model uses the bf16 data type. It can be trained in about 7 days using 80 nodes with 8 GPUs per node. The model includes 44
transformer layers, a hidden size of 6144, and 48 attention heads. The
sequence length is 2048, and the optimizer is Adam. This model uses tensor
parallelism of 8. For the details on all the parameters, see the 20b.yaml
config file.

To train a 20B GPT-3 model, modify the `conf/config.yaml` file to set:
```yaml
- training: gpt3/20b
run_training: True
```

And run:
```
python3 main.py
```

To train a 20B GPT-3 model on Base Command Platform cluster on 80 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=gpt3/20b run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False    run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_gpt3 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.json \
training.model.tokenizer.merge_file=/mount/data/bpe/merges.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively, and that the $NGC_ARRAY_SIZE will use the number of nodes selected when 
creating the job (number of replicas).

**40B configuration:**

The 40B model uses the bf16 data type. It can be trained in about 12 days using 80 nodes with 8 GPUs per node. The model includes 48
transformer layers, a hidden size of 8192, and 64 attention heads. The
sequence length is 2048, and the optimizer is Adam. This model uses tensor
parallelism of 8 and pipeline parallelism of 4. 
For the details on all the parameters, see the 40b.yaml config file.

To train a 40B GPT-3 model, modify the `conf/config.yaml` file to set:
```yaml
- training: gpt3/40b
run_training: True
```

And run:
```
python3 main.py
```

To train a 40B GPT-3 model on Base Command Platform cluster on 80 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=gpt3/40b run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False    run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_gpt3 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.json \
training.model.tokenizer.merge_file=/mount/data/bpe/merges.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively, and that the $NGC_ARRAY_SIZE will use the number of nodes selected when 
creating the job (number of replicas).

**175B configuration:**

The 175B model uses the bf16 data type. It can be trained in about 35 days using 128 nodes with 8 GPUs per node. The model includes 96
transformer layers, a hidden size of 12288, and 96 attention heads. The
sequence length is 2048, and the optimizer is Adam. This model uses tensor
parallelism of 8 and pipeline parallelism of 16. 
For the details on all the parameters, see the 175b.yaml config file.

To train a 175B GPT-3 model, modify the `conf/config.yaml` file to set:
```yaml
- training: gpt3/175b
run_training: True
```

And run:
```
python3 main.py
```

To train a 175B GPT-3 model on Base Command Platform cluster on 128 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=gpt3/175b run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False    run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_gpt3 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.json \
training.model.tokenizer.merge_file=/mount/data/bpe/merges.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively, and that the $NGC_ARRAY_SIZE will use the number of nodes selected when 
creating the job (number of replicas).

#### 5.2.2. Predefined Configurations of T5 Models
<a id="markdown-predefined-configurations-of-t5-models" name="predefined-configurations-of-t5-models"></a>

We provide configuration files for two T5 model sizes: 220M and
3B parameters. These configurations include carefully selected
hyperparameters, which should be used as guidelines for any custom model
configurations. The configuration files are provided in the `conf/training/t5`
directory. The desired configuration can be chosen by selecting the training
 parameter in the `conf/config.yaml` file.
For Base Command Platform, all jobs must be launched in multi-node mode.

**220M configuration:**

The 220M model uses the bf16 data type. It can be trained in about 4 days using 4 nodes with 8 GPUs per node. 
The model includes 12 transformer layers, a hidden size of 768, a feedforward network size of 2048,
and 12 attention heads with GeGLU activation function. The sequence length is 512, and the optimizer is
Adam. This model does not use any model parallelism. See the `t5/220m.yaml` config file for parameter details.

To train a 220M model on a Slurm cluster, modify the `conf/config.yaml` file to set:
```yaml
training: t5/220m
run_training: True
```

And run:
```
python3 main.py
```

To train a 220M model on Base Command Platform cluster on 4 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=t5/220m run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False    run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_t5 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively. `$NGC_ARRAY_SIZE` is automatically set to the number of nodes that will be used when creating the job (number of replicas). 

To train with a different number of nodes, the relevant parameters 
(e.g. `micro_batch_size`) can be adjusted either in the appropriate yaml config file or 
from the command line. More on this in [section 5.7](#57-resuming-training-from-fewer-nodes). 
For Base Command Platform, all jobs must be launched in multi-node mode.

**3B configuration:**

The 3B model uses the bf16 data type. It can be trained in about 11 days using 20 nodes with 8 GPUs per node. The model includes 24
transformer layers, a hidden size of 2048, a feedforward network size of 5120, and 32 attention heads  with GeGLU activation function. The
sequence length is 512, and the optimizer is Adam. This model uses tensor
parallelism of 2. For the details on all the parameters, see the `t5/3b.yaml`
config file.

To train a 3B model, modify the `conf/config.yaml` file to set:
```yaml
training: t5/3b
run_training: True
```

And run:
```
python3 main.py
```

To train a 3B model on Base Command Platform cluster on 20 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=t5/3b run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False    run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_t5 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively. `$NGC_ARRAY_SIZE` is automatically set to the number of nodes that will be used when creating the job (number of replicas).



**11B configuration:**

The 11B model uses the bf16 data type. It can be trained in about 40 days using 20 nodes with 8 GPUs per node. The model includes 24
transformer layers, a hidden size of 4096, a feedforward network size of 10240, and 64 attention heads  with GeGLU activation function. The
sequence length is 512, and the optimizer is Adam. This model uses tensor
parallelism of 4. For the details on all the parameters, see the `t5/11b.yaml`
config file.

To train a 11B model, modify the `conf/config.yaml` file to set:
```yaml
training: t5/11b
run_training: True
```

And run:
```
python3 main.py
```

To train a 11B model on Base Command Platform cluster on 20 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=t5/11b run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False    run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_t5 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively. `$NGC_ARRAY_SIZE` is automatically set to the number of nodes that will be used when creating the job (number of replicas).



**23B configuration:**

The 23B model uses the bf16 data type. It can be trained in about 55 days using 40 nodes with 8 GPUs per node. The model includes 36
transformer layers, a hidden size of 5120, a feedforward network size of 10880, and 64 attention heads with GeGLU activation function. The
sequence length is 512, and the optimizer is Adam. This model uses tensor
parallelism of 4 and pipeline parallelism of 2. For the details on all the parameters, see the `t5/23b.yaml`
config file.

To train a 23B model, modify the `conf/config.yaml` file to set:
```yaml
training: t5/23b
run_training: True
```

And run:
```
python3 main.py
```

To train a 23B model on Base Command Platform cluster on 40 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=t5/23b run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False    run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_t5 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively. `$NGC_ARRAY_SIZE` is automatically set to the number of nodes that will be used when creating the job (number of replicas).


**41B configuration:**

The 41B model uses the bf16 data type. It can be trained in about 91 days using 40 nodes with 8 GPUs per node. The model includes 36
transformer layers, a hidden size of 6144, a feedforward network size of 10880, and 96 attention heads with GeGLU activation function. The
sequence length is 512, and the optimizer is Adam. This model uses tensor
parallelism of 4 and pipeline parallelism of 4. For the details on all the parameters, see the `t5/23b.yaml`
config file.

To train a 41B model, modify the `conf/config.yaml` file to set:
```yaml
training: t5/41b
run_training: True
```

And run:
```
python3 main.py
```

To train a 41B model on Base Command Platform cluster on 40 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=t5/41b run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False run_evaluation=False bignlp_path=/opt/bignlp/bignlp-scripts \
data_dir=/mount/data/the_pile_t5 base_results_dir=/mount/results training.trainer.num_nodes=\$NGC_ARRAY_SIZE \
training.model.tokenizer.vocab_file=/mount/data/bpe/vocab.txt cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively. `$NGC_ARRAY_SIZE` is automatically set to the number of nodes that will be used when creating the job (number of replicas).



#### 5.2.3. Predefined Configurations of mT5 Models
<a id="markdown-predefined-configurations-of-mt5-models" name="predefined-configurations-of-mt5-models"></a>

We provide configuration files for three mT5 model sizes: 170M, 390M, and
3B parameters. These configurations include carefully selected
hyperparameters, which should be used as guidelines for any custom model
configurations. The configuration files are provided in the `conf/training/mt5`
directory. The desired configuration can be chosen by selecting the training
 parameter in the `conf/config.yaml` file.
For Base Command Platform, all jobs must be launched in multi-node mode.

**170M configuration:**

The 170M model uses the bf16 data type. It can be trained in about 4 days using 4 nodes with 8 GPUs per node. 
The model includes 8 transformer layers, a hidden size of 512, a feedforward network size of 1024,
and 6 attention heads with GeGLU activation function. The sequence length is 512, and the optimizer is
Adam. This model does not use any model parallelism. See the `mt5/170m.yaml` config file for parameter details.

To train a 170M model on a Slurm cluster, modify the `conf/config.yaml` file to set:
```yaml
training: mt5/170m
run_training: True
```

And run:
```
python3 main.py
```

To train a 170M model on Base Command Platform cluster on 4 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=mt5/170m run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False run_evaluation=False \
bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data base_results_dir=/mount/results \
training.trainer.num_nodes=\$NGC_ARRAY_SIZE cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively. `$NGC_ARRAY_SIZE` is automatically set to the number of nodes that will be used when creating the job (number of replicas). 

To train with a different number of nodes, the relevant parameters 
(e.g. `micro_batch_size`) can be adjusted either in the appropriate yaml config file or 
from the command line. More on this in [section 5.7](#57-resuming-training-from-fewer-nodes). 
For Base Command Platform, all jobs must be launched in multi-node mode.



**390M configuration:**

The 390M model uses the bf16 data type. It can be trained in about 4 days using 8 nodes with 8 GPUs per node. 
The model includes 8 transformer layers, a hidden size of 512, a feedforward network size of 2048,
and 12 attention heads with GeGLU activation function. The sequence length is 512, and the optimizer is
Adam. This model does not use any model parallelism. See the `mt5/390m.yaml` config file for parameter details.

To train a 390M model on a Slurm cluster, modify the `conf/config.yaml` file to set:
```yaml
training: mt5/390m
run_training: True
```

And run:
```
python3 main.py
```

To train a 390M model on Base Command Platform cluster on 8 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=mt5/390m run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False run_evaluation=False \
bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data base_results_dir=/mount/results \
training.trainer.num_nodes=\$NGC_ARRAY_SIZE cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively. `$NGC_ARRAY_SIZE` is automatically set to the number of nodes that will be used when creating the job (number of replicas). 



**3B configuration:**

The 3B model uses the bf16 data type. It can be trained in about 14 days using 20 nodes with 8 GPUs per node. The model includes 24
transformer layers, a hidden size of 2048, a feedforward network size of 5120, and 32 attention heads with GeGLU activation function. The
sequence length is 512, and the optimizer is Adam. This model uses tensor
parallelism of 2. For the details on all the parameters, see the `mt5/3b.yaml`
config file.

To train a 3B model, modify the `conf/config.yaml` file to set:
```yaml
training: mt5/3b
run_training: True
```

And run:
```
python3 main.py
```

To train a 3B model on Base Command Platform cluster on 20 nodes, use the command:
```
python3 /opt/bignlp/bignlp-scripts/main.py training=mt5/3b run_training=True \
run_data_preparation=False run_conversion=False run_finetuning=False run_evaluation=False \
bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data base_results_dir=/mount/results \
training.trainer.num_nodes=\$NGC_ARRAY_SIZE cluster_type=bcp
```
The command above assumes that the data and results workspaces are mounted in the `/mount/data` and `/mount/results` 
directories respectively. `$NGC_ARRAY_SIZE` is automatically set to the number of nodes that will be used when creating the job (number of replicas).



#### 5.2.4. Training Logs with TensorBoard and Weights & Biases
<a id="markdown-training-with-tb-wandb" name="training-with-tb-wandb"></a>
The training code can log the model and system related metrics to both TensorBoard and 
Weights & Biases (W&B). The local files will be stored in the directory specified in the 
`training.exp_manager.explicit_log_dir` parameter. TensorBoard logs are saved by default.

However, W&B needs the API key to be specified to work properly. To upload the logs to W&B, 
the user must first store the W&B API key to a file (on the first line of the file), and 
select the path to the file that contains the key using the `wandb_api_key_file` parameter. 
For Base Command Platform, this file can be stored in a dataset or workspace mounted to the job.
To enable the logging of the training metrics to W&B, the following training parameters must be set:
```yaml
exp_manager:
        create_wandb_logger: True
        wandb_logger_kwargs:
            project: [W&B project name]
            name: [W&B run name]
```

The logs show the reduced_train_loss, val_loss, train_step_timing (which is the best way 
to measure the time it takes to finish each global step), and other relevant metrics.

### 5.3. Using the HP Tool to Find the Optimal Configuration
<a id="markdown-using-the-hp-tool-to-find-the-optimal-configuration" name="using-the-hp-tool-to-find-the-optimal-configuration"></a>
This tool searches for the Hyper-Parameters (HPs) that achieve the highest throughput for training 
Large Language Models (LLMs) using NeMo-Megatron. It also searches for the inference HPs that 
achieve the highest throughput and the lowest latency.

#### 5.3.1. HP Tool Capabilities
<a id="markdown-hp-tool-capabilities" name="hp-tool-capabilities"></a>

The Hyper-Parameter (HP) tool is intended to quickly iterate over different model configurations, 
to find the best configuration with minimal time and money spending. To achieve that, our 
tool provides several different capabilities, as shown in the table below:

| Feature                              | GPT-3 | T5  | mT5 |
| ------------------------------------ | ----- | --- | --- |
| Model Size Recommendation            | Yes   | Yes | Yes |
| Base Config Generation               | Yes   | Yes | Yes |
| Training HP Search                   | Yes   | Yes | Yes |
| Parallel Training HP Search          | Yes   | Yes | Yes |
| Inference HP Search                  | Yes   | No  | No  |
| Parallel Inference HP Search         | No    | No  | No  |
| SLURM Based Clusters                 | Yes   | Yes | Yes |
| Base Command Platform Based Clusters | No    | No  | No  |

##### 5.3.1.1. Model Size Recommendation
<a id="markdown-model-size-recommendation" name="model-size-recommendation"></a>

For users who do not know what model size they wish to train, our tool is capable of recommending 
a model size, given the hardware and training constraints. If the number of GPUs, the TFLOPS per GPU, 
the maximum time to train, and the number of tokens to train for are known, then our tool can 
recommend a model size that can be trained with the specified hardware and time constraints.

For example, if the user has 20 NVIDIA DGX nodes available (80GB GPU memory), and wants to train a 
GPT-3 model for a maximum of 5 days, the tool will recommend using a 5B parameter GPT-3 model. 
The tool will perform a best effort guess using heuristics, so the results might not be exact.


##### 5.3.1.2. Base Config Generation
<a id="markdown-base-config-generation" name="base-config-generation"></a>

If the model size is provided by the user, or after the model size is suggested, 
the tool will generate a base configuration for the given model. This configuration will be a valid, 
runnable configuration in YAML format, which can be trained using NeMo-Megatron. However, this config 
will not be optimized at this stage.


##### 5.3.1.3. Training HP Search
<a id="markdown-training-hp-search" name="training-hp-search"></a>

Given the input model size and the base configuration, 
the tool will now search over four different critical Hyper-Parameters, that have great impact on the 
training throughput: Tensor Parallelism (TP), Pipeline Parallelism (PP), Micro Batch Size (MBS), 
and Activation Checkpointing Layers (ActCkpt).

First, the tool will use heuristics to choose good candidates for those four parameters to generate 
the grid of candidate configurations. All the candidate configurations will be saved to the results directory, 
and will include YAML files with the corresponding config. NOTE: some of these configurations might not work, 
due to high memory usage or for other reasons. The next step will determine which configurations are valid.

Once all the candidate configurations are generated, the tool will use heuristics to sort the most promising 
candidate configurations. Then, the tool will launch the most promising candidates in parallel, where the number 
of candidates can be set by the `limit_search_runs` parameter, to perform a grid search over the four training 
parameters. This search will launch the 
jobs using NeMo-Megatron, and it will train each config for a maximum of `max_minutes_per_run` minutes 
and a maximum of `max_steps_per_run` training steps, whichever is reached first on the 
target cluster. During this search, the jobs will run in the minimum number of nodes required by default, using 
Data Parallelism of 1 (DP=1) in most cases, but the number of nodes can be manually overriden using the 
`override_search_num_nodes`. Once all the jobs have finished running, the final result will be summarized in a 
CSV file.


##### 5.3.1.4. Inference HP Search
<a id="markdown-inference-hp-search" name="inference-hp-search"></a>

The tool can also search the best HPs for inference purposes. It will empirically measure the 
throughput and latency for each given configuration in the grid search space, and return a comprehensive 
table with all the numbers. The tool will search over three different critical HPs, which have great 
impact on the inference throughput and latency: Tensor Parallelism (TP), Pipeline Parallelism (PP), and 
Batch Size (BS). Technically, the tool is also capable of searching over different input/output sequence 
lengths. However, we do not recommend adding multiple different sequence lengths to the same search, 
since the model that uses the shortest sequence lengths will always achieve higher throughput and lower 
latency. Therefore, we recommend performing several different inference searches for different sequence 
lengths.

Once the search space has been defined, the tool will launch a job for each config, and measure the 
throughput and latency. This search will launch the jobs using NeMo-Megatron on the target cluster. 
Once all the jobs have finished running, the final result will be summarized in a CSV file.


#### 5.3.2. Usage
<a id="markdown-usage" name="usage"></a>

In this section, we will explain how to run each of the stages described above. 

##### 5.3.2.1. General Configuration
<a id="markdown-general-configuration" name="general-configuration"></a>

First, our configuration setup assumes that the `/opt/bignlp/bignlp-hp-tool` and `/opt/bignlp/bignlp-scripts`
directories have been copied from the container to the local file system.

The first parameter that must be set is the `bignlp_hp_tool_path` parameter inside the `conf/config.yaml` 
file. This parameter must point to the absolute path where the `bignlp-hp-tool` repository is stored in 
the file system. Additionally, if using a Slurm-based cluster, the config file in the 
`conf/cluster/bcm.yaml` subfolder has the parameters to set the generic cluster related information, 
such as the `partition` or `account` parameters.

The `bignlp_hp_tool_path` parameter will automatically be mounted to the container at the same path as 
in the local file system. Any additional directories that should be mounted must be specified using the
`container_mounts` parameter. If the paths contain the colon character (`:`), the code will assume both 
the source and destination paths are provided. Otherwise, the given paths will be mounted to the same 
path inside the container.

The `bignlp_scripts_path` must point to the path where bignlp-scripts is located. The location 
specified in the default config should be valid if `/opt/bignlp` was extracted correctly. Next, the 
`data_dir` value must point to the path where the training dataset is located. Note that the dataset 
for GPT-3, T5 and mT5 values will be different, so modify this parameter accordingly. Follow the data 
preparation steps to learn how to download and preprocess the datasets for each model. The dataset in 
this path does not need to be the full size dataset; only a small representative sample of the dataset 
is needed, since the HP tool does not train the models to convergence. Finally, the `base_results_dir` 
parameter can be modified to point to the location where the results will be stored. See all the 
parameters for the `conf/config.yaml` file below:

```yaml
defaults:
  - _self_
  - cluster: bcm
  - search_config: gpt3/5b
  - override hydra/job_logging: stdout

run_training_hp_search: True
run_inference_hp_search: True

bignlp_hp_tool_path: ???  # Path to the location of bignlp-hp-tool codebase.
bignlp_scripts_path: ${bignlp_hp_tool_path}/../bignlp-scripts  # Path to the location of BigNLP-Inference-Scripts codebase.
data_dir: ${bignlp_scripts_path}/data
base_results_dir: ${bignlp_hp_tool_path}/results

training_container: nvcr.io/ea-bignlp/ea-participants-kt/bignlp-training:22.06.rc2-py3
inference_container: nvcr.io/ea-bignlp/bignlp-inference:22.05-py3
container_mounts:
    - null

wandb:  # Weights and Biases (W&B) logging.
  enable: False  # Whether to save logs to W&B.
  api_key_file: null  # Path to the file where the w&B api key is stored. Key must be on the first line.
  project: bignlp-hp-tool  # Name of the W&B project to store the logs in. The name of the run will be populated automatically.
```

##### 5.3.2.2. Running Predefined Configs
<a id="markdown-running-predefined-configs" name="running-predefined-configs"></a>

The predefined configs we provide have been well tested, and the outputs produced by the HP tool 
have been verified manually. Running one of these configs will first generate a base config file for 
the specified model size. Then, it will launch the training and inference grid search jobs. When 
all the jobs have finished, a final recommendation will be produced for both training and inference, 
which will show the optimal hyper-parameters for the given model.

The predefined configs can be found in the `conf/search_config` directory. Each YAML file shows one 
model type (GPT-3, T5 or mT5) and one model size (up to 175B parameters for GPT-3 and up to 42B 
parameters for T5/mT5). To run the desired config, we will need to modify the `search_config` 
parameter in the `conf/config.yaml` file. For example, if we wish to run a 5B GPT-3 model, we can 
set this value to `gpt3/5b` (the .yaml ending should not be included). 

The tool will always generate the base configuration for the given model first. Then, the 
`run_training_hp_search` and `run_inference_hp_search` parameters can be set to `True`, 
to run the training and inference HP searches, respectively. If any of these two parameters are set 
to `False`, the corresponding pipeline will not be executed. Once these parameters are set, we can 
run the tool calling `python3 main.py`. 

###### 5.3.2.2.1. Model Config
<a id="markdown-model-config" name="model-config"></a>

To run the `gpt3/5b` config, we need to set up the `conf/search_config/gpt3/5b.yaml` file correctly.
The config is split in two sections: `train_settings` and `inference_settings`. 

```yaml
train_settings:
  model_size_in_b: 5 # unit in billion parameters
  num_nodes: 20
  gpus_per_node: 8
  gpu_memory_gb: 80  # Memory per GPU, in GB. Currently 40GB and 80GB A100s supported.
  max_training_days: 5 # unit in days
  limit_search_runs: 100 # Max number of runs to be launched in parallel for grid search.
  output_top_n: 10  # The result will print the top N fastest training configs.
  max_steps_per_run: 50 # Max steps per run for the grid search.
  max_minutes_per_run: 40 # minutes per run for the grid search.
  tflops_per_gpu: 140  # Estimated tflops per GPU.
  num_tokens_in_b: 300  # Unit in billions, typically 300B for GPT3 models.
  vocab_size: 51200
  logs: ${base_results_dir}/${search_config_value}_${.gpu_memory_gb}gb  # Example base_results_dir/gpt3/126m
  override_search_num_nodes: null  # null to use the minimum required number of nodes
  tensor_parallel_sizes: null  # null to use our recommendation, or a list, such as [1, 2, 4, 8]
  pipeline_parallel_sizes: null  # null to use our recommendation, or a list, such as [1, 2, 4, 8, 10]
  micro_batch_sizes: null  # null to use our recommendation, or a list, such as [1, 2, 4, 8, 16]
  act_ckpt_layers: null  # null to use our recommendation, or a list, such as [0, 1, 2, 3]
 
inference_settings:
  vocab_size: 51200
  start_id: 50256
  end_id: 50256
  input_seq_len: 60
  output_seq_len: 20
  max_latency_ms: 1200
  top_n: 10
  logs: ${base_results_dir}/${search_config_value}  # Example base_results_dir/gpt3/126m
  tensor_parallel_sizes: [1, 2, 4, 8]
  pipeline_parallel_sizes: [1]
  max_batch_sizes: [8, 16, 32, 64, 128, 256]
```

###### 5.3.2.2.2. Base Config Generation
<a id="markdown-base-config-generation" name="base-config-generation"></a>

Every time we call `python3 main.py`, a base configuration will be generated for the given model, 
and it will be saved to the `logs` directory indicated in your config files. The base configuration 
consists of a YAML file that can be run using the NeMo-Megatron training container. However, this 
base configuration has not yet been optimized to achieve the highest possible throughput.


###### 5.3.2.2.3. Training HP Search
<a id="markdown-training-hp-search" name="training-hp-search"></a>

To run the training HP search pipeline, the parameter `run_training_hp_search` must be set to `True` 
in the `conf/config.yaml` file. The model used to search the best training HPs must be selected 
using the `search_config` parameter in `conf/config.yaml`. For example, by default, this parameter 
will be set to `gpt3/5b`, so our tool will search the optimal training HPs for a 5B parameter GPT-3 
model. The configuration for this model can be found in the `conf/search_config/gpt3/5b.yaml` file. 
To configure the behavior of the HP search, the following parameters can be modified in the 
correspoinding YAML file: 

```yaml
train_settings:
  model_size_in_b: 5 # unit in billion parameters
  num_nodes: 20
  gpus_per_node: 8
  gpu_memory_gb: 80  # Memory per GPU, in GB. Currently 40GB and 80GB A100s supported.
  max_training_days: 5 # unit in days
  limit_search_runs: 100 # Max number of runs to be launched in parallel for grid search.
  output_top_n: 10  # The result will print the top N fastest training configs.
  max_steps_per_run: 50 # Max steps per run for the grid search.
  max_minutes_per_run: 40 # minutes per run for the grid search.
  tflops_per_gpu: 140  # Estimated tflops per GPU.
  num_tokens_in_b: 300  # Unit in billions, typically 300B for GPT3 models.
  vocab_size: 51200
  logs: ${base_results_dir}/${search_config_value}_${.gpu_memory_gb}gb  # Example base_results_dir/gpt3/126m
  override_search_num_nodes: null  # null to use the minimum required number of nodes
  tensor_parallel_sizes: null  # null to use our recommendation, or a list, such as [1, 2, 4, 8]
  pipeline_parallel_sizes: null  # null to use our recommendation, or a list, such as [1, 2, 4, 8, 10]
  micro_batch_sizes: null  # null to use our recommendation, or a list, such as [1, 2, 4, 8, 16]
  act_ckpt_layers: null  # null to use our recommendation, or a list, such as [0, 1, 2, 3]
```

The `model_size_in_b` parameter indicates how many billion parameters the model should contain, and 
the tool will provide a config and HPs for a model of that size. The `num_nodes` parameter indicates 
how many nodes will be used to train this model to full convergence, after the HP search is finished. 
Therefore, it will be ignored by the HP search tool, and it will only be used when generating the 
final config YAML files. The `gpus_per_node` parameter indicates how many GPUs are available in each 
node. To modify the behavior of the heuristics depending on whether 40gb or 80gb A100 GPUs are 
available, the `gpu_memory_gb` can be set to 40 or 80, respectively, and the HP tool will recommend 
candidate configs that are more suitable to each setting. 
The `max_training_days` parameter shows how many days this model will be trained for, when 
training to full convergence. It will be written to the final config YAML files. This parameter can 
also be used when `model_size_in_b` is set to `null`. The 
`limit_search_runs` parameter can be used to limit the number of configs that will be searched 
during the HP search stage. We recommend selecting a value between 30 and 100 for this parameter. 
The tool will probably need to search at least 30 different configs to find the optimal one. However, 
if the compute is available in your cluster, we recommend increasing this parameter to a value close 
to 100. The `output_top_n` parameter can be used to configure how much detail the output summary file 
will include. By default, when set to 10, it will output the top 10 configurations. The 
`max_steps_per_run` parameter indicates how many steps to train each configuration for. The 
`max_minutes_per_run` parameter indicates how long to run each configuration for, in minutes. We 
recommend using at least 20 minutes per run for the smaller models, and increasing it to over 60 
minutes for the larger models. The training run will be stopped when either `max_steps_per_run` or 
`max_minutes_per_run` is reached. The `tflops_per_gpu` parameter provides an estimate of the TFLOPs 
each GPU can achieve when training LLMs with NeMo-Megatron. This value is only used to provide an 
estimate of how long the model will take to train for full convergence, so you can know the time to 
train before you even begin training your model. The `num_tokens_in_b` parameter indicates how many 
billions of tokens you will train your model for, when training to full convergence. It will be used 
when estimating how long it will take to train the model, to the desired number of tokens. The 
`vocab_size` parameter must show the vocabulary size that will be used during training. The `logs` 
parameter can be used to configure where the result logs will be saved. By default, this directory 
will be created inside the `base_results_dir` indicated in the `conf/config.yaml` file. The 
`override_search_num_nodes` parameter can be used to override the number of nodes that will be 
used for each training run in the HP grid search. By default, leaving this as `null` will run the tool 
with the smallest possible node count, to save compute. Finally, 
the `tensor_parallel_sizes`, `pipeline_parallel_sizes`, `micro_batch_sizes`, and `act_ckpt_layers` 
parameters can be used to override the heuristics that choose the grid search space for these 
four parameters. If these are left as `null`, our tool will select appropriate values. However, 
if you wish to override them, you can use these parameters. For example, if you only wish to search 
for configurations with Tensor Parallelism (TP) values of 1 and 2, you can set 
`tensor_parallel_sizes: [1, 2]` and leave the other parameters as `null`.  

###### 5.3.2.2.4. Inference HP Search
<a id="markdown-inference-hp-search" name="inference-hp-search"></a>

To run the inference HP search pipeline, the parameter `run_inference_hp_search` must be set to `True`
in the `conf/config.yaml` file. The model used to search the best inference HPs must be selected
using the `search_config` parameter in `conf/config.yaml`. For example, by default, this parameter
will be set to `gpt3/5b`, so our tool will search the optimal inference HPs for a 5B parameter GPT-3
model. The configuration for this model can be found in the `conf/search_config/gpt3/5b.yaml` file.
To configure the behavior of the HP search, the following parameters can be modified in the
correspoinding YAML file:

```yaml
inference_settings:
  vocab_size: 51200  # Vocabulary size
  start_id: 50256  # id of start token in vocabulary
  end_id: 50256  # id of end token in vocabulary
  input_seq_len: 60  # Length of the input sequence
  output_seq_len: 20  # Length of the output sequence
  max_latency_ms: 1200  # Maximum allowed latency
  top_n: 10  # Top N models to be output in the summary.
  logs: ${base_results_dir}/${search_config_value}  # Log directory
  tensor_parallel_sizes: [1, 2, 4, 8]
  pipeline_parallel_sizes: [1]
  max_batch_sizes: [8, 16, 32, 64, 128, 256]
```

The `vocab_size` parameter indicates the vocabulary size. The `start_id` and `end_id` parameters 
indicate the ids of the start and end tokens in the vocabulary, respectively. The `input_seq_len` 
and `output_seq_len` parameters show the length of the input and output sequences for the model, 
respectively. The `max_latency_ms` value can be used to only output models that meet that latency 
requirement, in milliseconds. The `top_n` parameter can be used to modify how many configs will be 
written to the output summary file. The `logs` parameter indicates where the logs will be stored.
Finally, the `tensor_parallel_sizes`, `pipeline_parallel_sizes`, and `max_batch_sizes` must be a 
list of values to generate the desired HP search. In this case, these values cannot be null, they 
must be provided by the user.


##### 5.3.2.3. Running Custom Model Size Configs
<a id="markdown-running-custom-model-size-configs" name="running-custom-model-size-configs"></a>

The HP Tool is capable of recommending a model size, based on your hardware and training time 
constraints. For instance, if you want to train a GPT-3 model, but don't know what model size is 
appropriate, you can input the number of nodes (and GPUs per node) available in your cluster, 
the amount of time you want to spend training the model, and the tool will recommend a model size 
that can be trained in that time with your hardware. To see an example of this, you can look at 
the `conf/search_config/gpt3/unknown_size.yaml` file. In this file, the `model_size_in_b` 
parameter is set to null. This is how you can tell the tool to recommend a model size to you. 
For the recommendation to work correctly, the `num_nodes`, `gpus_per_node`, and `max_training_days` 
parameters must indicate the number of nodes and GPUs per node available, and how long you wish to 
train the model for. Also, the tool needs to know the vocabulary size, number of tokens you will 
train the model for, and the estimated TFLOPS per GPU your hardware can achieve. These can be 
modified using the `vocab_size`, `num_tokens_in_b`, and `tflops_per_gpu` parameters, respectively. 
Once all these parameters are set correctly, and after selecting the `gpt3/unknown_size` as the 
config to run in the `search_config` parameter in the `conf/config.yaml` file, the training 
pipeline can be executed calling `python3 main.py`. This will produce a base configuration for 
the suggested model size. If `run_training_hp_search` or `run_inference_hp_search` are set to 
`True`, the tool will also search for the HPs for training or inference, using the rest of the 
configuration yaml file as input. The tool will behave the same way as when using a predefined 
config.

##### 5.3.2.4. Interpreting the Results
<a id="markdown-interpreting-the-results" name="interpreting-the-results"></a>

When the tool generates the base configuration for a model, it will be saved inside the directory 
specified in the `logs` parameter in your config files. By default, this will be 
`.../bignlp-hp-tool/results/<model_name>/<model_size>_<gpu_mem_size>/`. As the default 
`search_config` value is set to `gpt3/5b` and the default `gpu_memory_gb` is set to 80, the results 
can be found in the `.../bignlp-hp-tool/results/gpt3/5b_80gb/` directory. The base config will be 
available inside that directory, with the name `base_cfg_<model_size>.yaml`. 

If the training HP search pipeline is run, the results will be in three different directories inside 
your `logs` directory. The `candidate_configs` directory contains all the YAML files with all the 
configurations generated by the HP search. The `training_logs` directory contains all the logs of 
training each of the individual configs the tool generated. If `limit_search_runs` was set to 30, 
then there should be 30 different directories with the logs for each model. 

Finally, after all the training runs have finished and the final run has analyzed the throughput 
of each configuration, the final model recommendation will be stored in the `final_results` 
directory. This directory will contain a log file which lists the `output_top_n` fastest configs, 
sorted from fastest to slowest. The directory will also contain a csv file with all the results 
from every config that was run with the HP tool for a given model size. The results will be sorted 
from highest throughput to slowest throughput. The CSV file also includes information such as the 
samples per second achieved by each model, the time per global step, the TFLOPS per GPU achieved, 
and so on. The `final_results` directory will also contain a YAML file, which corresponds to the 
config with the lowest training time. This is the recommended model for training. 

For the inference HP search, the results can be found inside the directory specified in the 
`logs` parameter of the YAML config file. Inside that directory, you will find:
`.../inference/workspace/navigator_workspace/analyzer/results/metrics-model-inference.csv`. 
This csv file will have the results of every model that was profiled by the inference HP search 
tool. To see more details on how to interpret the inference results, review the Deployment 
Search Results section.

Notes: 
 - Since the HP search tool uses the minimum number of nodes necessary to save compute and time, 
the result might vary slightly when increasing the node count for these models. This value can be 
overriden using the `override_search_num_nodes` parameter, but increasing the node count will make 
the search slower and more costly.
 - If one of the optimal configs is very close to 100% GPU memory utilization, it is possible that 
the full training job will crash due to a memory spike. We recommend using a config that keeps the 
memory usage under 98% to avoid this issue. To save some memory, the recommendation is to try 
increasing the activation checkpointing layers by one each time. The performance will suffer 
slightly, but the memory footprint will be reduced.

##### 5.3.2.5. Logging Runs with Weights and Biases
<a id="markdown-logging-runs-with-weights-and-biases" name="logging-runs-with-weights-and-biases"></a>

Weights and Biases (W&B) can be used to log all the training search runs. To achieve this, the 
`wandb` parameters must be modified in the `conf/config.yaml` file. First, `enable` must be set to 
`True`. Then, the `api_key_file` must be set to point to the path where the file which contains 
the W&B API key. The API key must be in the first line of that file. Finally, the `project` parameter
must have the name of the W&B project where the metrics will be stored. The name of each run does not 
need to be provided. It will be automatically generated by the tool, using the model name, model size, 
and hyper-parameters used for each specific run.

```yaml
wandb:  # Weights and Biases (W&B) logging.
    enable: True 
    api_key_file: null
    project: bignlp-hp-tool
```

### 5.4. Training with Custom Configurations
<a id="markdown-training-with-custom-configurations" name="training-with-custom-configurations"></a>

The training config files can be modified, or other files can be created to be
used for training. They should follow the same structure and guidelines as the
existing model configurations.

#### 5.4.1 Example: Changing Embedding Type for T5 models
<a id="markdown-example-changing-embedding-time-for-t5-models" name="example-changing-embedding-time-for-t5-models"></a>

Here we show an example to change the embedding type for T5 models. Let's assume a case you want to
train a 220M T5 model. Instead of using default absolute learnable positional embeddings, you 
want to use relative positional embeddings.

First of all, you might want to check the training configuration file in `conf/training/(model_type)/(model_size).yaml`. 
In this case it will be `conf/training/t5/220m.yaml`. In the configuration file, you can find all the options we support.
You can find the parameters of your interests, in this case they will be
```yaml
position_embedding_type: 'learned_absolute' # Position embedding type. Options ['learned_absolute', 'relative']
relative_attention_num_buckets: 32 # Relative position number of buckets for computing the bias
relative_attention_max_distance: 128 # max_distance to keep relative distance in the attention_num_buckets.
```

For Slurm based systems, you can directly modify the configuration file in line. In this case, you can
change above three lines into
```yaml
position_embedding_type: 'relative' # Position embedding type. Options ['learned_absolute', 'relative']
relative_attention_num_buckets: 32 # Relative position number of buckets for computing the bias
relative_attention_max_distance: 128 # max_distance to keep relative distance in the attention_num_buckets.
```
and submit the training job.

For BCP, you can override the default configurations by adding argument 
`training.model.position_embedding_type='relative'` when submitting the training job. 

For more details of submitting training jobs on Slurm and BCP, please check [Section 5.6](#56-model-training). 

### 5.5. Bring Your Own Dataset
<a id="markdown-bring-your-own-dataset" name="bring-your-own-dataset"></a>
If you want to train the GPT-3, T5, or mT5 models on your own dataset (which is already
filtered and cleaned), you must first convert the dataset files to jsonl files.

As discussed in previous sections, the `data_preparation` parameter in `conf/config.yaml` 
specifies which file to use for data preparation
configuration purposes. The `data_preparation` parameter needs to be specified as `custom_dataset` for
bringing your own dataset and `run_data_preparation` must be set to `True` to run it. 
The `custom_dataset` config file can be found in `conf/data_preparation/custom_dataset.yaml`.
With our scripts, you can train your own tokenizer and preprocess your own dataset into a format
that can be consumed by our training scripts. 

Custom dataset only supports SentencePiece tokenizers at the moment. You can either train 
a fresh SentencePiece tokenizer with our scripts or load existing ones.

The data preparation can be parallelized by using multiple nodes (by default 20 nodes) to preprocess 
all custom dataset files in parallel.

###### 5.5.1. Slurm
<a id="markdown-451-slurm" name="451-slurm"></a>

First, ensure the cluster related configuration in the `conf/cluster/bcm.yaml` file is correct.
The `cluster` and `cluster_type` parameters in `conf/config.yaml` must be set to bcm.
Then, modify the `time_limit` or any other parameter related to the job in the `custom_dataset.yaml`
file.
The data preparation can be parallelized by using `nodes * workers_per_node` number of workers (up to one workder for each dataset file).

Example:

To run only the data preparation pipeline and not the training, evaluation or
inference pipelines, set the `conf/config.yaml` file to:
```yaml
run_data_preparation: True
run_training: False
run_conversion: False
run_finetuning: False
run_evaluation: False
```

And then run:
```
python3 main.py
```

###### 5.5.2. Base Command Platform
<a id="markdown-452-base-command-platform" name="452-base-command-platform"></a>

In order to run the data preparation script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. 
By default, the data preparation script will put the preprocessed data into the `bignlp-scripts/data/` directory.
We recommend that the `data_dir` parameter is set to a workspace, so that the data 
is visible across multiple jobs later on. The tokenizer model files should also be 
stored to the same workspace as the dataset, for later usage. The data preparation code 
must be launched in a multi-node job. It can be parallelized to use up to number of
nodes which is equal to the number of custom dataset files for faster preparation of the dataset.

To run the data preparation pipeline, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py run_data_preparation=True run_training=False run_conversion=False run_finetuning=False    \
run_evaluation=False cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data \
base_results_dir=/mount/results data_preparation=custom_dataset \
dataprepartion.train_tokenizer_args.inp=/path/to/text/file/for/training/tokenizer \
datapreparation.raw_dataset_files=[/path/to/custom_data_files] \
>> /results/data_custom_dataset_log.txt 2>&1
```

The command above assumes you mounted the data 
workspace in `/mount/data`, and the results workspace in `/mount/results`. Stdout and stderr are redirected to the `/results/data_gpt3_log.txt` file, so it can be downloaded from NGC. 
Any other parameter can also be added to the command to modify its behavior.

###### 5.5.3. Common
<a id="markdown-453-common" name="453-common"></a>

Set the configuration for the custom data preparation job in the YAML file:
```yaml
  dataset: custom_dataset
  custom_dataset_dir: ${data_dir}/custom_dataset
  train_tokenizer: True # True to train a sentence piece tokenizer
  train_tokenizer_args: # For all options please check: https://github.com/google/sentencepiece/blob/master/doc/options.md
     input: /path/to/text/file # text file for training tokenizer
     input_format: "text" # text or tsv
     model_prefix: "custom_sp_tokenizer"
     model_type: "bpe" # model algorithm: unigram, bpe, word or char
     vocab_size: 8000 # Vocabulary size
     character_coverage: 0.9995 # character coverage to determine the minimum symbols
     unk_id: 1
     bos_id: 2
     eos_id: 3
     pad_id: 0
  bpe_save_dir: ${.custom_dataset_dir}/bpe # Dir to save sentence piece tokenizer model and vocab files
  preprocess_data: True  # True to preprocess the data from json, jsonl or json.gz files, False otherwise.
  raw_dataset_files:
    - /path/to/dataset/files # Each file should be input json, jsonl or json.gz file
  tokenizer_model: ${.bpe_save_dir}/${data_preparation.train_tokenizer_args.model_prefix}.model # trained SentencePiece tokenizer model
  preprocess_worker_mapping: ${.custom_dataset_dir}/preprocess_mapping
  preprocessed_dir: ${.custom_dataset_dir}/preprocessed
  log_dir: ${base_results_dir}/data_preparation/custom_dataset_logs  # Where to save the logs
  nodes: 20
  cpus_per_node: 256 # 256 cpus for A100(80G)
  time_limit: "24:00:00"
  workers_per_node: 1 # Number of workers per node in preprocessing step.
```


### 5.6. Model Training
<a id="markdown-model-training" name="model-training"></a>
We provide an easy-to-use yet powerful pipeline to perform distributed training
of both GPT-3, T5 and mT5 models across multiple nodes and GPUs. We also provide
well-established recipes for different sizes models, where the
throughput has been maximized, and the convergence properties of the
models have been tested and confirmed.

#### 5.6.1. GPT-3 Training
<a id="markdown-gpt-3-training" name="gpt-3-training"></a>
The configuration used for the training pipeline must be specified in the
`conf/config.yaml` file, specifying the training parameter, specifying which file
to use for training purposes. The `run_training` parameter must be set to `True` to
run the training pipeline. The default value is set to `gpt3/5b`, which can be found
in `conf/training/gpt3/5b.yaml`. The parameters can be modified to adjust the
hyperparameters of the training runs. All supported model types and sizes can be found
in `conf/training` folder.

##### 5.6.1.1. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for your Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"

```

And set the training job specific parameters in the `conf/training/(model_type)/(model_size).yaml` file, 
using the run section:
```yaml
run:
    name: gpt3_126m
    results_dir: ${base_results_dir}/${.name}
    time_limit: "1-12:00:00"
    dependency: "singleton"
```

To run only the training pipeline and not the data preparation, evaluation or
inference pipelines, set the `conf/config.yaml` file to:
```yaml
run_data_preparation: False
run_training: True
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: False
```
And then run:
```
python3 main.py
```

##### 5.6.1.2. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>

Select the cluster related configuration following the NGC documentation. 
Then, use the `python3 main.py` command to launch the job and override the 
desired parameters from the training job parameters.


#### 5.6.2. T5 Training
<a id="markdown-t5-training" name="t5-training"></a>
The configuration used for the training pipeline must be specified in the
`conf/config.yaml` file, specifying the training parameter, specifying which file
to use for training purposes. The `run_training` parameter must be set to `True` to
run the training pipeline. The `training` parameter needs to be set to `t5/(model_size)`
for T5 models. For example, one can use `t5/220m` which can be found
in `conf/training/t5/220m.yaml`. The parameters can be modified to adjust the
hyperparameters of the training runs. All supported model types and sizes can be found
in `conf/training` folder.

##### 5.6.2.1. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for your Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

And set the training job specific parameters in the `conf/training/(model_type)/(model_size).yaml` file, 
using the run section:
```yaml
run:
    name: t5_220m
    results_dir: ${base_results_dir}/${.name}
    time_limit: "7-00:00:00"
    dependency: "singleton"
```

To run only the training pipeline and not the data preparation, evaluation or
inference pipelines, set the `conf/config.yaml` file to:
```yaml
run_data_preparation: False
run_training: True
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: False
```
And then run:
```
python3 main.py
```

##### 5.6.2.2. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>

Select the cluster related configuration following the NGC documentation. 
Then, use the python3 main.py command to launch the job and override the 
desired parameters from the training job parameters.



#### 5.6.3. mT5 Training
<a id="markdown-mt5-training" name="mt5-training"></a>
The configuration used for the training pipeline must be specified in the
`conf/config.yaml` file, specifying the training parameter, specifying which file
to use for training purposes. The `run_training` parameter must be set to `True` to
run the training pipeline. The `training` parameter needs to be set to `t5/(model_size)`
for T5 models. For example, one can use `mt5/390m` which can be found
in `conf/training/mt5/390m.yaml`. The parameters can be modified to adjust the
hyperparameters of the training runs. All supported model types and sizes can be found
in `conf/training` folder.

##### 5.6.3.1. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for your Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

And set the training job specific parameters in the `conf/training/(model_type)/(model_size).yaml` file, 
using the run section:
```yaml
run:
    name: mt5_390m
    results_dir: ${base_results_dir}/${.name}
    time_limit: "7-00:00:00"
    dependency: "singleton"
```

To run only the training pipeline and not the data preparation, evaluation or
inference pipelines, set the `conf/config.yaml` file to:
```yaml
run_data_preparation: False
run_training: True
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: False
```
And then run:
```
python3 main.py
```

##### 5.6.3.2. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>

Select the cluster related configuration following the NGC documentation. 
Then, use the python3 main.py command to launch the job and override the 
desired parameters from the training job parameters.


### 5.7. Resuming Training with Different Number of Nodes
<a id="markdown-resuming-training-with-different-number-of-nodes" name="resuming-training-with-different-number-of-nodes"></a>

To be able to resume a training run with a different number of nodes, we recommend to keep
the global batch size unchanged. This ensures that each training step will be
almost identical, regardless of the number of nodes. The number of nodes selected must be 
compatible with the rest of the parameters: GBS must be a multiple of 
(MBS * num_gpus) / (tensor_parallelism * pipeline parallelism)

where MBS is the micro batch size. For instance, the default GBS for the 5B GPT-3
model is 1440; the MBS is 2; the number of GPUs is 20\*8 = 160; 
the `tensor_parallelism` value is set to 2; and the `pipeline_parallelism` value is set to 1.
Therefore, the GBS is set to a valid value:
```
1440 % (2 * 160) / (2 * 1) == 0
```


### 5.8. Checkpoint Conversion
<a id="markdown-checkpoint-conversion" name="checkpoint-conversion"></a>

We provide a simple tool to convert the checkpoints from `.ckpt` format to `.nemo` format, 
which will later be used for evaluation (in T5 models) and inference purposes. 

#### 5.8.1. GPT-3 Conversion
<a id="markdown-gpt-3-conversion" name="gpt-3-conversion"></a>

The configuration used for the checkpoint conversion needs to be specified in the 
`conf/config.yaml` file, specifying the conversion parameter, which specifies the file 
to use for conversion purposes. The default value is set to `convert_gpt3`, which can be found 
in `conf/conversion/convert_gpt3.yaml` for GPT-3 models. 

The run_conversion parameter must be set to `True` to run the conversion pipeline.

##### 5.8.1.1. Common
<a id="markdown-common" name="common"></a>
To specify the input checkpoint to be used for conversion for GPT-3 models, use the `model` parameters
in `conf/conversion/convert_gpt3.yaml`:
```yaml
model:
    model_type: gpt # gpt or t5
    checkpoint_folder: ${conversion.run.train_dir}/checkpoints
    checkpoint_name: latest # latest OR name pattern of a checkpoint (e.g. megatron_gpt-*last.ckpt)
    hparams_file: ${conversion.run.train_dir}/hparams.yaml
    tensor_model_parallel_size: 2 # 1 for 126m, 2 for 5b, and 8 for 20b or larger models
    pipeline_model_parallel_size: 1 
    model_parallel_size: ${multiply:${.tensor_model_parallel_size}, ${.pipeline_model_parallel_size}}
    vocab_file: ${data_dir}/bpe/vocab.json
    merge_file: ${data_dir}/bpe/merges.txt
```

To specify the output location and file name of the converted `.nemo` file for GPT-3 models, use the `run` parameters
in `conf/conversion/convert_gpt3.yaml`:
```yaml
run:
    job_name: convert_${conversion.run.model_train_name}
    nodes: ${divide_ceil:${conversion.model.model_parallel_size}, 8} # 8 gpus per node
    time_limit: "2:00:00"
    ntasks_per_node: ${divide_ceil:${conversion.model.model_parallel_size}, ${.nodes}}
    convert_name: convert_nemo
    model_train_name: gpt3_5b
    train_dir: ${base_results_dir}/${.model_train_name}
    results_dir: ${.train_dir}/${.convert_name}
    output_path: ${.train_dir}/${.convert_name}
    nemo_file_name: megatron_gpt.nemo # name of nemo checkpoint; must be .nemo file
```

##### 5.8.1.2. Slurm
<a id="markdown-slurm" name="slurm"></a>
Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the conversion pipeline and not the data preparation, training, 
evaluation or inference pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: True
run_finetuning: False
run_prompt_learning: False
run_evaluation: False
```

then run:
```
python3 main.py
```

##### 5.8.1.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the conversion script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The conversion script must be launched in a multi-node job.

To run the conversion pipeline to convert a 126M checkpoint stored in 
`/mount/results/gpt3_126m/checkpoints`, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py run_data_preparation=False run_training=False run_conversion=True run_finetuning=False    \
run_evaluation=False cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data/the_pile_gpt3 \
base_results_dir=/mount/results conversion.run.model_train_name=gpt3_126m conversion.model.vocab_file=/mount/data/bpe/vocab.json \
conversion.model.merge_file=/mount/data/bpe/merges.txt conversion.run.results_dir=/mount/results/gpt3_126m/convert_nemo \
conversion.model.checkpoint_folder=/mount/results/gpt3_126m/checkpoints conversion.model.tensor_model_parallel_size=1 \
>> /results/convert_gpt3_log.txt 2>&1
```
The command above assumes you mounted the data workspace in `/mount/data`, and the results workspace in `/mount/results`. 
The stdout and stderr outputs will also be redirected to the `/results/convert_gpt3_log.txt` file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.

#### 5.8.2. T5 Conversion
<a id="markdown-t5-conversion" name="t5-conversion"></a>

The configuration used for the checkpoint conversion needs to be specified in the 
`conf/config.yaml` file, specifying the conversion parameter, which specifies the file 
to use for conversion purposes. 
The conversion parameter needs to be set to `convert_t5` for T5 models, which can be found 
in `conf/conversion/convert_t5.yaml`.

The `run_conversion` parameter must be set to `True` to run the conversion pipeline.

##### 5.8.2.1. Common
<a id="markdown-common" name="common"></a>
To specify the input checkpoint to be used for conversion for T5 models, use the `model` parameters
in `conf/conversion/convert_t5.yaml`:
```yaml
model:
    model_type: t5 # gpt or t5
    checkpoint_folder: ${conversion.run.train_dir}/checkpoints
    checkpoint_name: latest # latest OR name pattern of a checkpoint (e.g. megatron_gpt-*last.ckpt)
    hparams_file: ${conversion.run.train_dir}/hparams.yaml
    tensor_model_parallel_size: 1 # 1 for 220m, 2 for 3b
    pipeline_model_parallel_size: 1 
    model_parallel_size: ${multiply:${.tensor_model_parallel_size}, ${.pipeline_model_parallel_size}}
    vocab_file: ${data_dir}/bpe/vocab.txt
    merge_file: null
```

To specify the output location and file name of the converted `.nemo` file for T5 models, use the `run` parameters
in `conf/conversion/convert_t5.yaml`:
```yaml
run:
    job_name: convert_${conversion.run.model_train_name}
    nodes: ${divide_ceil:${conversion.model.model_parallel_size}, 8} # 8 gpus per node
    time_limit: "2:00:00"
    ntasks_per_node: ${divide_ceil:${conversion.model.model_parallel_size}, ${.nodes}}
    convert_name: convert_nemo
    model_train_name: t5_220m
    train_dir: ${base_results_dir}/${.model_train_name}
    results_dir: ${.train_dir}/${.convert_name}
    output_path: ${.train_dir}/${.convert_name}
    nemo_file_name: megatron_t5.nemo # name of nemo checkpoint; must be .nemo file
```

##### 5.8.2.2. Slurm
<a id="markdown-slurm" name="slurm"></a>
Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the conversion pipeline and not the data preparation, training, 
evaluation or inference pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: True
run_finetuning: False
run_prompt_learning: False
run_evaluation: False
```

then run:
```
python3 main.py
```

##### 5.8.2.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the conversion script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The conversion script must be launched in a multi-node job.

To run the conversion pipeline to convert a T5 220M checkpoint stored in 
`/mount/results/t5_220m/checkpoints`, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py conversion=convert_t5 \
run_data_preparation=False run_training=False run_conversion=True run_finetuning=False    \
run_evaluation=False cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data/the_pile_t5 \
base_results_dir=/mount/results conversion.model.vocab_file=/mount/data/bpe/vocab.txt \
conversion.run.model_train_name=t5_220m conversion.run.results_dir=/mount/results/t5_220m/convert_nemo \
conversion.model.checkpoint_folder=/mount/results/t5_220m/checkpoints \
conversion.model.tensor_model_parallel_size=1 conversion.model.pipeline_model_parallel_size=1 \
>> /results/convert_t5_log.txt 2>&1
```
The command above assumes you mounted the data workspace in `/mount/data`, and the results workspace in `/mount/results`. 
The stdout and stderr outputs will also be redirected to the `/results/convert_t5_log.txt` file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.

#### 5.8.3. mT5 Conversion
<a id="markdown-mt5-conversion" name="mt5-conversion"></a>

The configuration used for the checkpoint conversion needs to be specified in the 
`conf/config.yaml` file, specifying the conversion parameter, which specifies the file 
to use for conversion purposes. 
The conversion parameter needs to be set to `convert_mt5` for mT5 models, which can be found 
in `conf/conversion/convert_mt5.yaml`.

The `run_conversion` parameter must be set to `True` to run the conversion pipeline.

##### 5.8.3.1. Common
<a id="markdown-common" name="common"></a>
To specify the input checkpoint to be used for conversion for mT5 models, use the `model` parameters
in `conf/conversion/convert_mt5.yaml`:
```yaml
model:
  model_type: t5 # gpt or t5, use t5 for mt5 as well
  checkpoint_folder: ${conversion.run.train_dir}/checkpoints
  checkpoint_name: latest # latest OR name pattern of a checkpoint (e.g. megatron_gpt-*last.ckpt)
  hparams_file: ${conversion.run.train_dir}/hparams.yaml
  tensor_model_parallel_size: 1 
  pipeline_model_parallel_size: 1
  model_parallel_size: ${multiply:${.tensor_model_parallel_size}, ${.pipeline_model_parallel_size}}
  vocab_file: null
  merge_file: null
  tokenizer_model: ${data_dir}/mc4/bpe/mt5_tokenizer.model
```

To specify the output location and file name of the converted `.nemo` file for mT5 models, use the `run` parameters
in `conf/conversion/convert_mt5.yaml`:
```yaml
run:
  job_name: convert_${conversion.run.model_train_name}
  nodes: ${divide_ceil:${conversion.model.model_parallel_size}, 8} # 8 gpus per node
  time_limit: "2:00:00"
  ntasks_per_node: ${divide_ceil:${conversion.model.model_parallel_size}, ${.nodes}}
  convert_name: convert_nemo
  model_train_name: mt5_390m
  train_dir: ${base_results_dir}/${.model_train_name}
  results_dir: ${.train_dir}/${.convert_name}
  output_path: ${.train_dir}/${.convert_name}
  nemo_file_name: megatron_mt5.nemo # name of nemo checkpoint; must be .nemo file
```

##### 5.8.3.2. Slurm
<a id="markdown-slurm" name="slurm"></a>
Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the conversion pipeline and not the data preparation, training, 
evaluation or inference pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: True
run_finetuning: False
run_prompt_learning: False
run_evaluation: False
```

then run:
```
python3 main.py
```

##### 5.8.3.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the conversion script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The conversion script must be launched in a multi-node job.

To run the conversion pipeline to convert a mT5 390M checkpoint stored in 
`/mount/results/mt5_390m/checkpoints`, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py conversion=convert_mt5 \
run_data_preparation=False run_training=False run_conversion=True run_finetuning=False    \
run_evaluation=False cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data \
conversion.run.model_train_name=mt5_390m \
base_results_dir=/mount/results conversion.run.results_dir=/mount/results/mt5_390m/convert_nemo \
conversion.model.checkpoint_folder=/mount/results/mt5_390m/checkpoints \
conversion.model.tensor_model_parallel_size=1 conversion.model.pipeline_model_parallel_size=1 \
>> /results/convert_mt5_log.txt 2>&1
```
The command above assumes you mounted the data workspace in `/mount/data`, and the results workspace in `/mount/results`. 
The stdout and stderr outputs will also be redirected to the `/results/convert_mt5_log.txt` file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.

### 5.9. Model Finetuning
<a id="markdown-model-finetuning" name="model-finetuning"></a>

We also provide an easy-to-use tool to help fine-tuning the trained checkpoints
on GLUE tasks for T5 models and on XNLI for mT5 models. Fine-tuning for GPT-3 models are not supported.

#### 5.9.1. T5 Finetuning
<a id="markdown-t5-finetuning" name="t5-finetuning"></a>

The following downstream GLUE tasks are supported for T5 models: 
`cola`, `sst-2`, `mrpc`, `qqp`, `mnli`, `qnli`, and `rte`.

The configuration used for the fine-tuning needs to be specified in the
`conf/config.yaml` file, specifying the `finetuning` parameter, which specifies the
file to use for fine-tuning purposes. The `run_finetuning` parameter must be set
to `True` to run the fine-tuning pipeline. To fine-tune checkpoint on `mnli` task, set
`finetuning` parameter to `t5/mnli`, which can be found in `conf/finetuning/t5/mnli.yaml`. The
parameters can be modified to adapt different GLUE tasks and checkpoints
in fine-tuning runs. One will need to tune the fine-tuning hyper parameters
to reach the best accuracy for a specific GLUE task. The provided hyper parameters
are only optimized for T5 220M model on `mnli` task.

##### 5.9.1.1. Common
<a id="markdown-common" name="common"></a>
To specify the configuration for what tasks to run for finetuning, 
use the `run.task_name` parameter. 
And use all the `run` parameters to define the job specific config:
```yaml
run:
    name: ${.task_name}_${.model_train_name}
    time_limit: "04:00:00"
    dependency: "singleton"
    convert_name: convert_nemo
    model_train_name: t5_220m
    task_name: "mnli" # Supported task names: "cola", "sst-2", "mrpc", "qqp", "mnli", "qnli", "rte"
    results_dir: ${base_results_dir}/${.model_train_name}/${.task_name}
```

To specify which model checkpoint to load and its definition, use the `model` parameter:

```yaml
model: # For different fine-tuning tasks, tuning the hyper parameters accordingly; below is only for MNLI
    restore_from_path: ${base_results_dir}/${finetuning.run.model_train_name}/${finetuning.run.convert_name}/megatron_t5.nemo # Path to a trained T5 .nemo file
    tensor_model_parallel_size: 1
    pipeline_model_parallel_size: 1
```

##### 5.9.1.2. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the evaluation pipeline and not the data preparation, training, 
conversion or inference pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: False
run_finetuning: True
run_prompt_learning: False
run_evaluation: False
```

then run:
```
python3 main.py
```

##### 5.9.1.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the fine-tuning script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The evaluation script must be launched in a multi-node job.

To run the fine-tuning pipeline to fine-tune a 220M T5 model converted checkpoint stored in 
/mount/results/t5_220m/convert_nemo, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py finetuning=t5/mnli run_data_preparation=False run_training=False \
run_conversion=False run_finetuning=True run_evaluation=False cluster_type=bcp \
bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data base_results_dir=/mount/results \
finetuning.run.model_train_name=t5_220m \
finetuning.model.restore_from_path=/mount/results/t5_220m/convert_nemo/megatron_t5.nemo \
>> /results/finetune_t5_log.txt 2>&1
```

The command above assumes you mounted the data workspace in /mount/data, and the results workspace in /mount/results. 
The stdout and stderr outputs will also be redirected to the /results/finetune_t5_log.txt file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.



#### 5.9.2. mT5 Finetuning
<a id="markdown-mt5-finetuning" name="mt5-finetuning"></a>

XNLI benchmark are supported for mT5 models.

The configuration used for the fine-tuning needs to be specified in the
`conf/config.yaml` file, specifying the `finetuning` parameter, which specifies the
file to use for fine-tuning purposes. The `run_finetuning` parameter must be set
to `True` to run the fine-tuning pipeline. To fine-tune checkpoint on `xnli` task, set
`finetuning` parameter to `mt5/xnli`, which can be found in `conf/finetuning/mt5/xnli.yaml`.

##### 5.9.2.1. Common
<a id="markdown-common" name="common"></a>
To specify the configuration for what tasks to run for finetuning, 
use the `run.task_name` parameter. 
And use all the `run` parameters to define the job specific config:
```yaml
run:
  name: ${.task_name}_${.model_train_name}
  time_limit: "04:00:00"
  dependency: "singleton"
  convert_name: convert_nemo
  model_train_name: mt5_220m
  task_name: "xnli"
  results_dir: ${base_results_dir}/${.model_train_name}/${.task_name}
```

To specify which model checkpoint to load and its definition, use the `model` parameter:

```yaml
model:
  restore_from_path: ${base_results_dir}/${finetuning.run.model_train_name}/${finetuning.run.convert_name}/megatron_mt5.nemo # Path to a trained mt5 .nemo file
  tensor_model_parallel_size: 1
  pipeline_model_parallel_size: 1
```

##### 5.9.2.2. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the evaluation pipeline and not the data preparation, training, 
conversion or inference pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: False
run_finetuning: True
run_prompt_learning: False
run_evaluation: False
```

then run:
```
python3 main.py
```

##### 5.9.2.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the fine-tuning script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The evaluation script must be launched in a multi-node job.

To run the fine-tuning pipeline to fine-tune a 390M mT5 model converted checkpoint stored in 
/mount/results/mt5_390m/convert_nemo, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py  finetuning=mt5/xnli run_data_preparation=False run_training=False \
run_conversion=False run_finetuning=True run_evaluation=False cluster_type=bcp \
bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data base_results_dir=/mount/results \
finetuning.run.model_train_name=mt5_390m \
finetuning.model.restore_from_path=/mount/results/mt5_390m/convert_nemo/megatron_mt5_glue_xnli.nemo \
>> /results/finetune_mt5_log.txt 2>&1
```

The command above assumes you mounted the data workspace in /mount/data, and the results workspace in /mount/results. 
The stdout and stderr outputs will also be redirected to the /results/finetune_mt5_log.txt file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.

#### 5.9.3. Finetuning on Custom Tasks
<a id="markdown-finetuning-on-custom-tasks" name="finetuning-on-custom-tasks"></a>
We also support fine-tuning on custom down-stream tasks in T5 and mT5. In order to benchmark on your own
dataset, you are required to split the original dataset into two files, i.e. a txt file corresponding to the 
source (context) data, and txt file corresponding to the target data. Each line of these two files forms a 
fine-tuning sample.

Custom fine-tuning configuration files can be found in `conf/finetuning/t5/custom_task.yaml` for T5 models
and `conf/finetuning/mt5/custom_task.yaml` for mT5 models. The essential parameters are listed below. You need
to specify the dataset paths and preferred benchmark metrics.
```yaml
  data:
    train_ds:
      src_file_name: ??? # Path to the txt file corresponding to the source data.
      tgt_file_name: ??? # Path to the txt file corresponding to the target data.

    validation_ds:
      src_file_name: ??? # Path to the txt file corresponding to the source data.
      tgt_file_name: ??? # Path to the txt file corresponding to the target data.
      metric:
        name: "exact_string_match" # Name of the evaluation metric to use.
        average: null # Average the metric over the dataset. Options: ['macro', 'micro']. Works only for 'F1', 'accuracy' etc. Refer to torchmetrics for metrics where this is supported.
        num_classes: null
```
You can follow the instructions in T5 and mT5 fine-tuning sections to submit a custom task job.



### 5.10. Model Prompt Learning
<a id="markdown-model-prompt-learning" name="model-prompt-learning"></a>


Within NeMo Megatron we refer to **p-tuning** and **prompt tuning** methods collectively as prompt
learning. Both methods are parameter efficient alternatives to fine-tuning pretrained language
models. Our NeMo implementation makes it possible to use one pretrained GPT-3 model on many downstream
tasks without needing to tune the model's full set of parameters. It also allows for adding new tasks
to your model without overwriting or disrupting previous tasks for which the model has already been
p-tuned/prompt-tuned. Because the original model parameters are frozen and never altered by either
method, p-tuning/prompt-tuning also avoid cartographic forgetting issues often encountered when
fine-tuning models. 

Instead of selecting discrete text prompts in a manual or automated fashion, prompt tuning and p-tuning utilize virtual prompt embeddings that can be optimized via gradient decent. The only difference between prompt tuning and p-tuning within NeMo-Megatron is the architecture used to tune the soft prompt tokens during training.

- Our prompt tuning implementation is based off Lester et. al’s EMNLP 2021 paper "[The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/abs/2104.08691)"
- Our p-tuning implementation is based off Liu et al's paper "[GPT Understands, Too](https://arxiv.org/abs/2103.10385)"

For more details of our implementation, please check [Prompt Learning](https://github.com/NVIDIA/NeMo/blob/main/docs/source/nlp/prompt_learning.rst) in NeMo.

We support prompt learning on NeMo Megatron GPT-3 models.

#### 5.10.1. GPT-3 Prompt Learning
<a id="markdown-gpt-3-prompt-learning" name="gpt-3-prompt-learning"></a>

SQuAD v2.0 benchmark is supported for prompt learning. With default prompt learning config file, 
our scripts will download and preprocess original SQuAD v2.0 dataset to prompt learning dataset format.
You can also bring your own task dataset as long as it has been processed into the prompt learning dataset 
format.

The configuration used for the prompt learning needs to be defined in the
`conf/config.yaml` file by modifying the `prompt_learning` parameter, which specifies the
file to use for prompt learning purposes. The `run_prompt_learning` parameter must be set
to `True` to run the prompt learning pipeline. To prompt learning on `squad` task, set
`prompt_learning` parameter to `gpt3/squad`, which can be found in `conf/prompt_learning/gpt3/squad.yaml`.

##### 5.10.1.1. Common
<a id="markdown-common" name="common"></a>
To specify the configuration for prompt learning, 
use all the `run` parameters to define the job specific config:
```yaml
run:
  name: ${.task_name}_${.model_train_name}
  time_limit: "04:00:00"
  dependency: "singleton"
  convert_name: convert_nemo
  model_train_name: gpt3_5b
  task_name: "squad"
  results_dir: ${base_results_dir}/${.model_train_name}/prompt_learning_${.task_name}
```

To specify which language model checkpoint to load and its definition, use the `model` parameter:

```yaml
model:
  language_model_path: ${base_results_dir}/${prompt_learning.run.model_train_name}/${prompt_learning.run.convert_name}/megatron_gpt.nemo # Restore lanugage model from pre-trained .nemo checkpoint
  tensor_model_parallel_size: 1
  pipeline_model_parallel_size: 1
```

##### 5.10.1.2. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: 1
gpus_per_node: null
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the prompt learning pipeline and not the data preparation, training, 
conversion or other pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: False
run_finetuning: False
run_prompt_learning: True
run_evaluation: False
```

then run:
```
python3 main.py
```

##### 5.10.1.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the prompt learning script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The evaluation script must be launched in a multi-node job.

To run the prompt learning pipeline to prompt-learn a 5B GPT-3 model converted checkpoint stored in 
`/mount/results/gpt3_5b/convert_nemo`, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py  prompt_learning=gpt3/squad run_data_preparation=False run_training=False \
run_conversion=False run_finetuning=False run_evaluation=False run_prompt_tuning=True cluster_type=bcp \
bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data base_results_dir=/mount/results \
prompt_learning.run.model_train_name=gpt3_5b \
prompt_learning.model.language_model_path=/mount/results/gpt3_5b/convert_nemo/megatron_gpt.nemo \
>> /results/prompt_learning_gpt3_log.txt 2>&1
```

The command above assumes you mounted the data workspace in `/mount/data`, and the results workspace in `/mount/results`. 
The stdout and stderr outputs will also be redirected to the `/results/prompt_learning_gpt3_log.txt` file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.


### 5.11. Model Evaluation
<a id="markdown-model-evaluation" name="model-evaluation"></a>

#### 5.11.1. GPT-3 Evaluation
<a id="markdown-gpt-3-evaluation" name="gpt-3-evaluation"></a>

We also provide a simple tool to help evaluate the trained checkpoints. You can
evaluate the capabilities of the GPT-3 model on the following ZeroShot
downstream evaluation tasks: `lambada`, `boolq`, `race`, `piqa`, `hellaswag`, `winogrande`,
`wikitext2`, and `wikitext103`.

The model evaluation must be performed using a training checkpoint (.ckpt format), not
a converted checkpoint (`.nemo` format).

The configuration used for the evaluation needs to be specified in the
`conf/config.yaml` file, specifying the `evaluation` parameter, which specifies the
file to use for evaluation purposes. The `run_evaluation` parameter must be set
to `True` to run the evaluation pipeline. The default value is set to
`gpt3/evaluate_all`, which can be found in `conf/evaluation/gpt3/evaluate_all.yaml`. The
parameters can be modified to adapt different evaluation tasks and checkpoints
in evaluation runs. For Base Command Platform, all these parameters should be overriden from the command line.

##### 5.11.1.1. Common
<a id="markdown-common" name="common"></a>
To specify the configuration for what tasks to run for evaluation, use the `run.tasks` parameter. 
And use all the `run` parameters to define the job specific config:
```yaml
run:
    name: ${.eval_name}_${.model_train_name}
    time_limit: "4:00:00"
    nodes: ${divide_ceil:${evaluation.model.model_parallel_size}, 8} # 8 gpus per node
    ntasks_per_node: ${divide_ceil:${evaluation.model.model_parallel_size}, ${.nodes}}
    eval_name: eval_all
    model_train_name: gpt3_5b
    train_dir: ${base_results_dir}/${.model_train_name}
    tasks: all_tasks    # supported: lambada, boolq, race, piqa, hellaswag, winogrande, wikitext2, wikitext103 OR all_tasks
    results_dir: ${base_results_dir}/${.model_train_name}/${.eval_name}
```

To specify which model checkpoint to load and its definition, use the `model` parameter:

```yaml
model:
    model_type: nemo-gpt3
    checkpoint_folder: ${evaluation.run.train_dir}/checkpoints
    checkpoint_name: latest # latest OR name pattern of a checkpoint (e.g. megatron_gpt-*last.ckpt)
    hparams_file: ${evaluation.run.train_dir}/hparams.yaml
    tensor_model_parallel_size: 2 #1 for 126m, 2 for 5b, 8 for 20b
    pipeline_model_parallel_size: 1
    model_parallel_size: ${multiply:${.tensor_model_parallel_size}, ${.pipeline_model_parallel_size}}
    precision: bf16 # must match training precision - 32, 16 or bf16
    eval_batch_size: 4
    vocab_file: ${data_dir}/bpe/vocab.json
    merge_file: ${data_dir}/bpe/merges.txt
```

##### 5.11.1.2. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the evaluation pipeline and not the data preparation, training, 
conversion or inference pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: True
```

then run:
```
python3 main.py
```

##### 5.11.1.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the evaluation script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The evaluation script must be launched in a multi-node job.

To run the evaluation pipeline to evaluate a 126M GPT-3 model checkpoint stored in 
`/mount/results/gpt3_126m/checkpoints`, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py run_data_preparation=False run_training=False run_conversion=False run_finetuning=False    \
run_evaluation=True cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data/the_pile_gpt3 \
base_results_dir=/mount/results evaluation.model.vocab_file=/mount/data/bpe/vocab.json \
evaluation.model.merge_file=/mount/data/bpe/merges.txt evaluation.run.results_dir=/mount/results/gpt3_126m/evaluation \
evaluation.model.checkpoint_folder=/mount/results/gpt3_126m/checkpoints evaluation.model.eval_batch_size=16 \
evaluation.model.tensor_model_parallel_size=1 \
>> /results/eval_gpt3_log.txt 2>&1
```

The command above assumes you mounted the data workspace in `/mount/data`, and the results workspace in `/mount/results`. 
The stdout and stderr outputs will also be redirected to the `/results/eval_gpt3_log.txt` file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.


#### 5.11.2. T5 Evaluation
<a id="markdown-t5-evaluation" name="gpt-3-evaluation"></a>


On top of fine-tuned checkpoint, you can run the evaluation scripts to
evaluate the capabilities of the finetuned T5 model on the following 
downstream evaluation tasks: `cola`, `sst-2`, `mrpc`, `qqp`, 
`mnli`, `qnli`, and `rte`. Usually the task of finetuning and evaluation
should be the same.

The model evaluation must be performed with a fine-tuned checkpoint in `.nemo` format.

The configuration used for the evaluation needs to be specified in the
`conf/config.yaml` file, specifying the `evaluation` parameter, which specifies the
file to use for evaluation purposes. The `run_evaluation` parameter must be set
to `True` to run the evaluation pipeline. The default value is set to
`t5/mnli_matched`, which can be found in `conf/evaluation/t5/mnli_matched.yaml`. The
parameters can be modified to adapt different evaluation tasks and checkpoints
in evaluation runs. For Base Command Platform, all these parameters should be overriden from the command line.


##### 5.11.2.1. Common
<a id="markdown-common" name="common"></a>
To specify the configuration for what tasks to run for evaluation, use the `run.task_name` parameter. 
And use all the `run` parameters to define the job specific config: 
```yaml
run:
    name: eval_${.task_name}_${.model_train_name}
    time_limit: "04:00:00"
    dependency: "singleton"
    model_train_name: t5_220m
    task_name: "mnli" # Supported task names: "cola", "sst-2", "mrpc", "qqp", "mnli", "qnli", "rte"
    finetuning_results_dir: ${base_results_dir}/${.model_train_name}/${.task_name}
    results_dir: ${base_results_dir}/${.model_train_name}/${.task_name}_eval
```

To specify which fine-tuned checkpoint to load and its definition, use the `model` parameter:

```yaml
model:
    restore_from_path: ${evaluation.run.finetuning_results_dir}/checkpoints/megatron_t5_glue.nemo # Path to a finetuned T5 .nemo file
    tensor_model_parallel_size: 1
    pipeline_model_parallel_size: 1
```

##### 5.11.2.2. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the evaluation pipeline and not the data preparation, training, 
conversion or inference pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: True
```

then run:
```
python3 main.py
```

##### 5.11.2.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the evaluation script on Base Command Platform for T5 models, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The evaluation script must be launched in a multi-node job.

To run the evaluation pipeline to evaluate a 220M T5 model which has been fine-tuned
on `mnli` task and checkpoint stored in `/mount/results/t5_220m/mnli/checkpoints`, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py evaluation=t5/mnli_matched \
run_data_preparation=False run_training=False run_conversion=False run_finetuning=False    \
run_evaluation=True cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data \
base_results_dir=/mount/results evaluation.run.model_train_name=t5_220m \
evaluation.model.restore_from_path=/mount/results/t5_220m/mnli/checkpoints/megatron_t5_glue.nemo \
>> /results/eval_t5_log.txt 2>&1
```

The command above assumes you mounted the data workspace in `/mount/data`, and the results workspace in `/mount/results`. 
The stdout and stderr outputs will also be redirected to the `/results/eval_t5_log.txt` file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.


#### 5.11.3. mT5 Evaluation
<a id="markdown-mt5-evaluation" name="mt5-evaluation"></a>


On top of fine-tuned checkpoint, you can run the evaluation scripts to
evaluate the capabilities of the finetuned mT5 model on the following 
downstream evaluation tasks: `xnli`. Usually the task of finetuning and evaluation
should be the same.

The model evaluation must be performed with a fine-tuned checkpoint in `.nemo` format.

The configuration used for the evaluation needs to be specified in the
`conf/config.yaml` file, specifying the `evaluation` parameter, which specifies the
file to use for evaluation purposes. The `run_evaluation` parameter must be set
to `True` to run the evaluation pipeline. The default value is set to
`mt5/xnli`, which can be found in `conf/evaluation/mt5/xnli.yaml`. The
parameters can be modified to adapt different evaluation tasks and checkpoints
in evaluation runs. For Base Command Platform, all these parameters should be overriden from the command line.


##### 5.11.3.1. Common
<a id="markdown-common" name="common"></a>
To specify the configuration for what tasks to run for evaluation, use the `run.task_name` parameter. 
And use all the `run` parameters to define the job specific config: 
```yaml
run:
    name: eval_${.task_name}_${.model_train_name}
    time_limit: "04:00:00"
    dependency: "singleton"
    model_train_name: mt5_390m
    task_name: "xnli"
    finetuning_results_dir: ${base_results_dir}/${.model_train_name}/${.task_name}
    results_dir: ${base_results_dir}/${.model_train_name}/${.task_name}_eval
```

To specify which fine-tuned checkpoint to load and its definition, use the `model` parameter:

```yaml
model:
    restore_from_path: ${evaluation.run.finetuning_results_dir}/checkpoints/megatron_mt5_glue_xnli.nemo # Path to a finetuned T5 .nemo file
    tensor_model_parallel_size: 1
    pipeline_model_parallel_size: 1
```

##### 5.11.3.2. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: null
gpus_per_node: 8
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the evaluation pipeline and not the data preparation, training, 
conversion or inference pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: True
```

then run:
```
python3 main.py
```

##### 5.11.3.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the evaluation script on Base Command Platform for mT5 models, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The evaluation script must be launched in a multi-node job.

To run the evaluation pipeline to evaluate a 390M mT5 model which has been fine-tuned
on `xnli` task and checkpoint stored in `/mount/results/mt5_390m/xnli/checkpoints`, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py evaluation=mt5/xnli \
run_data_preparation=False run_training=False run_conversion=False run_finetuning=False \
run_evaluation=True cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data \
base_results_dir=/mount/results evaluation.run.model_train_name=mt5_390m \
evaluation.model.restore_from_path=/mount/results/mt5_390m/mnli/checkpoints/megatron_mt5_glue_xnli.nemo \
>> /results/eval_mt5_log.txt 2>&1
```

The command above assumes you mounted the data workspace in `/mount/data`, and the results workspace in `/mount/results`. 
The stdout and stderr outputs will also be redirected to the `/results/eval_mt5_log.txt` file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.


#### 5.11.4. Prompt Learnt GPT-3 Evaluation
<a id="markdown-prompt-learnt-gpt-3-evaluation" name="prompt-learnt-gpt-3-evaluation"></a>

We also provide a simple tool to help evaluate the prompt learnt GPT-3 checkpoints. You can
evaluate the capabilities of the prompt learnt GPT-3 model on a customized prompt learning test dataset.
We provide an example to evaluate our checkpoint, which went through prompt learning on SQuAD v2.0,
on the SQuAD v2.0 test dataset created in prompt learning step.

The configuration used for the evaluation needs to be defined in the
`conf/config.yaml` file by modifying the `evaluation` parameter, which specifies the
file to use for evaluation purposes. The `run_evaluation` parameter must be set
to `True` to run the evaluation pipeline. The value should be set to
`prompt_gpt3/squad.yaml`, which can be found in `conf/evaluation/prompt_gpt3/squad.yaml`. The
parameters can be modified to adapt different evaluation tasks and checkpoints
in evaluation runs. For Base Command Platform, all these parameters should be overridden from the command line.

##### 5.11.4.1. Common
<a id="markdown-common" name="common"></a>
To specify the configuration, use all the `run` parameters to define the job specific config. (
`run.tasks` has to be set to `prompt` to run evaluation on prompt learning test tasks):
```yaml
run:
  name: ${.eval_name}_${.model_train_name}
  time_limit: "4:00:00"
  nodes: ${divide_ceil:${evaluation.model.model_parallel_size}, 8} # 8 gpus per node
  ntasks_per_node: ${divide_ceil:${evaluation.model.model_parallel_size}, ${.nodes}}
  eval_name: eval_prompt_squad
  model_train_name: gpt3_5b
  tasks: "prompt" # general prompt task
  prompt_learn_dir: ${base_results_dir}/${.model_train_name}/prompt_learning_squad # assume prompt learning was on squad task
  results_dir: ${base_results_dir}/${.model_train_name}/${.eval_name}
```

To specify which model checkpoint to load and which prompt learning test dataset to evaluate, 
use the `model` parameter:

```yaml
model:
  model_type: nemo-gpt3-prompt
  nemo_model: ${evaluation.run.prompt_learn_dir}/megatron_gpt_prompt.nemo
  tensor_model_parallel_size: 2 #1 for 126m, 2 for 5b, 8 for 20b
  pipeline_model_parallel_size: 1
  model_parallel_size: ${multiply:${.tensor_model_parallel_size}, ${.pipeline_model_parallel_size}}
  precision: bf16 # must match training precision - 32, 16 or bf16
  eval_batch_size: 4
  prompt_dataset_paths: ${data_dir}/prompt_data/squad-v2.0/squad_test.jsonl
  disable_special_tokens: False # Whether to disable virtual tokens in prompt model evaluation. This is equivalent to evaluate without prompt-/p-tuning.
```

##### 5.11.4.2. Slurm
<a id="markdown-slurm" name="slurm"></a>

Set configuration for a Slurm cluster in the `conf/cluster/bcm.yaml` file:

```yaml
partition: null
account: null
exclusive: True
gpus_per_task: 1
gpus_per_node: null
mem: 0
overcommit: False
job_name_prefix: "bignlp-"
```

**Example:**

To run only the evaluation pipeline and not the data preparation, training, 
conversion or inference pipelines set the `conf/config.yaml` file to:

```yaml
run_data_preparation: False
run_training: False
run_conversion: False
run_finetuning: False
run_prompt_learning: False
run_evaluation: True
```

then run:
```
python3 main.py
```

##### 5.11.4.3. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>
In order to run the evaluation script on Base Command Platform, set the
`cluster_type` parameter in `conf/config.yaml` to `bcp`. This can also be overriden
from the command line, using hydra. The evaluation script must be launched in a multi-node job.

To run the evaluation pipeline to evaluate a prompt learnt 5B GPT-3 model checkpoint stored in 
`/mount/results/gpt3_5b/checkpoints`, run:
```
python3 /opt/bignlp/bignlp-scripts/main.py run_data_preparation=False run_training=False run_conversion=False run_finetuning=False    \
run_evaluation=True cluster_type=bcp bignlp_path=/opt/bignlp/bignlp-scripts data_dir=/mount/data \
base_results_dir=/mount/results evaluation.run.results_dir=/mount/results/gpt3_5b/eval_prompt_squad \
evaluation.model.nemo_model=/mount/results/gpt3_5b/prompt_learning_squad/megatron_gpt_prompt.nemo \
evaluation.model.nemo_model=4 evaluation.model.tensor_model_parallel_size=2 \
>> /results/eval_prompt_gpt3_log.txt 2>&1
```

The command above assumes you mounted the data workspace in `/mount/data`, and the results workspace in `/mount/results`. 
The stdout and stderr outputs will also be redirected to the `/results/eval_prompt_gpt3_log.txt` file, to be able to download the logs from NGC.
Any other parameter can also be added to the command to modify its behavior.



## 6. Deploying the BigNLP Model

This section describes the deployment of the BigNLP model on the NVIDIA Triton
Inference Server with FasterTransformer Backend on both single and multiple
node environments.    NVIDIA Triton Inference Server supports many inference
scenarios, of which two most important are:
* Offline inference    scenario - with a goal to maximize throughput regardless
    of the latency, usually achieved with increasing batch size and using server
    static batching feature.
* Online inference scenario - with a goal to maximize throughput within a given
    latency budget, usually achieved with small batch sizes and increasing
    concurrency requests to the server, using dynamic batching feature.

[NVIDIA Triton Model Navigator](https://github.com/triton-inference-server/model_navigator)
helps with conversion and setting up a deployment environment to do inference
for models from BigNLP training scripts. Use scripts to convert models to a new
format, then use NVIDIA Triton Inference Server to process inference requests. 
Unfortunately, deployment scripts currently are not supported for T5 models.

NeMo Megatron supports the training of GPT-3 models with pipeline parallelism > 1. 
However, deployment scripts currently only support checkpoints with pipeline parallelism = 1.

The inference scripts execute at a Slurm or Base Command Platform cluster in several steps:
* Megatron/NeMo checkpoint conversion to FasterTransformer format.
* Preparation of model repository for NVIDIA Triton Inference Server.
* Profiling and selecting the best inference model and NVIDIA
    Triton Inference Server configuration.
* Accuracy verification.
* Profiling of deployed models.

The inference container is pulled from a Docker registry. You must ensure that
your cluster configuration allows access to your registry. NVIDIA provides the
container with all components necessary for inference at the
[NGC Docker registry](https://ngc.nvidia.com/catalog/containers).
Inference scripts use the [pyxis slurm plug-in](https://github.com/NVIDIA/pyxis)
to pull and run the container in a Slurm node.


The navigator script converts a checkpoint from a training format to the
[FasterTransformer](https://github.com/triton-inference-server/fastertransformer_backend)
format. The NVIDIA Triton Model Navigator looks for a trained
checkpoint in the workspace passed as an argument and creates a navigator
workspace with all output files, which can be used for production inference
deployment.

The NVIDIA Triton Model Navigator script generates many NVIDIA Triton model
repositories and manages them to conduct optimization of configuration
parameters. This optimizes GPU memory and makes inference a lot faster. NVIDIA
Triton Inference Server’s optimization tool Model Analyzer helps to find the
best configuration, taking into account constraints defined in the navigator’s
configuration. It is possible to set constraints for latency, number of GPUs
and [NVIDIA DGX A100](https://www.nvidia.com/en-us/data-center/dgx-a100/)
systems. All generated models are profiled to report latency and throughput.
Once the model is optimized, you can deploy it to your inference infrastructure
and use it in production.


### 6.1. Model Inference Deployment Process
<a id="markdown-model-inference-deployment-process" name="model-inference-deployment-process"></a>

<img src="img/inference_deployment_flow.png"/>

### 6.2. Prepare Environment
<a id="markdown-prepare-environment" name="prepare-environment"></a>

The whole solution uses a set of Docker containers executed at Slurm or Base Command Platform cluster.
The training container also includes conversion
scripts and NVIDIA Triton Model Navigator. The inference container is just the
NVIDIA Triton Inference Server with the FasterTransformer backend installed.
Install the BigNLP scripts dependencies on the:
    - Head node of your Slurm cluster.
    - Your workstation if running them on Base Command Platform cluster.

```
pip install -r requirements.txt
```

You can use `virtualenv` to prevent polluting your
head node environment for other Python projects. If your Slurm configuration
lacks pip, then you can use [get\_pip.py](https://github.com/pypa/get-pip)
with just `python3`.

You must set your configuration for a cluster in YAML file.

#### 6.2.1. Slurm
<a id="markdown-slurm" name="slurm"></a>

Sample Slurm cluster configuration file:

```yaml
cluster:                                # example config for enterprise cluster
    type: pyxis                     # type of job executor to be used
    sbatch_parameters:        # this overwrites sbatch parameters generated by submitit
        account: null             # slurm account
        partition: "batch"    # slurm partition
        exclude: null             # slurm nodes, which should be excluded from jobs
    srun_args: ["--mpi", "pmix"] # additional slurm arguments list
    enable_gpus_allocation: true
env:
  job_name_prefix: "bignlp-"
  training_container_image: nvcr.io/ea-bignlp/ea-participants-kt/bignlp-training:22.06.rc2-py3
  inference_container_image: nvcr.io/ea-bignlp/bignlp-inference:22.05-py3
```

The `cluster` section configures Slurm cluster parameters. The `srun_args`
should contain [--mpi](https://slurm.schedmd.com/mpi_guide.html) parameter
valid for your cluster. `enable_gpus_allocation` parameters controls
sbatch/srun `--gpus[-n]` parameters and should be disabled on cluster where
allocation of GPUs is not supported.

The `env` section sets development environment parameters:
 * `job_name_prefix`: Prefix which will be prepended to the name of each queued job.
 * `training_container_image`: NGC training container for BigNLP.
 * `inference_container_image`: NGC inference container for BigNLP.

#### 6.2.2. Base Command Platform
<a id="markdown-base-command-platform" name="base-command-platform"></a>

Sample Base Command Platform cluster configuration file:

```yaml
cluster:                                # example config for enterprise cluster
    type: base_command        # type of job executor to be used
    instance_with_gpu: dgxa100.40g.8.norm
    instance_without_gpu: dgxa100.40g.1.norm
env:
  job_name_prefix: "bignlp-"
  training_container_image: nvcr.io/ea-bignlp/ea-participants-kt/bignlp-training:22.06.rc2-py3
  inference_container_image: nvcr.io/ea-bignlp/bignlp-inference:22.05-py3
```

The `cluster` section set Base Command Platform parameters:
 * `instance_with_gpu`: Instance to be used when Job to be submitted will require GPUs
 * `instance_without_gpu`: Instance to be used when Job to be submitted will not require GPUs

The `env` section sets development environment parameters:
 * `job_name_prefix`: Prefix which will be prepended to the name of each queued job.
 * `training_container_image`: NGC training container for BigNLP.
 * `inference_container_image`: NGC inference container for BigNLP.

When using Base Command Platforms clusters [workspaces](https://docs.nvidia.com/base-command-platform/user-guide/index.html#managing-workspaces)
are used to share with Jobs executed on computation node
input data (checkpoints and datasets) and result files (Triton Model Repositories, result files, etc).
Sample structure of workspace:

```
/5b-pile-all-optimize-checkpoint    # directory with Megatron checkpoints
/5b.nemo                                                    # or Nemo checkpoint file
/lambada                                                    # dataset of accuracy testing
/infer_workspace-20211201_000000    # workspace with results which will be created on each execution of Inference Scripts
```

During the execution of Inference Scripts, the paths to input and output files
are placed inside the directory where the NGC workspace is mounted. The
exception is for Model Navigator and cluster config files - they are not needed
to be shared with the Job container or are copied on the workspace by scripts.
Also, the user needs to define the Inference Scripts workspace inside the NGC
workspace. Example Inference Script call:

```sh
        python3 ./bignlp/infer_scripts/prepare_model_repository.py \
        --cluster-config-path ./conf/inference/cluster_bcp.yaml \
        --navigator-config-path ./conf/inference/medium_mbs_128-pp_1-tp_8-io_60_20.yaml \
        --model-path /<path_to_mounted_workspace>/5b-pile-all-optimize-checkpoint/release \
        --model-name test_5b \
        --model-repository-path /<path_to_mounted_workspace>/test_5b \
        --dataset-dir /<path_to_mounted_workspace>/lambada \
        --accuracy-tests --performance-tests \
        --workspace-path /<path_to_mounted_workspace>/infer_workspace-$(date +%Y%m%d_%H%M%S) # name of the infer_workspace folder for this run
```

### 6.3. Provide Model and Inference Configuration
<a id="markdown-provide-model-and-inference-configurationn" name="provide-model-and-inference-configurationn"></a>

#### 6.3.1. Predefined Configuration for Selected Models
<a id="markdown-predefined-configuration-for-selected-models" name="predefined-configuration-for-selected-models"></a>

The repository contains the conf/inference folder with predefined NVIDIA Triton
Model Navigator configurations saved in YAML files. Those configurations are
prepared for 5B, 20B, 175B and 530B GPT3 models for two input/output
configurations 200/200 and 60/20. The configurations cover inference with
several GPUs in a single node. The files are present in the
`conf/inference/optimal_configurations` folder.

The configuration changes for different input sequence lengths and output
sequence lengths used in inference tasks. An application like chatbot can work
with an input of 60 tokens and an output of 20 tokens. Scenarios like text
translation require much longer lengths closer to 200 for input tokens and 200
for output tokens. The RAM usage for a bigger batch size with longer sequence
lengths increases significantly, so optimal configurations set different
maximum batch size values for different sequence lengths. The predefined
configuration files can be used with the `prepare_model_repository.py` script
described later. The files are marked with a number of parameters in model
architecture like 5B, which means 5 billion parameters.

Input sequence lengths 60 and output 20:
* **5B GPT3**: `5b_io_60_20.yaml`
* **20B GPT3**: `20b_io_60_20.yaml`
* **175B GPT3**: `175b_io_60_20.yaml`
* **530B GPT3**: `530b_io_60_20.yaml`

Input sequence lengths 200 and output 200:
* **5B GPT3**: `5b_io_200_200.yaml`
* **20B GPT3**: `20b_io_200_200.yaml`
* **175B GPT3**: `175b_io_200_200.yaml`
* **530B GPT3**: `530b_io_200_200.yaml`

The configuration folder also contains configuration for random
FasterTransformer checkpoints. It is possible to start FasterTransformer
inference without weight files because the engine just initializes them to
random values. This model cannot deliver any valid accuracy, but it is possible
to benchmark inference constraints like latency before the expensive training
of a large model is finished. The folder `conf/inference/model_specs` contains a
folder with predefined random model configuration, which cover range of example
GPT3 configurations, where each folder is marked with a number of model
parameters:
* **5B**: `5b.ft`
* **20B**: `20b.ft`
* **89B**: `89b.ft`
* **175B**: `175b.ft`
* **310B**: `310b.ft`
* **530B**: `530b.ft`


#### 6.3.2. Optimal Configuration Search
<a id="markdown-optimal-configuration-search" name="optimal-configuration-search"></a>

##### 6.3.2.1. Random Weights Checkpoint Benchmark
<a id="markdown-random-weights-checkpoint-benchmark" name="random-weights-checkpoint-benchmark"></a>

NVIDIA Triton Model Navigator can benchmark inference before training is
finished and verify inference constraints ahead of time; for example maximum
latency budget or number of GPUs, thus cost of inference. For performance
reasons, if you already know model size and parameters, you can use the
FasterTransformer NVIDIA Triton backend to generate a checkpoint with random
weights inside the NVIDIA Triton Inference Server.

The first step in the benchmark script generates a random checkpoint based on
your configuration. The second step configures model repositories. The third
step starts a set of NVIDIA Triton Inference Servers and executes the
performance measurements for each.

The inputs:
* Random model configuration - For example, `conf/inference/model_specs/5b.ft`
* Docker image with training and profiling scripts.
* Docker image with NVIDIA Triton and FasterTransformer backend.
* Performance profile configuration YAML file.

The outputs:
* Performance report.
* Performance results.
* Optimal configurations.
* NVIDIA Triton model stores with a placeholder for the trained model checkpoint.

You can benchmark a model using
`bignlp/infer_scripts/profile_model_with_random_weights.py` script:

```
python3 ./bignlp/infer_scripts/profile_model_with_random_weights.py \
        --cluster-config-path <Your cluster config>.yaml \
        --navigator-config-path ./conf/inference/profile_offline.yaml \
        --model-path conf/inference/model_specs/5b.ft \
        --model-name ft_5B \
        --tensor-parallel-sizes 1 8 \
        --pipeline-parallel-sizes 1 \
        --input-output-lengths 60,20 200,200 \
        --max-batch-sizes 128 \
        --max-latency-ms 4000 \
        --workspace-path /<path_to_mounted_workspace>/infer_workspace-$(date +%Y%m%d_%H%M%S)
```

The parameters:
* `cluster-config-path`: Cluster configuration YAML file.
* `navigator-config-path`: Navigator configuration YAML;
     for example,`./conf/inference/profile_offline.yaml`
* `model-path`: This model path contains a YAML file with
     random checkpoint configuration.
* `model-name`: Your model name for NVIDIA Triton repository.
* `tensor-parallel-sizes`: Tensor parallel factor (Number of GPUs per node); for example, `1 2 4 8`
* `pipeline-parallel-sizes`: Pipeline parallel factor (Number of nodes); for example, `1 2 3 4`
* `input-output-lengths`: Analyzed input and output lengths in format of
     `<input_len>,<output_len>[ <input_len>,<output_len> …]`;
     for example, `60,20 200,200`
* `max-batch-sizes`: Maximum batch sizes used for optimization;
     for example, `1 2 4 8 16 256`
* `max-latency-ms`: Maximum p99 latency valid for your scenario.
* `top-n-configs`: Number of optimal configurations to save.

The parameters `tensor-parallel-sizes`, `pipeline-parallel-sizes`,
`input-output-lengths`, and `max-batch-sizes` are used to generate combinations of
possible configurations for FasterTransformer and performance measurement
scripts. The profile script compares throughput normalized to 1 GPU of all
generated configurations and prints N-best configurations taking into account a
maximum latency constraint. If you request very small maximum latency, then the
script will not be able to find any valid configurations.

The repository contains two profile configurations for Model Navigator:
* `conf/inference/profile_offline.yaml` - Configuration for offline scenario
     focusing on changing batch sizes but not user request concurrency.
* `conf/inference/profile_online.yaml` - Configuration for online scenario
     focusing on changing user request concurrency.


The random model configuration for the model-path parameter is in YAML file:

```yaml
decoder_layers: 105    # Number of decoder layers
head_num: 128                # Number of heads in layer
size_per_head: 160     # Size per head
inter_size: 81920        # It can be: inter_size = size_per_head * head_num * 4
tensor_para_size: 8    # Default tensor parallel configuration (ignored)
vocab_size: 51200        # Vocabulary size based on vocabulary file
start_id: 50256            # id of start token in vocabulary
end_id: 50256                # id of end token in vocabulary
```

The output files are saved in the `current_folder/infer_workspace_<YYYYmmdd_HHMMSS>`.
The N best configurations are printed to the terminal.
The `infer_workspace_<YYYYmmdd_HHMMSS>` folder contains CSV file with all
measurements combined:

```
navigator_workspace/analyzer/results/metrics-model-inference.csv
```

The best configuration is selected based on the throughput normalized for one
GPU. It is possible to deploy the same model at a number of GPUs, so the cost
of model deployment is not constant for all configurations. The script
normalizes this cost by dividing throughput of a model instance by the number
of GPUs used for computation.

##### 6.3.2.2. Trained Checkpoint Benchmark
<a id="markdown-trained-checkpoint-benchmark" name="trained-checkpoint-benchmark"></a>

As an alternative to generating checkpoints randomly, you can use a trained
checkpoint to look for optimal configuration; however, for larger models that
might take a significant amount of time and might not be feasible.

The inputs:
* Megatron/NeMo trained checkpoint.
* Docker image with training and profiling scripts.
* Docker image with NVIDIA Triton and FasterTransformer backend.
* Performance profile configuration YAML file.

The outputs:
* Performance report.
* Performance results.
* Optimal configurations.
* NVIDIA Triton model stores with trained FasterTransformer model checkpoint.

Model repository preparation for the NVIDIA Triton Inference Server:

```sh
python3 ./bignlp/infer_scripts/profile_model.py \
        --cluster-config-path <Your cluster config>.yaml \
        --navigator-config-path ./conf/inference/profile_offline.yaml \
        --model-path <Your path to training checkpoint> \
        --model-name model_name \
        --tensor-parallel-sizes 1 \
        --pipeline-parallel-sizes 1 \
        --input-output-lengths 60,20 \
        --max-batch-sizes 1 \
        --max-latency-ms 4000 \
        --workspace-path /<path_to_mounted_workspace>/infer_workspace-$(date +%Y%m%d_%H%M%S)
```

The parameters:
* `cluster-config-path`: Cluster configuration YAML file.
* `navigator-config-path`: Navigator configuration YAML;
     for example,`./conf/inference/profile_offline.yaml`
* `model-path`: This model path contains a trained Megatron/NeMo checkpoint.
   A NeMo checkpoint must be passed as a file with `.nemo` extension,
   but a Megatron checkpoint must be passed as a folder.
* `model-name`: Your model name for NVIDIA Triton repository.
* `tensor-parallel-sizes`: Tensor parallel factor (Number of GPUs per node); for example, `1 2 4 8`
* `pipeline-parallel-sizes`: Pipeline parallel factor (Number of nodes); for example, `1 2 3 4`
* `input-output-lengths`: Analyzed input and output lengths in format of
     `<input_len>,<output_len>[ <input_len>,<output_len> …]`;
     for example, `60,20 200,200`
* `max-batch-sizes`: Maximum batch sizes used for optimization;
     for example, `1 2 4 8 16 256`
* `max-latency-ms`: Maximum p99 latency valid for your scenario.
* `top-n-configs`: Number of optimal configurations to save.

Megatron checkpoint must have embedded vocabulary in PyTorch checkpoint file
or vocabulary file stored in `<model-path>/vocab.json`. Vocabulary embedding can
be performed with `./bignlp/infer_scripts/embed_vocab_in_megatron_checkpoint.py` script.

The parameters `tensor-parallel-sizes`, `pipeline-parallel-sizes`,
`input-output-lengths`, and `max-batch-sizes` are used to generate combinations of
possible configurations for FasterTransformer and performance measurement
scripts. The profile script compares throughput normalized to 1 GPU of all
generated configurations and prints N-best configurations taking into account a
maximum latency constraint. If you request very small maximum latency, then the
script won’t be able to find any valid configurations.

### 6.4. Review Deployment Search Results
<a id="markdown-review-deployment-search-results" name="review-deployment-search-results"></a>

The `profile_model_with_random_weights.py` and
`profile_model.py` scripts create a folder
`infer_workspace_<YYYYmmdd_HHMMSS>` with a timestamp at the end.

It contains the following folders:
* `model_name-ft_gpu_counts_8-converted.ft`: Folders with converted
     FasterTransformer checkpoints.
* `logs`: Logs.
* `model_repo_model_name-io_60_20-half_1-pp_1-tp_8-mbs_256`:
     NVIDIA Triton model repository for input sequence length 60
     and output length 20 for pipeline parallel 2 and tensor parallel 8
     and maximum batch size 256.
*    `model_repo_model_name-io_60_20-half_1-pp_1-tp_8-mbs_256`:
     NVIDIA Triton model repository for input sequence length 60
     and output length 20 for pipeline parallel 1 and tensor parallel 8 and
     maximum batch size 256.
* `navigator_workspace`: Folder to NVIDIA Triton Model Navigator configurations.
* `cluster_workspace`: Folder with cluster logs and submission scripts.

Both profile scripts print a list of the best models with the name
of the NVIDIA Triton model repository with the best results and performance metrics.

Results from `profile_model.py` and `profile_model_with_random_weights.py`
scripts are saved for review under:
`./infer_workspace-<YYYYmmdd_HHMMSS>/navigator_workspace/analyzer/results/metrics-model-inference.csv`

The CSV file contains several columns:
* `Model` - NVIDIA Triton model name.
* `Batch` - Batch size.
* `Concurrency` - User request concurrency.
* `Model Config Path` - Path to model configuration.
* `Backend Parameters` - Measurement and backend parameters (PP - pipeline
    parallel, TP - tensor parallel, and half - FP16 used for some computations),
    `max_input` - maximum sequence input length, `max_sec` - maximum sequence input
    length plus maximum sequence output length.
* `Preferred Batch Sizes` - List of preferred batch sizes used in NVIDIA Triton configuration.
* `Satisfies Constraints` - “Yes” if a model satisfies the p99 latency constraint, set as the max-latency-ms parameter.
* `Throughput (inder/sec)` - Throughput not normalized for the number of GPUs but just measured for one model instance.
* `p95 Latency(ms)`.
* `p99 Latency(ms)`.

Best configurations are mentioned from the top,
To review configurations, check the directory with all generated configs:
`infer_workspace-<YYYYmmdd_HHMMSS>/navigator_workspace/top_configs`

NVIDIA Triton model repositories contain symbolic links to folders with weights.
You should copy final folder with model to expand links into files.

```
    cp -rL <NVIDIA Triton store from script> <destination>
```

### 6.5. Prepare NVIDIA Triton Model Repository and Run Accuracy/Performance Tests
<a
id="markdown-prepare-nvidia-triton-model-repository-and-run-accuracy%2Fperformance-tests"
name="prepare-nvidia-triton-model-repository-and-run-accuracy%2Fperformance-tests"></a>

Having the best config and trained checkpoint. A trained model checkpoint is
required as this is final model deployment and verification. For large models,
loading a checkpoint from storage can take a significant amount of time.

The inputs:
* Trained model checkpoint.
* Docker image with NVIDIA Triton and FasterTransformer backend.
* Lambada dataset.
* Model vocabulary.
* Model merges file.

The English data for accuracy experiments can be downloaded from open resources.

The Lambada dataset can be downloaded from GITHUB:

```
wget https://raw.githubusercontent.com/cybertronai/bflm/master/lambada_test.jsonl
```

The vocabulary and merge files can be downloaded from the Huggingface project:

```
wget https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-vocab.json
wget https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-merges.txt
```

It’s recommended that you put all files in one folder used for accuracy
verification of your model.

The outputs:
* NVIDIA Triton Model Repository with a converted model in FasterTransformer format.
* Accuracy measurement report.
* Performance measurement report.

The accuracy report is stored in the current directory in the file `lambada_metrics.csv`.
You can verify your model running in NVIDIA Triton by using the Lambada dataset:

```sh
python3 ./bignlp/infer_scripts/prepare_model_repository.py \
        --cluster-config-path <Your cluster config>.yaml \
        --navigator-config-path ./conf/inference/small_mbs_256-pp_1-tp_1-io_60_20.yaml \
        --model-path <Your path to training checkpoint> \
        --model-name model_name \
        --dataset-dir <Your lambada folder> \
        --model-repository-path <Your output path for NVIDIA Triton model repository> \
        --accuracy-tests \
        --performance-tests
```

Parameters:
* `cluster-config-path`: Cluster configuration YAML file.
* `navigator-config-path`: Navigator configuration to set up NVIDIA Triton.
* `model-path`: This model path contains a trained Megatron/NeMo checkpoint.
   A NeMo checkpoint must be passed as a file with `.nemo` extension,
   but a Megatron checkpoint must be passed as a folder.
* `model-name`: Model name.
* `dataset-dir`: Folder with downloaded lambada dataset, merges and vocabulary files.
* `model-repository-path`: Path to result NVIDIA Triton Model Repository.
* `accuracy-tests`: Run accuracy tests.
* `performance-tests`: Run performance offline and online tests.

Megatron checkpoint must have embedded vocabulary in PyTorch checkpoint file
or vocabulary file stored in `<model-path>/vocab.json`. Vocabulary embedding can
be performed with `./bignlp/infer_scripts/embed_vocab_in_megatron_checkpoint.py` script.

The parameter `navigator-config-path` contains the Navigator configuration to
convert a model, set up a NVIDIA Triton, and parameters to perform performance
tests. You must set some basic parameters to have a working model to verify
accuracy. You can use a predefined configuration for this task, which sets
basic values for a tiny model:

```
./conf/inference/small_mbs_256-pp_1-tp_1-io_60_20.yaml
```

You must check your model size and look for optimal configuration to run
accuracy for your model. The larger models must be run with many GPUs and nodes
to work. The predefined configurations for some GPT3 architectures and
inference tasks are described in the _Predefined configurations_ section above.

### 6.6. Run NVIDIA Triton Server with Selected Model Repository
<a id="markdown-run-nvidia-triton-server-with-selected-model-repository"
name="run-nvidia-triton-server-with-selected-model-repository"></a>

The inputs:
* NVIDIA Triton model repository with FasterTransformer checkpoint
     ready for inference at production.
* Docker image with NVIDIA Triton and FasterTransformer backend.

The outputs:
* Running NVIDIA Triton model instance serving model in cluster.

To run the NVIDIA Triton Model Navigator, do the following:
```sh
python3 ./bignlp/infer_scripts/run_tritonserver.py \
        --cluster-config-path <Your cluster config>.yaml \
        --model-repository-path <Your output path for NVIDIA Triton model repository>
```

The parameters:
* `cluster-config-path`: Cluster configuration YAML file.
* `model-repository-path`: NVIDIA Triton model repository path from folder
     generated by `prepare_model_repository.py` script.

The NVIDIA Triton model repository created in scripts above contains symbolic
links. You need to expand links for `run_tritonserver.py` to
be able to access files when they are mounted in job containers.

The script saves NVIDIA Triton logs so you can verify what happens when
FasterTransformer loads a checkpoint. The command above starts the server, so
that users can test it with other tools created later. You can use this
script to demo inference. The job does not stop on its own, if you don't stop it
manually, it will stop when the time limit is reached on the cluster.

FasterTransformer backend ignores missing files for weights and uses random
tensors in such a scenario. You should make sure that your NVIDIA Triton
instance is serving requests with real weights by inspecting logs.


If you notice warning about missing files, you should double check your model:

```
[WARNING] file /triton-model-repository/model_name/1/1-gpu/model.wpe.bin cannot be opened, loading model fails!
[WARNING] file /triton-model-repository/model_name/1/1-gpu/model.wte.bin cannot be opened, loading model fails!
[WARNING] file /triton-model-repository/model_name/1/1-gpu/model.final_layernorm.bias.bin cannot be opened, loading model fails!
[WARNING] file /triton-model-repository/model_name/1/1-gpu/model.final_layernorm.weight.bin cannot be opened, loading model fails!
```


### 6.7. Text generation

#### 6.7.1. Setup

You must start BigNLP training container with interactive session at your cluster.
You can do it with `srun` at slurm:

```
srun --partition=<SLURM PARTITION> \
        --container-workdir /bignlp_workdir \
        --container-image <TRAINING CONTAINER DOCKER IMAGE> \
        --container-mounts <FOLDER WITH BIGNLP SCRIPTS>:/bignlp_workdir \
        --pty bash
```

You must ensure that a vocabulary (`vocab.json`) and merge (`merges.txt`) files are accessible at a compute
node so you can pass the folder with those files as parameter for
scripts described below.

You need working instance of Triton Inference Server with loaded
FasterTransformer model converted from real checkpoint. You can use
`run_tritonserver.py` script described above to start an inference machine.

#### 6.7.2. Basic Text Generation

The simple implementation of text input script was prepared
as Python command line client script `bignlp/infer_scripts/chatbot.py`.
You can run it to send a simple request:
```sh
python3    bignlp/infer_scripts/chatbot.py \
        --url <TRITON CLUSTER NODE>:<PORT> \
        --protocol <PROTOCOL> \
        --datasets-dir <FOLDER WITH MERGES AND VOCABULARY> \
        --model-name <MODEL NAME> \
        --output-len <REQUESTED OUTPUT LEN> \
        --query "<TEXT QUERY>"
```

Parameters:
* `url`: Triton URL. It is printed by `run_tritonserver.py` script.
* `protocol`: Communication protocol (for example GRPC, HTTP).
* `dataset-dir`: Folder with downloaded merges and vocabulary files.
* `model-name`: Model name.
* `output-len`: Token sequence output length.
* `query`: Text sent to model as a query.

The additional inference parameters can be used to improve results of inference computation:
* `beam-width`: `uint32`, beam size for beam search, using sampling if set to 1.
* `top-k`: `unit32`, candidate number for sampling.
* `top-p`: `float`, candidate threshould for sampling.
* `temperature`: `float`, temperature for logit.
* `repetition-penalty`: `float`, repetition penalty for logit.

See all model
[parameters](https://github.com/triton-inference-server/fastertransformer_backend/blob/main/docs/gpt_guide.md#how-to-set-the-model-configuration)
in FasterTransformer repository.

The script will print out FasterTransformer output:
```sh
python3    bignlp/infer_scripts/chatbot.py --url triton-node:8001 --protocol grpc \
        --datasets-dir /bignlp_workdir/data/ \
        --temperature 1.0 \
        --top-k 1 \
        --top-p 0.9 \
        --repetition-penalty 1.0 \
        --model-name 20B_mega_real --output-len 40 \
        --query "A car is"
 a vehicle that can be driven by one person.

The word "car" comes from the French word for chariot, which was used to describe the first cars in the late 19th century. The first

```

You can change `output-len` to generate longer sequences, but a quality of output
from a small checkpoint degrades significantly when length is increased.

#### 6.7.3. Longer Text Generation

The script `author.py` was created to generate longer texts. It passes
an output from a previous inference to model again and asks FasterTransformer to generate more text.
The issue with this approach, is that a context of previous requests is lost quite fast and a model
forgets, what it outputted before.


```sh
python3    bignlp/infer_scripts/author.py \
        --url <TRITON CLUSTER NODE>:<PORT> \
        --protocol <PROTOCOL> \
        --datasets-dir <FOLDER WITH MERGES AND VOCABULARY> \
        --model-name <MODEL NAME> \
        --output-len <REQUESTED OUTPUT LEN> \
        --query "<TEXT QUERY>"
```

Parameters:
* `url`: Triton URL. It is printed by `run_tritonserver.py` script
* `protocol`: Communication protocol (for example grpc, http)
* `dataset-dir`: Folder with downloaded dataset, merges and vocabulary files.
* `model-name`: Model name.
* `output-len`: Token sequence output length.
* `query`: Text sent to model as a query.

Additional inference parameters can also be used with this script.

<details>

<summary>
Example below shows text generation.
</summary>

You can pass the text _AI is like a new steam engine_ to `author.py` to generate few paragraphs of text:

```sh
python3    bignlp/infer_scripts/author.py --url triton-node:8001 --protocol grpc \
        --datasets-dir /bignlp_workdir/data/ \
        --model-name 20B_mega_real \
        --output-len 40 \
        --query "AI is like a new steam engine."
 It’s not just about the technology, it’s also about how we can use AI to solve problems that are important for society and our economy.

The first thing I want to do is talk a little bit about what we mean by artificial intelligence (AI).

What is Artificial Intelligence?

Artificial intelligence is defined as “the ability of machines to perform tasks that normally require human intelligence.” This definition is broad and can be applied in many different ways, but it does not necessarily mean that the machine will actually think like a person. For example, a computer program may have been trained to recognize images of cats or dogs by analyzing millions of pictures. The program has learned how to identify these animals based on their features, such as ears, eyes^CKeyboard handler detected with signal

```
You can interrupt text generation by using `Ctrl+C`.

</details>

The `author.py` script uses output from previous query to generate more text.
The table below shows examples of input and output used for text generated above.

<details>

<summary>
The table below shows examples of input and output used for text generated above.
</summary>

| Input len | Input text | Output len | Output text |
| --------- | ---------- | ---------- | ----------- |
| 8 | 'AI is like a new steam engine.' | 40 | 'It's not just about the technology, it's also about how we can use AI to solve problems that are important for society and our economy. The first thing I want' |
| 40 | 'It's not just about the technology, it's also about how we can use AI to solve problems that are important for society and our economy. The first thing I want' | 40 | ' to do is talk a little bit about what we mean by artificial intelligence (AI). What is Artificial Intelligence?Artificial intelligence is defined as 'the ability of machines to perform' |
| 40 | 'to do is talk a little bit about what we mean by artificial intelligence (AI). What is Artificial Intelligence? Artificial intelligence is defined as 'the ability of machines to perform' | 40 | ' tasks that normally require human intelligence.' This definition is broad and can be applied in many different ways, but it does not necessarily mean that the machine will actually think like a person. For example' |
| 41 | 'tasks that normally require human intelligence.' This definition is broad and can be applied in many different ways, but it does not necessarily mean that the machine will actually think like a person. For example' | 40 | ', a computer program may have been trained to recognize images of cats or dogs by analyzing millions of pictures. The program has learned how to identify these animals based on their features, such as ears, eyes' |

</details>


#### 6.7.4. Dialogue Text Generation

The `dialogue.py` script was created to showcase text generation for a simple
support chatbot dialogue scenario:

```sh
python3    bignlp/infer_scripts/dialogue.py \
        --url <TRITON CLUSTER NODE>:<PORT> \
        --protocol <PROTOCOL> \
        --datasets-dir <FOLDER WITH MERGES AND VOCABULARY> \
        --model-name <MODEL NAME> \
        --output-len <REQUESTED OUTPUT LEN> \
        --customer "<TEXT CONTEXT FOR CUSTOMER ROLE>" \
        --support "<TEXT CONTEXT FOR SUPPORT ROLE>"
```

Parameters:
* `url`: Triton URL. It is printed by `run_tritonserver.py` script
* `protocol`: Communication protocol (for example grpc, http)
* `dataset-dir`: Folder with downloaded dataset, merges and vocabulary files.
* `model-name`: Model name.
* `output-len`: Token sequence output length.
* `customer`: Text used to generate prompt for a customer role.
* `support`: Text used to generate prompt for a support role.

Additional inference parameters can also be used with this script.

A model needs prompt to be able to generate text useful for chatbot application.
You must tell a machine, that it is working in a support team in your company and
answering questions from customers.

<details>

<summary>
Example below shows text generation.
</summary>


```sh
python3 bignlp/infer_scripts/dialogue.py --url triton-node:8001 --protocol grpc \
        --datasets-dir /bignlp_workdir/data/ \
        --model-name 20B_mega_real \
        --output-len 40 \
        --customer "NVIDIA customer:" \
        --support "NVIDIA machine learning expert:"
NVIDIA customer:What is machine learning?
NVIDIA machine learning expert: It's a way to make computers do things that they couldn't before.
NVIDIA customer: (END to FINISH): What I need to start experiments with machine learning?
NVIDIA machine learning expert: We can help you get started. We have a free trial of our GPU-accelerated deep learning platform, and we'll be happy to show you how it works.
NVIDIA customer: (END to FINISH): Can AI recognize cats?
NVIDIA machine learning expert: Sure! Let's try that!
NVIDIA customer: (END to FINISH): Can AI generate text?
NVIDIA machine learning expert: Yes, it can. It will take a few minutes to train the model.
NVIDIA customer: (END to FINISH): Is AI dangerous?
NVIDIA machine learning expert: No, not at all! We're just trying to help you make better decisions.
NVIDIA customer: (END to FINISH): END


```

</details>

The `dialogue.py` script reads an input from console, so you can just type
and press Enter to send a question to a model. It is extended with a prompt to
provide context. When you type _What is machine learning?_ then script sends text query:

```
NVIDIA customer: "What is machine learning?"
NVIDIA machine learning expert:

```

The model generates answer much longer than necessary:

```


"It\'s a way to make computers do things that they couldn\'t before."


------
\jamesblonde
I'm not sure what the point of this article was. It seems
```


A model can recognize from this prompt that quote characters should mark an expected
answer. It generates an answer but with more text because it was asked for 40 output
tokens here. Not all training datasets are good with teaching a model, when text
generation should stop, but they contain many dialogues from books and
support forums. The `author.py` script uses quote characters to wrap input
from user and later uses them to extract answer from a text generated by
a model. You must consider similar output cleaning and post processing
routines to use this solution.


<details>

<summary>
The table below shows examples of input and output used for text generated above.
</summary>

| Input len | Input text | Output len | Output text |
| --------- | ---------- | ---------- | ----------- |
| 15 | 'NVIDIA customer: "What is machine learning?" NVIDIA machine learning expert: ' | 40 | '"It's a way to make computers do things that they couldn\'t before."-jamesblonde. I\'m not sure what the point of this article was. It seems' |
| 41 | 'NVIDIA machine learning expert: "It's a way to make computers do things that they couldn\'t before." NVIDIA customer: "What I need to start experiments with machine learning?" NVIDIA machine learning expert: ' | 40 | '"We can help you get started. We have a free trial of our GPU-accelerated deep learning platform, and we'll be happy to show you how it works."The' |
| 56 | 'NVIDIA machine learning expert: "We can help you get started. We have a free trial of our GPU-accelerated deep learning platform, and we\'ll be happy to show you how it works." NVIDIA customer: "Can AI recognize cats?" NVIDIA machine learning expert: ' | 40 | '"Sure! Let's try that!"A: I think the best way is to use a library like Googlec or tens.net has is is moreing with a a' |
| 28 | 'NVIDIA machine learning expert: "Sure! Let's try that!" NVIDIA customer: "Can AI generate text?" NVIDIA machine learning expert: ' | 40 | '"Yes, it can. It will take a few minutes to train the model." NVIDIA customer: "Great! I\'ll wait here for you to finish training your model."A:' |
| 36 | 'NVIDIA machine learning expert: "Yes, it can. It will take a few minutes to train the model." NVIDIA customer: "Is AI dangerous?" NVIDIA machine learning expert: ' | 40 | '"No, not at all! We\'re just trying to help you make better decisions."A: I think this is an interesting question and I\'m going to try my hand' |

</details>

#### 6.7.5. Inference Parameters

Inference related parameters like `temperature`, `top_k`, and `top_p` are stored in
`config.pbtxt` file inside the Triton model repository.

The parameters are set like this:

```
parameters {
    key: "top_k"
    value {                                                                                                                                                
        string_value: "1"
    }
}
parameters {
    key: "top_p"
    value {
        string_value: "0.0"
    }
}
```
You can modify them using text editor. Since the FasterTransformer backend reads the
parameters when the model is loaded, the compute node with the new configuration must
be started again to apply the change. The FasterTransformer
cannot be restarted in the same compute job due to MPI limitations.

The C++ inference engine reads parameters from the Triton configuration and runs inference
using weight files. Some parameters are determined by weights created during
training but other parameters can be adjusted to improve inference results
for different tasks.

There are three main types of parameters:
* Parameters derived from training configurations.
    These cannot be changed later, you must train
     a new model to modify them. The weight files structure depends on them.    Example: `decoder_layers`.
* Parameters decided during the conversion from PyTorch to
     FasterTransformer. Example: `tensor_para_size`.
* Parameters adjustable for inference. These can be changed after training to
     improve the accuracy of your inference task. Example `top_k`.


<details>

<summary>
Triton parameters table
</summary>

| Parameter Name                             | Example Value | Determined by Weights | Comment                                                                                                                                                                                                                |
|------------------------------|---------------|-----------------------|----------------------------------------------------------------------------------------------------------------|
| `beam_search_diversity_rate` | 0.0                     | No                                        | Adjust to improve inference results                                                                                                                                                        |
| `beam_width`                                 | 1                         | No                                        | Adjust to improve inference results                                                                                                                                                        |
| `decoder_layers`                         | 44                        | Yes                                     | Decided during training                                                                                                                                                                                |
| `end_id`                                         | 50256                 | Yes                                     | Derived from vocabulary used during training                                                                                                                                     |
| `head_num`                                     | 48                        | Yes                                     | Decided during training                                                                                                                                                                                |
| `inter_size`                                 | 24576                 | Yes                                     | Decided during training                                                                                                                                                                                |
| `is_half`                                        | 1                         | No                                        | Do not change                                                                                                                                                                                                    |
| `len_penalty`                                | 1                         | No                                        | Adjust to improve inference results                                                                                                                                                        |
| `max_input_len`                            | 60                        | No                                        | Can be used for optimization                                                                                                                                                                    |
| `max_seq_len`                                | 80                        | No                                        | The maximum output sequence length we can serve. Parameter is used for buffer allocation                                            |
| `model_name`                                 | model_name    | No                                        | Name                                                                                                                                                                                                                     |
| `pipeline_para_size`                 | 1                         | No                                        | Can be modified but number of nodes used to run a model must match. It must divide the number of layers             |
| `repetition_penalty`                 | 1.0                     | No                                        | Adjust to improve inference results                                                                                                                                                        |
| `size_per_head`                            | 128                     | Yes                                     | Decided during training                                                                                                                                                                                |
| `start_id`                                     | 50256                 | Yes                                     | Derived from vocabulary used during training                                                                                                                                     |
| `temperature`                                | 1.0                     | No                                        | Adjust to improve inference results                                                                                                                                                        |
| `tensor_para_size`                     | 4                         | Yes                                     | Decided during conversion to FasterTransformer checkpoint. It must be equal to number of used GPUs                        |
| `top_k`                                            | 1                       | No                                        | Adjust to improve inference results                                                                                                                                                        |
| `top_p`                                            | 0.9                     | No                                        | Adjust to improve inference results                                                                                                                                                        |
| `vocab_size`                                 | 51200                 | Yes                                     | Derived from vocabulary used during training                                                                                                                                     |


</details>

## 7. Performance
<a id="markdown-performance" name="performance"></a>

### 7.1. GPT-3 Results
<a id="markdown-gpt-3-results" name="gpt-3-results"></a>

#### 7.1.1. Training Accuracy Results
Training Accuracy: NVIDIA DGX SuperPOD (8 x 8 x A100 80GB for 126M GPT-3 Model; 20 x 8 x A100 80GB for 5B GPT-3 Model)

We evaluated the 126M parameter and 5B parameter models on 8 different language
tasks. The results can be found in the table below. All the tasks are provided
as part of the evaluation harness, so the user can evaluate any `.nemo`
checkpoint file on all these tasks.

|Task                            |Metric                        | 126M                         | 5B                             |
| ---------------- | ---------------- | ---------------- | ---------------- |
|Lambada                     |Accuracy                    | 38.70%                     | 68.93%                     |
|                                    |PPL                             | 25.8                         | 4.22                         |
|Boolq                         |Accuracy                    | 56.94%                     | 65.29%                     |
|Race                            |Accuracy                    | 28.71%                     | 38.66%                     |
|                                    |Accuracy Norm         | 34.74%                     | 41.62%                     |
|Piqa                            |Accuracy                    | 61.21%                     | 73.88%                     |
|                                    |Accuracy Norm         | 61.97%                     | 75.40%                     |
|Hellaswag                 |Accuracy                    | 28.48%                     | 46.45%                     |
|                                    |Accuracy Norm         | 29.54%                     | 60.85%                     |
|Winogrande                |Accuracy                    | 50.43%                     | 60.77%                     |
|Wikitext2                 |Word PPL                    | 31.35                        | 12.36                        |
|                                    |Byte PPL                    | 1.9                            | 1.6                            |
|                                    |Bits per Byte PPL | 0.64                         | 0.47                         |
|Wikitext103             |Word PPL                    | 31.35                        | 12.36                        |
|                                    |Byte PPL                    | 1.9                            | 1.6                            |
|                                    |Bits per Byte PPL | 0.64                         | 0.47                         |

Training the 5B GPT-3 model to convergence takes 6.5 days, and the loss curve can be seen in the figure below:

<img src="img/5B_GPT_3_loss_final.svg"/>

The table below shows the converged training loss, the throughput, and the
total time to train for the 5B GPT-3 model, using a given number of GPUs and a
given Global Batch Size (GBS).

| \#GPUs | GBS    | Seq Length | \#Tokens | Loss    | Throughput (Tokens/sec) | Time to Train (days) |
| ------ | ---- | ---------- | -------- | ----- | ----------------------- | -------------------- |
| 160    | 1440 | 2048       | 300B     | 1.685 | 726,384                 | 4.8                  |


#### 7.1.2. Training Performance Results
<a id="markdown-training-performance-results" name="training-performance-results"></a>
Training performance: NVIDIA DGX SuperPOD (20 x 8 x A100 80GB for 5B GPT-3 model)

We measured the throughput of training a 5B parameter GPT-3 model on a DGX
SuperPOD using a different number of nodes, and we achieved near-linear
scaling. For example, when scaling from 1 node to 20 nodes, we achieve 18.51x
speedup. The table and chart below show the performance results.

|      |                                 |        |        |        | Nodes  |        |        |        |
| ---- | ------------------------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|      |                                 | 1      | 2      | 5      | 9      | 10     | 18     | 20     |
|      | Tokens per Second               | 39543  | 79128  | 195047 | 344523 | 383500 | 670254 | 731791 |
| 5B   | Perfect Linear Scaling (Tokens) | 39543  | 79086  | 197715 | 355887 | 395430 | 711774 | 790860 |
|      | Speed-up                        | 1x     | 2x     | 4.93x  | 8.71x  | 9.7x   | 16.95x | 18.51x |

<img src="img/5B_GPT_3_throughput.svg"/>

#### 7.1.3. Inference Performance
<a id="markdown-inference-performance" name="inference-performance"></a>

The most important factor for NLP model performance is the size of a model. You
can use a smaller model to get faster inference but it will likely degrade your
accuracy.

If you know your model size, then there are two parameters you can vary to find
the best throughput and keep inside a latency budget:
* Number of GPUs used for one instance of your model.
* Batch size used during processing requests.

The same model can be executed with different amounts of GPUs and nodes so the
basic throughput values don't reflect cost of inference like for one GPU model.
A throughput normalized to one GPU is used as a proxy for cost of inference in
graphs and tables below.


The FasterTransformer hardware configuration is described by two parameters:
* Tensor parallel (TP) size - number of GPUs used at each node for computation.
* Pipeline parallel (PP) size - number of nodes used for one instance of model.
The number of GPUs used for computation is determined by multiplying those two
numbers. Only easily divisible parts of the whole DGX A100 system was considered
during tests so it will be easy to deploy a model in a cluster.

The table below contains a summary of used configurations.

| TP | PP | #GPUs | #Nodes | Max GPU RAM \[GB\] |
| -- | -- | ----- | ------ | ------------------ |
| 1    | 1    | 1         | 1            | 80                                 |
| 2    | 1    | 2         | 1            | 160                                |
| 4    | 1    | 4         | 1            | 320                                |
| 8    | 1    | 8         | 1            | 640                                |
| 8    | 2    | 16        | 2            | 1280                             |
| 8    | 3    | 24        | 3            | 1920                             |
| 8    | 4    | 32        | 4            | 2560                             |


##### 7.1.3.1. 5B Model
<a id="markdown-b-model" name="b-model"></a>

The 5B model can fit into a single A100 80GB GPU. Still FasterTransformer can
run 5B model using tensor parallel splitting of model between multiple GPUs and
pipeline parallel, when different transformer layers are distributed across
many nodes it gives the possibility to utilize different tradeoffs (e.g.
latency vs throughput). You can also consider using several DGX nodes in DGX
SuperPOD as one instance of the FasterTransformer model. You should also
consider an inference task for your application. Some inference tasks require
longer token sequence lengths for input and output.

##### 7.1.3.2. 5B Chatbot for Question Answering
<a id="markdown-b-chatbot-for-question-answering" name="b-chatbot-for-question-answering"></a>

Let us consider a scenario with a chatbot for question answering. It can be
implemented with FasterTransformer, when sequence length for input tokens is 60
and output length is 20. Two graphs below show how latency and throughput vary,
when a certain number of GPUs is used for inference for batch size=1 and for
batch size=256.


<img src="img/5B_GPT_3_batch_size_1_input_len_60_output_len_20.svg"/>
<img src="img/5B_GPT_3_batch_size_256_input_len_60_output_len_20.svg"/>

If latency achievable at 1-GPU configuration fits within latency budget, then
the best performance can be derived from the graph below, which shows how
latency and throughput change for different batch sizes used for computations.


<img src="img/5B_GPT_3_of_GPU_1_input_len_60_output_len_20.svg"/>

A chatbot with a latency budget within 380 ms can work for batch size=64 and 1
GPU used for computation.


##### 7.1.3.3. 5B: Translation and Style Transfer
<a id="markdown-b%3A-translation-and-style-transfer" name="b%3A-translation-and-style-transfer"></a>

A translation or style transfer inference task requires input length 200 and
output length 200.

<img src="img/5B_GPT_3_batch_size_1_input_len_200_output_len_200.svg"/>
<img src="img/5B_GPT_3_batch_size_256_input_len_200_output_len_200.svg"/>

The graph for 1 GPU with many batch sizes shows what batch size can fit into a
certain latency budget.


<img src="img/5B_GPT_3_of_GPU_1_input_len_200_output_len_200.svg"/>

The graph clearly shows that the translation or style transfer inference task
with latency budget 2000 milliseconds can be deployed using 1 GPU and batch
size = 16.

##### 7.1.3.4. Summary for 5B Results
<a id="markdown-summary-for-5b-results" name="summary-for-5b-results"></a>

The table below contains performance measurements from all graphs for the 5B
model running in FasterTransformer at DGX A100 80 GB system.

<details>

<summary>
5B model: Latency and throughput for different number of GPUs and batch sizes.
</summary>

| GPUs | Latency p99                                | Normalized throughput to 1 GPU | Latency p99 | Normalized throughput to 1 GPU | Latency p99                                    | Normalized throughput to 1 GPU | Latency p99 | Normalized throughput to 1 GPU |
| ---- | -------------------------- | ------------------------------ | ----------- | ------------------------------ | ---------------------------- | ------------------------------ | ----------- | ------------------------------ |
|            | Input len 60 output len 60 |                                                                |                         |                                                                | Input len 200 output len 200 |                                                                |                         |                                                                |
|            | BS=256                                         |                                                                | BS=1                |                                                                | BS=256                                             |                                                                | BS=1                |                                                                |
| 1        | 1143                                             | 224                                                        | 172                 | 5.81                                                     | 9048                                                 | 28.3                                                     | 1623                | 0.616                                                    |
| 2        | 799                                                | 160                                                        | 126                 | 3.95                                                     | 6018                                                 | 21.3                                                     | 1219                | 0.410                                                    |
| 4        | 529                                                | 121                                                        | 94                    | 2.66                                                     | 3939                                                 | 16.2                                                     | 923                 | 0.271                                                    |
| 8        | 436                                                | 73                                                         | 115                 | 1.08                                                     | 3154                                                 | 10.1                                                     | 998                 | 0.125                                                    |
| 16     | 327                                                | 49                                                         | 101                 | 0.62                                                     | 2776                                                 | 5.8                                                        | 977                 | 0.064                                                    |
| 24     | 273                                                | 39                                                         | 100                 | 0.42                                                     | 2484                                                 | 4.3                                                        | 950                 | 0.044                                                    |
| 32     | 284                                                | 28                                                         | 95                    | 0.33                                                     | 2517                                                 | 3.2                                                        | 897                 | 0.035                                                    |

</details>

##### 7.1.3.5. 20B Model
<a id="markdown-b-model" name="b-model"></a>

To improve accuracy a larger model can be used.

##### 7.1.3.6. 20B: Chatbot for Question Answering
<a id="markdown-b%3A-chatbot-for-question-answering" name="b%3A-chatbot-for-question-answering"></a>

<img src="img/20B_GPT_3_batch_size_1_input_len_60_output_len_20.svg"/>
<img src="img/20B_GPT_3_batch_size_256_input_len_60_output_len_20.svg"/>
<img src="img/20B_GPT_3_of_GPU_1_input_len_60_output_len_20.svg"/>

##### 7.1.3.7. 20B: Translation and Style Transfer
<a id="markdown-b%3A-translation-and-style-transfer" name="b%3A-translation-and-style-transfer"></a>

<img src="img/20B_GPT_3_batch_size_1_input_len_200_output_len_200.svg"/>
<img src="img/20B_GPT_3_batch_size_256_input_len_200_output_len_200.svg"/>
<img src="img/20B_GPT_3_of_GPU_4_input_len_200_output_len_200.svg"/>

##### 7.1.3.8. Summary for 20B Results
<a id="markdown-summary-for-20b-results" name="summary-for-20b-results"></a>

The table below contains performance measurements from all graphs for the 20B
model running in FasterTransformer at DGX A100 80GB.

<details>

<summary>
20B model: Latency and throughput for different number of GPUs and batch sizes.
</summary>

| GPUs | Latency p99                                | Normalized throughput to 1 GPU | Latency p99 | Normalized throughput to 1 GPU | Latency p99                                    | Normalized throughput to 1 GPU | Latency p99 | Normalized throughput to 1 GPU |
| ---- | -------------------------- | ------------------------------ | ----------- | ------------------------------ | ---------------------------- | ------------------------------ | ----------- | ------------------------------ |
|            | Input len 60 output len 60 |                                                                |                         |                                                                | Input len 200 output len 200 |                                                                |                         |                                                                |
|            | BS=256                                         |                                                                | BS=1                |                                                                | BS=64,128,256                                |                                                                | BS=1                |                                                                |
| 1        | 4146                                             | 62                                                         | 560                 | 1.78                                                     | 10772                                                | 5.9                                                        | 5650                | 0.177                                                    |
| 2        | 2429                                             | 53                                                         | 359                 | 1.39                                                     | 10544                                                | 6.1                                                        | 3548                | 0.141                                                    |
| 4        | 1592                                             | 40                                                         | 251                 | 1.00                                                     | 10453                                                | 6.1                                                        | 2486                | 0.101                                                    |
| 8        | 1169                                             | 27                                                         | 230                 | 0.54                                                     | 7909                                                 | 4.0                                                        | 2147                | 0.058                                                    |
| 16     | 923                                                | 17                                                         | 218                 | 0.29                                                     | 7380                                                 | 2.2                                                        | 2131                | 0.029                                                    |
| 24     | 758                                                | 14                                                         | 218                 | 0.19                                                     | 6511                                                 | 1.6                                                        | 2123                | 0.020                                                    |
| 32     | 742                                                | 11                                                         | 224                 | 0.14                                                     | 6200                                                 | 1.3                                                        | 2124                | 0.015                                                    |

</details>

##### 7.1.3.9. Model Size and Performance
<a id="markdown-model-size-and-performance" name="model-size-and-performance"></a>

###### 7.1.3.9.1. Online Scenario
<a id="markdown-online-scenario" name="online-scenario"></a>

An online scenario focuses on the minimization of latency. Large checkpoints
were generated with randomly initialized weights.

<img src="img/Chatbot_Q_A_batch_size_1_input_len_60_output_len_20.svg"/>

<img src="img/Translation_or_style_transfer_batch_size_1_input_len_200_output_len_200.svg"/>

The performance measurements were obtained on DGX A100 80 GB nodes.

<details>

<summary>
Performance for different model sizes in online scenario
</summary>

|                                                 | Len input 60 output 20 |                                     |                        |                                                         |                                                                |                                | Len input 200 output 200 |                                     |                        |                                                         |                                                                |                                |
| ----------------------- | ---------------------- | ----------------- | ---------- | --------------------------- | ------------------------------ | -------------- | ------------------------ | ----------------- | ---------- | --------------------------- | ------------------------------ | -------------- |
| Parameters number \[B\] | Latency\[ms\]                    | Infer/sec per GPU | Batch size | Tensor parallel (GPUs used) | Pipeline parallel (nodes used) | Number of GPUs | Latency\[ms\]                        | Infer/sec per GPU | Batch size | Tensor parallel (GPUs used) | Pipeline parallel (nodes used) | Number of GPUs |
| 5B                                            | 93                                         | 2.68                            | 1                    | 4                                                     | 1                                                            | 4                            | 923                                            | 0.271                         | 1                    | 4                                                     | 1                                                            | 4                            |
| 13B                                         | 189                                        | 1.32                            | 1                    | 4                                                     | 1                                                            | 4                            | 1893                                         | 0.132                         | 1                    | 4                                                     | 1                                                            | 4                            |
| 20B                                         | 251                                        | 0.50                            | 1                    | 8                                                     | 1                                                            | 8                            | 2230                                         | 0.056                         | 1                    | 8                                                     | 1                                                            | 8                            |
| 89B                                         | 464                                        | 0.27                            | 1                    | 8                                                     | 1                                                            | 8                            | 4585                                         | 0.027                         | 1                    | 8                                                     | 1                                                            | 8                            |
| 175B                                        | 923                                        | 0.14                            | 1                    | 8                                                     | 1                                                            | 8                            | 8873                                         | 0.014                         | 1                    | 8                                                     | 1                                                            | 8                            |
| 310B                                        | 1354                                     | 0.09                            | 1                    | 8                                                     | 1                                                            | 8                            | 13391                                        | 0.005                         | 1                    | 8                                                     | 2                                                            | 16                         |
| 530B                                        | 2035                                     | 0.03                            | 1                    | 8                                                     | 3                                                            | 24                         | 21034                                        | 0.002                         | 1                    | 8                                                     | 3                                                            | 24                         |

</details>

###### 7.1.3.9.2. Offline Scenario
<a id="markdown-offline-scenario" name="offline-scenario"></a>

The offline scenario focuses on maximum throughput. The two graphs below show
latency and throughput for two tasks. The first one is chatbot questions
answering and a second one is translation or style transfer.

<img src="img/Chatbot_Q_A_batch_size_256_input_len_60_output_len_20.svg"/>

<img src="img/Translation_or_Style_Transfer_batch_size_max_input_len_200_output_len_200.svg"/>

The chatbot scenario can be executed with batch size equal to 256 for all model
sizes so it is possible to utilize computing resources in GPUs.


<details>

<summary>
Performance for different model sizes in offline scenario
</summary>

|                                                 | Len input 60 output 20 |                                     |                        |                                 |                                                                |                                | Len input 200 output 200 |                                     |                        |                                                         |                                                                |                                |
| ----------------------- | ---------------------- | ----------------- | ---------- | --------------- | ------------------------------ | -------------- | ------------------------ | ----------------- | ---------- | --------------------------- | ------------------------------ | -------------- |
| Parameters number \[B\] | Latency\[ms\]                    | Infer/sec per GPU | Batch size | Tensor parallel | Pipeline parallel (nodes used) | Number of GPUs | Latency\[ms\]                        | Infer/sec per GPU | Batch size | Tensor parallel (GPUs used) | Pipeline parallel (nodes used) | Number of GPUs |
| 5B                      | 1143                                     | 224.0                           | 256                | 1                             | 1                                                            | 1                            | 9047                                         | 28.297                        | 256                | 1                                                     | 1                                                            | 1                            |
| 13B                     | 2756                                     | 92.9                            | 256                | 1                             | 1                                                            | 1                            | 13390                                        | 9.559                         | 256                | 2                                                     | 1                                                            | 2                            |
| 20B                     | 4145                                     | 61.8                            | 256                | 1                             | 1                                                            | 1                            | 10453                                        | 6.123                         | 256                | 4                                                     | 1                                                            | 4                            |
| 89B                     | 4686                                     | 22.2                            | 256                | 4                             | 1                                                            | 4                            | 17815                                        | 1.796                         | 256                | 8                                                     | 1                                                            | 8                            |
| 175B                    | 5728                                     | 15.7                            | 256                | 8                             | 1                                                            | 8                            | 16181                                        | 0.494                         | 64                 | 8                                                     | 1                                                            | 8                            |
| 310B                    | 6768                                     | 2.4                             | 256                | 8                             | 2                                                            | 16                           | 13686                                        | 0.018                         | 2                  | 8                                                     | 1                                                            | 8                            |
| 530B                    | 10588                                    | 0.8                             | 256                | 8                             | 3                                                            | 24                           | 21034                                        | 0.002                         | 1                  | 8                                                     | 3                                                            | 24                         |

</details>


### 7.2. T5 Results
<a id="markdown-t5-results" name="t5-results"></a>

#### 7.2.1. Training Accuracy Results
Training Accuracy: NVIDIA DGX SuperPOD (4 x 8 x A100 80GB for 220M T5 Model; 20 x 8 x A100 80GB for 3B T5 Model)

We evaluated the 220M parameter and 3B parameter T5 models on 2 GLUE
tasks. The results can be found in the table below. The user can 
finetune on top of any `.nemo` trained checkpoint file on all available 
GLUE tasks mentioned in T5 finetuning section with their own recipes.

| Task        |Metric                        | 220M    | 3B    |
|---------| ---------------- |-------|-------|
| MNLI-m    |Accuracy                    | 86.8% | 90.6% |
| MNLI-mm |Accuracy                    | 87.3% | 90.6% |
| SST-2     |Accuracy                    | 94.3% | 97.2% |

Training the 220M T5 model to convergence takes 4 days, and the loss curve can be seen in the figure below:

<img src="img/220M_T5_loss_final.svg"/>

The table below shows the converged training loss, the throughput, and the
total time to train for the 220M T5 model, using a given number of GPUs and a
given Global Batch Size (GBS).

| \#GPUs | GBS    | Seq Length | \#Tokens | Loss    | Throughput (Tokens/sec) | Time to Train (days) |
|--------|------|------------|----------|-------|-------------------------|----------------------|
| 32         | 2048 | 512                | 1T             | 1.501 | 3,273,728                             | 4                                        |


Training the 3B T5 model to convergence takes 11 days, and the loss curve of a fully trained model can be seen in the figure below:

<img src="img/3B_T5_loss_100percent.svg"/>

The table below shows the converged training loss, the throughput, and the
total time to train for the 3B T5 model, using a given number of GPUs and a
given Global Batch Size (GBS).

| \#GPUs | GBS    | Seq Length | \#Tokens | Loss  | Throughput (Tokens/sec) | Time to Train (days) |
|--------|------|------------|----------|--------------------|-------------------------|----------------------|
| 160        | 2160 | 512                | 1T             | 1.147                            | 1,395,131                             | 11                                     |



#### 7.2.2. Training Performance Results
<a id="markdown-training-performance-results" name="training-performance-results"></a>
Training Performance: NVIDIA DGX SuperPOD (20 x 8 x A100 80GB for 3B T5 Model)

We measured the throughput of training a 3B parameter T5 model on NVIDIA DGX
SuperPOD using a different number of nodes. When scaling from 1 node to 20 nodes, we achieve 16.38x
speedup. We are actively working on improving the scaling performance for T5 models. The table and chart below show the performance results.


|         |                                        |        |                |                | Nodes    |                |                 |
|-----|----------------------------------------|--------|--------|--------|--------|--------|---------|
|         |                                        | 1      | 2            | 4            | 5            | 10         | 20            |
|         | Tokens per Second                      |103842|	204421	|397813	|489345	|929345	|1701415|
| 3B    | Perfect Linear Scaling (Tokens)        |  103842|	207685	|415369	|519211	|1038423|	2076845|
|         | Speed-up                               |1x	  | 1.97x	|3.83x	|4.71x	|8.95x	|16.38x|

<img src="img/3B_T5_throughput_2205.svg"/>



### 7.3. mT5 Results
<a id="markdown-t5-results" name="t5-results"></a>

#### 7.3.1. Training Accuracy Results
Training Accuracy: NVIDIA DGX SuperPOD (4 x 8 x A100 80GB for 170M mT5 Model; 8 x 8 x A100 80GB for 390M mT5 Model; 20 x 8 x A100 80GB for 3B mT5 Model)

We evaluated the 170M parameter, 390M parameter, and 3B parameter mT5 models on XNLI
task. The results can be found in the table below. The user can 
finetune on top of any `.nemo` trained checkpoint file on `XNLI` task mentioned in mT5 finetuning section.

| Task-Language | Metric    | 170M  | 390M  | 3B    |
|---------------|-----------|-------|-------|-------|
| XNLI-en       | Accuracy  | 80.1% | 84.6% | 89.4% |
| XNLI-es       | Accuracy  | 73.3% | 79.3% | 86.4% |
| XNLI-de       | Accuracy  | 69.6% | 76.4% | 84.5% |
| XNLI-fr       | Accuracy  | 72.2% | 78.6% | 85.8% |
| XNLI-zh       | Accuracy  | 73.8% | 70.1% | 79.9% |


Training the 170M mT5 model to convergence takes 4 days, and the loss curve can be seen in the figure below:

<img src="img/170M_mT5_loss_final.svg"/>

The table below shows the converged training loss, the throughput, and the
total time to train for the 170M mT5 model, using a given number of GPUs and a
given Global Batch Size (GBS).

| \#GPUs | GBS    | Seq Length | \#Tokens | Loss  | Throughput (Tokens/sec) | Time to Train (days) |
|--------|------|------------|----------|-------|-------------------------|----------------------|
| 32         | 2048 | 512                | 1T             | 1.980 | 4,112,062               | 4                                        |




Training the 390M mT5 model to convergence takes 4 days, and the loss curve can be seen in the figure below:

<img src="img/390M_mT5_loss_final.svg"/>

The table below shows the converged training loss, the throughput, and the
total time to train for the 390M mT5 model, using a given number of GPUs and a
given Global Batch Size (GBS).

| \#GPUs | GBS    | Seq Length | \#Tokens | Loss  | Throughput (Tokens/sec) | Time to Train (days) |
|--------|------|------------|----------|-------|-------------------------|----------------------|
| 64     | 2048 | 512                | 1T             | 1.584 | 3,744,914               | 4                                        |


Training the 3B mT5 model to convergence takes 14 days, and the loss curve of a fully trained model can be seen in the figure below:

<img src="img/3B_mT5_loss_final.svg"/>

The table below shows the converged training loss, the throughput, and the
total time to train for the 3B T5 model, using a given number of GPUs and a
given Global Batch Size (GBS).

| \#GPUs | GBS  | Seq Length | \#Tokens | Loss   | Throughput (Tokens/sec) | Time to Train (days) |
|--------|------|------------|----------|--------|-------------------------|----------------------|
| 160        | 1920 | 512                | 1T             | 1.134  | 911,065                 | 14                   |


#### 7.3.2. Training Performance Results
<a id="markdown-training-performance-results" name="training-performance-results"></a>
Training Performance: NVIDIA DGX SuperPOD (20 x 8 x A100 80GB for 3B mT5 Model)

We measured the throughput of training a 3B parameter mT5 model on NVIDIA DGX
SuperPOD using a different number of nodes. When scaling from 1 node to 20 nodes, we achieve 14.87x
speedup. We are actively working on improving the scaling performance for mT5 models. 
The table and chart below show the performance results.


|         |                                    |        |         |         | Nodes   |         |          |
|---------|------------------------------------|--------|---------|---------|---------|---------|----------|
|         |                                    | 1      | 2       | 4       | 5       | 10      | 20       |
|         | Tokens per Second                  | 87685	 | 172433	 | 336312  |411142	| 769202  | 1303767  |
| 3B      | Perfect Linear Scaling (Tokens)    | 87685	 | 175371	 | 350741  |438427	| 876853  | 1753706  |
|         | Speed-up                           | 1x	    | 1.97x	  | 3.84x	  |4.69x   	| 8.77x  | 14.87x |

<img src="img/3B_mT5_throughput_2205.svg"/>


## 8. Changelog
<a id="markdown-changelog" name="changelog"></a>

**NeMo Megatron 22.06.RC1**
* Relative Position Embedding for T5 - early access
  - **Disclaimer:** We have confirmed that the loss curves for the two Relative Position Embeddings implementations (Megatron-LM and NeMo Megatron) are matching based on a partial convergence run. However, we observed lower accuracy results for Relative Position Embeddings compared to Absolute Position Embeddings. NVIDIA engineers are now conducting additional verification of Relative Position Embeddings.
* Hyperparameter tool: support for DGX A100 40GB configurations
* P-Tuning and Prompt Tuning for GPT-3 with pipeline parallelism (training only)
* Operation fusions for higher training throughput

**NeMo Megatron 22.05.01**
* Cloud service providers: support for Microsoft Azure (performance validated up to 36 `Standard_ND96amsr_A100_v4` instances)
* Cluster validation tools (DGMI, NCCL)
* 20B GPT-3 training configuration improved by 2.7% for higher throughput

**NeMo Megatron 22.05**
* Asynchronous gradient all-reduce for GPT-3, T5, mT5 models with pipeline parallel size equal to 1
* P-Tuning and Prompt Tuning for GPT-3 with tensor parallelism (training only)
* Hyperparameter tool to find the highest throughput configs for training and inference on Base Command Manager
* Custom tokenizer support (training only)
* GPT-3 with pipeline parallelism support on Base Command Manager (inference)
* Hyperparameters for text generation: top-p, top-k, and temperature

**NeMo Megatron 22.04**
* T5 with pipeline parallelism support (training only)
* Switched from GeLU to GeGLU as activation function for T5
* mT5 with tensor parallelism and pipeline parallelism support (training only)
* 11B, 23B, and 41B T5 training configurations
* 170M, 390M, and 3B mT5 training configurations
* Automatic and configurable Non-Uniform Memory Access (NUMA) mapping

**NeMo Megatron 22.03**
* T5 with tensor parallelism support (optimized for <20B parameters, training only)
* 220M and 3B T5 training configurations
* GLUE fine-tuning and evaluation support for T5

**NeMo Megatron 22.02**
* GPT-3 with pipeline parallelism support (training only)
* 40B and 175B GPT-3 training configurations

**NeMo Megatron 22.01**
* GPT-3 with tensor parallelism support on Base Command Platform
* O2-style AMP (accelerated training of larger models)
* Chatbot sample application using your trained GPT-3 model
* Training metric monitoring and visualization with Weights & Biases

## 9. Known Issues
<a id="markdown-known-issues" name="known-issues"></a>
* We observe lower accuracy results for Relative Position Embeddings compared to Absolute Position Embeddings
* The 22.05 inference container provides better performance for large models like 530B, but can be slower for 5B model for some configurations
* The inference profiling scripts can fail to produce final summary of results due to the division by zero error. The results are still present in CSV files
* For customers looking to do inference on BCP please use a previous inference container
