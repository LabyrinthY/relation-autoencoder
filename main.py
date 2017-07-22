import os, sys, inspect
from definitions import settings
from processing import OiePreprocessor


def creat_dataset():
    for dataset_name in ["train", "dev", "test"]:
        command = "python -m processing.OiePreprocessor --batch-name {} {} {}".format(
                dataset_name, settings.raw_data_dir[dataset_name], settings.data_input)

        print command
        os.system(command)

def learn():
    command = "python -m learning.OieInduction --pickled_dataset {} --model_name discrete-autoencoder --model AC --optimization 1 --epochs 10 --batch_size 100 --relations_number 10 --negative_samples_number 5 --l2_regularization 0.1 --alpha 0.1 --seed 2 --embed_size 10 --learning_rate 0.1".format(settings.data_input)

    print command
    os.system(command)



if __name__ == "__main__":
    #creat_dataset()
    learn()
