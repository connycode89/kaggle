# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 16:21:08 2018

@author: cdonovan
"""

import os
import pandas as pd
import numpy as np

dir1 = 'C:\\MyWorkingFolder\\Github Repositories\\kaggle\\Toxic Comments\\'
dir_conts = os.listdir(dir1)

data_dict = {}
for item in filter(lambda x:'.csv' in x, dir_conts):
    data_dict[item.replace('.csv.zip','')] = pd.read_csv(dir1+item)

sample, test, train = (data_dict[item] for item in data_dict.keys())
del data_dict, dir_conts, item

# train data
num_cols = train[train.columns[2:]]
row_sums = np.sum(num_cols, axis=1)
worst = train.loc[np.argwhere(row_sums==np.amax(row_sums)).flatten()]
more_than1 = train.loc[row_sums[row_sums>1].index]
just_1 = train.loc[row_sums[row_sums==1].index]
none = train.loc[row_sums[row_sums==0].index]
