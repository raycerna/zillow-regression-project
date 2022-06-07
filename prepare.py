import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn import metrics
import acquire

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def split_zillow_data(df):
    '''
    This function performs split on zillow data
    Returns train, validate, and test dfs.
    70, 20, 10
    '''
    train_validate, test = train_test_split(df, test_size=.10, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.20, random_state=123)
    return train, validate, test

##################################

def handle_na(df):    
    # filling n/a's with zero on columns with n/a's
    df = df.dropna(subset=['square_feet', 'lot_size', 'pool', 'zip_code', 'year_built', 'assessed_value', 'tax_value'])
    df = df.fillna(0)
    return df

def optimize_types(df):
    df["bedrooms"] = df["bedrooms"].astype(int)
    df["square_feet"] = df["square_feet"].astype(int)
    df["lot_size"] = df["lot_size"].astype(int)
    df["pool"] = df["pool"].astype(int)
    df["zip_code"] = df["zip_code"].astype(int)
    df["year_built"] = df["year_built"].astype(int)
    df["fips"] = df["fips"].astype(int)
    df["assessed_value"] = df["assessed_value"].astype(int)
    df["tax_value"] = df["tax_value"].astype(int)
    return df

def handle_outliers(df):
    """Manually handle outliers that only include the following"""
    df = df[df.bathrooms <= 6]
    df = df[df.bedrooms <= 6]
    df = df[df.square_feet <= 3000]
    return df

def add_months(df):
    df['transaction_date'] = df.transaction_date.astype('str')
    df['transaction_month'] = df.transaction_date.str.split('-',expand=True)[1]
    return df     

def prep_zillow(df):
    """
    Acquires Zillow data
    Handles nulls
    optimizes or fixes data types
    handles outliers w/ manual logic
    returns a clean dataframe
    """
    df = acquire.get_zillow_data()

    df = handle_na(df)

    df = optimize_types(df)

    df = handle_outliers(df)

    df = add_months(df)

    df.to_csv("zillow.csv", index=False)

    return df
