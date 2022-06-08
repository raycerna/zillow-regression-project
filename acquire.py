'''
Functions to acquire data for Zillow clustering model.
Seperate functions to connect to sql database and save data to csv.
Login credentials in env file are required.
'''

# IMPORTS
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from env import host, username, password


# SQL CONNECTION
def get_db_url(db_name):

    '''
    Connect to the SQL database with credentials stored in env file.
    Function parameter is the name of the database to connect to.
    Returns url.
    '''
    
    # Creates the url and the function returns this url
    url = f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
    return (url)


# ACQUIRE
def get_zillow_data():

    '''
    Connect to SQL Database with url function called within this function.
    Checks if database is already saved to computer in csv file.
    If no file found, saves to a csv file and assigns database to df variable.
    If file found, just assigns database to df variable.
    '''
    
    # data_name allows the function to work no matter what a user might have saved their file name as
    # First, we check if the data is already stored in the computer
    # First conditional runs if the data is not already stored in the computer
    if os.path.isfile('zillow.csv') == False:

        # Querry selects the whole predicstion_2017 table from the database
        sql = '''
                        SELECT bedroomcnt AS bedrooms, bathroomcnt AS bathrooms, `calculatedfinishedsquarefeet` AS square_feet,  
                        `lotsizesquarefeet` AS lot_size, poolcnt AS pool, `regionidzip` AS zip_code, yearbuilt AS year_built, latitude, 
                        longitude, fips, `taxvaluedollarcnt` AS assessed_value, `taxamount` AS tax_value, transactiondate AS transaction_date, logerror as log_error
                        FROM properties_2017
                        JOIN predictions_2017 USING (id)
                        WHERE propertylandusetypeid = 261 AND bedroomcnt > 0 AND bathroomcnt > 0
                        AND transactiondate >= '2017-01-01' AND transactiondate <= '2017-12-31'
                        '''

        # Connecting to the data base and using the query above to select the data
        # the pandas read_sql function reads the query into a DataFrame
        df = pd.read_sql(sql, get_db_url('zillow'))

        # The pandas to_csv function writes the data frame to a csv file
        # This allows data to be stored locally for quicker exploration and manipulation
        df.to_csv('zillow.csv')

    # This conditional runs if the data has already been saved as a csv (if the function has already been run on your computer)
    else:
        # Reads the csv saved from above, and assigns to the df variable
        df = pd.read_csv('zillow.csv', index_col=0)

    return df
