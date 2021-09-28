# BigNLP-Scripts

Scripts and code to provide end-to-end data preparation and training for
Megatron-LM.

The training dataset is "[The Pile](https://pile.eleuther.ai/)" and it consists
of 22 smaller dataset. The dataset is already blended by using the mix
described in their [paper](https://arxiv.org/pdf/2101.00027.pdf).

It is best to store this repository in a file system shared by all the nodes,
since the downloaded datasets will be stored inside this repository.


## Dependencies:

1. Install dependencies: 

        cd bignlp-scripts
        pip3 install --user -r requirements.txt

2. Clone the Megatron-LM repository as a submodule. Both the preprocessing and
training need the Megatron-LM repository.

        cd bignlp-scripts
        git submodule update --init --recursive


## Download and Preprocess Training Dataset
Main directory: prepare_dataset


#### Usage:
First, update the default config inside bignlp-scripts/conf/config.yaml, to
decide which config to use for the data preparation part of your job. 
More specifically, select or update the config inside 
bignlp-scripts/conf/data_preparation to perform the tasks you need.  

Once the config is set correctly, run:

    cd prepare_dataset
    python3 end_to_end_data_prep.py

NOTE: This project uses Hydra config, so you can always override any of the
configuration parameters from the CLI. See the hydra documentation for
examples on how to do this.



#### Tricks and Tips:
##### Using a Subset of the Training Data
If you want to download only a subset of the training data, you can download
any of the 30 files that comprise it.

Set the file_numbers: "0-29" to the files you want to download, using any
numbers from 0 to 29, either separated by a comma or a dash.
If you do this, you will also need to modify the gpt_blend.sh file to match the
datasets to use for training later on.

For example, to download only the 0th file:
    file_numbers: "0"

##### Limiting the number of nodes in the cluster
Use the nodes parameter in the data_preparation config file.
For example, to use only 4 nodes per job, set:
nodes: 4


#### Result Dataset:
The result will be the dataset in binary format (.bin) stored in a directory
named `the_pile`.



## Training GPT-3
Main directory: train_scripts

#### Train 126M Parameter Model:
First, modify the conf/training/*.yaml file for the model you want to run.
Maake sure all the paths are set correctly by replacing the ??? symbols with
the right paths. Make sure the correct yaml file is selected in the
conf/config.yaml file, for the training parameter.

To train the 126M model after modifying the yaml file:
```
cd bignlp-scripts/train_scripts
python3 train_model.py
```


## Download the Test Data

#### LAMBADA Dataset:
To download the LAMBADA test dataset do:
```
cd bignlp-scripts/prepare_dataset
```


## Evaluating GPT-3
Main directory: eval_scripts

#### Evaluate 126M Parameter Model on LAMBADA:
To evaluate the 126M model do:
```
cd bignlp-scripts/eval_scripts
sbatch eval
```

## Benchmark multinode inference
(Only tested on selene)

```
cd bignlp-scripts/infer_scripts
bash multi_node_infer.sh
```
