import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn.preprocessing
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
    df = df.dropna(subset=['square_feet', 'lot_size', 'pool', 'zip_code', 'year_built', 'tax_value', 'tax_amount'])
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
    df["tax_value"] = df["tax_value"].astype(int)
    df["tax_amount"] = df["tax_amount"].astype(int)
    return df

def handle_outliers(df):
    """Manually handle outliers that only include the following"""
    df = df[df.bathrooms <= 6]
    df = df[df.bedrooms <= 6]
    df = df[df.square_feet <= 3000]
    df = df[df.tax_value <= 1000000]
    return df

def add_months(df):
    df['transaction_date'] = df.transaction_date.astype('str')
    df['transaction_month'] = df.transaction_date.str.split('-',expand=True)[1]
    return df     

def add_county(df):
    df['county'] = np.where(df.fips == 6037, 'Los Angeles', np.where(df.fips == 6059, 'Orange','Ventura') )
    #df = df.drop(columns = ‘fips’)
    
    #fips = pd.DataFrame({
    #'fips': [6037, 6059, 6111],
    #'County':['Los Angles', 'Orange', 'Ventura']})
    return df

def add_tax_rate(df):
     df['tax_rate'] = (df.tax_amount/df.tax_value) * 100
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

    df = add_county(df)

    df = add_tax_rate(df)

    #df.to_csv("zillow.csv", index=False)

    return df

def scale_data(train, validate, test):

    columns_to_scale = ['tax_amount','tax_value','bathrooms','bedrooms','square_feet','lot_size']
    
    # 1. Create the Scaling Object
    scaler = sklearn.preprocessing.StandardScaler()

    # 2. Fit to the train data only
    scaler.fit(train[columns_to_scale])

    # 3. use the object on the whole df
    # this returns an array, so we convert to df in the same line
    train_scaled = pd.DataFrame(scaler.transform(train[columns_to_scale]))
    validate_scaled = pd.DataFrame(scaler.transform(validate[columns_to_scale]))
    test_scaled = pd.DataFrame(scaler.transform(test[columns_to_scale]))

    # the result of changing an array to a df resets the index and columns
    # for each train, validate, and test, we change the index and columns back to original values

    # Train
    train_scaled.index = train[columns_to_scale].index
    train_scaled.columns = train[columns_to_scale].columns

    # Validate
    validate_scaled.index = validate[columns_to_scale].index
    validate_scaled.columns = validate[columns_to_scale].columns

    # Test
    test_scaled.index = test[columns_to_scale].index
    test_scaled.columns = test[columns_to_scale].columns

    return train_scaled, validate_scaled, test_scaled

def percentage_stacked_plot(columns_to_plot, title, df):
    
    '''
    Returns a 100% stacked plot of the response variable for independent variable of the list columns_to_plot.
    Parameters: columns_to_plot (list of string): Names of the variables to plot
    '''
    
    number_of_columns = 2
    number_of_rows = math.ceil(len(columns_to_plot)/2)

    # create a figure
    fig = plt.figure(figsize=(12, 5 * number_of_rows)) 
    fig.suptitle(title, fontsize=22,  y=.95)
 

    # loop to each column name to create a subplot
    for index, column in enumerate(columns_to_plot, 1):

        # create the subplot
        ax = fig.add_subplot(number_of_rows, number_of_columns, index)

        # calculate the percentage of observations of the response variable for each group of the independent variable
        # 100% stacked bar plot
        prop_by_independent = pd.crosstab(df[column], df['tax_value']).apply(lambda x: x/x.sum()*100, axis=1)

        prop_by_independent.plot(kind='bar', ax=ax, stacked=True,
                                 rot=0, color=['#94bad4','#ebb086'])

        # set the legend in the upper right corner
        ax.legend(loc="upper right", bbox_to_anchor=(0.62, 0.5, 0.5, 0.5),
                  title='Tax Value', fancybox=True)

        # eliminate the frame from the plot
        spine_names = ('top', 'right', 'bottom', 'left')
        for spine_name in spine_names:
            ax.spines[spine_name].set_visible(False)

    return percentage_stacked_plot