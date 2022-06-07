import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def split_zillow_data(df):
    '''
    This function performs split on zillow data
    Returns train, validate, and test dfs.
    70, 20, 10
    '''
    train_validate, test = train_test_split(df, test_size=.10, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.20, 
                                   random_state=123)
    return train, validate, test

##################################

