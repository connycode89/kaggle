# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 10:14:59 2018

@author: cdonovan
"""

import os
dir1 = 'C:\\MyWorkingFolder\\Github Repositories\\kaggle\\Toxic Comments\\'
os.chdir(dir1+'Code')
from read_data import *

# train data
num_cols = train[train.columns[2:]]
row_sums = np.sum(num_cols, axis=1)
worst = train.loc[np.argwhere(row_sums==np.amax(row_sums)).flatten()]
more_than1 = train.loc[row_sums[row_sums>1].index]
just_1 = train.loc[row_sums[row_sums==1].index]
none = train.loc[row_sums[row_sums==0].index]

col_sums = np.sum(num_cols, axis=0)

