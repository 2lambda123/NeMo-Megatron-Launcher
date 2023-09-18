
params=()
if [[ $MAX_STEPS -le 100 ]]; then # If greater than hundred we use defaults set in the training config file.
  LOG_EVERY_N_STEPS=`expr $MAX_STEPS / 100`
  VAL_CHECK_INTERVAL=`expr $MAX_STEPS / 5`
  LIMIT_VAL_BATCHES=`expr $MAX_STEPS / 20`
  params+=(training.trainer.log_every_n_steps=$LOG_EVERY_N_STEPS)
  params+=(training.trainer.limit_val_batches=$LIMIT_VAL_BATCHES)
  params+=(training.trainer.val_check_interval=$VAL_CHECK_INTERVAL)
fi
if [[ ! -z $LOCAL_NEMO_PATH ]]; then
  params+=("container_mounts=[${LOCAL_NEMO_PATH}:/opt/bignlp/NeMo]")
fi
DATA_DIR=/lustre/fsw/joc/big_nlp/gpt3/prepare_dataset/the_pile/train
DATA_PREFIX=[1.0,/lustre/fsw/joc/big_nlp/gpt3/prepare_dataset/the_pile/train/my-gpt3_00_text_document]

set -o xtrace

RUN_MODEL="gpt3"
RUN_MODEL_SIZE="126m"
TP_SIZE=1
PP_SIZE=1
NUM_NODES=1
BUILD_IMAGE_NAME_SBATCH="nvcr.io/nvidian/bignlp-train:23.08-nemofw-nightly"
BASE_RESULTS_DIR="/home/pagaray/code/NeMo-Megatron-Launcher-results"

#TODO : Can add additional parameters (key value pairs from gitlab-ci.yaml file)
HYDRA_FULL_ERROR=1 NEMO_LAUNCHER_CI=1 python3 main.py \
    training=${RUN_MODEL}/${RUN_MODEL_SIZE} \
    stages=["training"] \
    launcher_scripts_path=${LAUNCHER_PATH} \
    data_dir=${DATA_DIR} \
    base_results_dir=${BASE_RESULTS_DIR} \
    "container='${BUILD_IMAGE_NAME_SBATCH}'" \
    training.run.name=${RUN_NAME} \
    training.run.time_limit=${TIME_LIMIT} \
    training.trainer.num_nodes=${NUM_NODES} \
    training.trainer.max_steps=${MAX_STEPS} \
    training.model.tensor_model_parallel_size=${TP_SIZE} \
    training.model.pipeline_model_parallel_size=${PP_SIZE} \
    training.model.data.data_prefix=${DATA_PREFIX} \
    "${params[@]}" ${ADDITIONAL_PARAMS}

