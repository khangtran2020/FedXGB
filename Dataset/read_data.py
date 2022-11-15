import os
import pandas as pd
import numpy as pd

def read_clients(args):
    bank_data = {}
    for i in range(args.num_bank):
        bank_data['bank_{}'.format(i)] = {}

    for i in range(args.num_bank):
        path = os.path.join(args.data_path, 'bank_{}'.format(i))
        train_df, test_df = read_client(path=path)
        bank_data['bank_{}'.format(i)]['train'] = train_df
        bank_data['bank_{}'.format(i)]['test'] = test_df
    return bank_data

def read_client(path):
    train_df = None
    test_df = None
    for f in os.listdir(path):
        temp = pd.read_csv('{}/{}'.format(path, f))
        if ('test' not in f):
            if type(train_df) == 'NoneType':
                train_df = temp
            else:
                train_df = pd.concat([train_df, temp], axis=0).reset_index(drop=True)
        else:
            if type(test_df) == 'NoneType':
                test_df = temp
            else:
                test_df = pd.concat([test_df, temp], axis=0).reset_index(drop=True)
    return train_df, test_df

