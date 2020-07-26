import pandas as pd
from random import random


def run():
    # Load dataset and output sample
    data = pd.read_csv("/data/filtered_train_data.csv", header=0)
    output = pd.read_csv("/data/filtered_sample_output.csv", header=0)

    ##################### Your code goes here #####################
    for i, row in output.iterrows():
        if random() > 0.5:
            row[int(random() * row.size)] = 1
    ###############################################################

    # Save the result in the appropriate path
    output.to_csv('/result/result.csv', index=False)


if __name__ == '__main__':
    run()
