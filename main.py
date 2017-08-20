import os, sys, inspect
import time
import argparse
from definitions import settings
from processing import OiePreprocessor

def find_aviliable_fliename(name):
    """Get file or dir name that not exists yet"""
    file_name, file_extension = os.path.splitext(name)
    i = 0
    while True:
        tmp = "{}_{:03d}_{}".format(file_name, i, file_extension)
        if not os.path.exists(tmp):
            break
        i+=1
    return tmp

def creat_dataset(threshold):
    for dataset_name in ["train", "dev", "test"]:
        command = "python -m processing.OiePreprocessor --batch-name {} {} {} --threshold {}".format(
                dataset_name, settings.raw_data_dir[dataset_name], settings.data_input(threshold), threshold)

        print command
        os.system(command)

def learn(threshold):
    model_name = find_aviliable_fliename(os.path.join(settings.models_path, "m_{}".format(threshold)))
    command = "python -m learning.OieInduction --pickled_dataset {} --model_name {} --model AC --optimization 1 --epochs 6 --batch_size 100 --relations_number 100 --negative_samples_number 20 --l2_regularization 0.1 --alpha 0.1 --seed {} --embed_size 30 --learning_rate 0.1".format(settings.data_input(threshold), model_name, int(time.time()))
    command = "python -m learning.OieInduction --pickled_dataset {} --model_name {} --model A --optimization 1 --epochs 6 --batch_size 100 --relations_number 100 --negative_samples_number 20 --l2_regularization 0.1 --alpha 0.25 --seed {} --embed_size 30 --learning_rate 0.1".format(settings.data_input(threshold), model_name, int(time.time()))

    #command = "python -m learning.OieInduction --pickled_dataset {} --model_name {} --model C --optimization 1 --epochs 6 --batch_size 100 --relations_number 100 --negative_samples_number 20 --l2_regularization 0.1 --alpha 0.05 --seed {} --embed_size 30 --learning_rate 0.1".format(settings.data_input(threshold), model_name, int(time.time()))
    print command
    os.system(command)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=int, default=-1)

    opts,_ = parser.parse_known_args(sys.argv)
    threshold = opts.threshold

#    creat_dataset(threshold)
    learn(threshold)
