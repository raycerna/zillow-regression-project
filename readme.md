# Predicting property tax assessed values of Single Family Properties

## project description with goals

#### The goal of this project is to find the key drivers of property tax value for single family properties that had a transaction in 2017. The scenario is that a Zillow Data Science Team has a model ready, but they are looking for insights that can help improve it. This project will give recommendations on a way to make a better model. It will also give me an opportunity to practice the data science pipeline to include Acquire, Prepare, Exploring, and Modeling.


## initial hypotheses:

#### 𝐻0 there is no relationship between tax values and number of bedrooms, bathrooms and square_feet
#### 𝐻𝑎: There is a relationship between tax values and number of bedrooms, bathrooms and square_feet

## data dictionary (only features used in exploration):

| Feature                       | Definition                               
|-------------------------------|------------------------------------------------------------|
|'bathroomcnt'                  | Number of bathrooms in home including fractional bathrooms |
|'bedroomcnt'                   | Number of bedrooms in home                                 |           
|'calculatedfinishedsquarefeet' | Calculated total finished living area of the home          |
|'fips'                         | Federal Information Processing Standard code               |
|'latitude'                     | Latitude coordinates of the middle of the parcel           |
|'longitude'                    | Longitude coordinates of the middle of the parcel          |
|'lotsizesquarefeet'            | Area of the lot in square feet                             |
|'parcelid'                     | Unique identifier for parcels (lots)                       |
|'poolcnt'                      | Number of pools on the lot (if any)                        |
|'regionidzip'                  | Zip code in which the property is located                  |
|'yearbuilt'                    | The Year the principal residence was built                 |
|'taxvaluedollarcnt'            |The total tax assessed value of the parcel                  |
|'taxamount'                    |The total property tax assessed for that assessment year    |


## project planning:
- Acquire
    - Acquired data using SQL from the zillow database.
        - Note: Functions to acquire data are built into the acquire.py file.
        - Loaded and inspected dataset.
        - prepared some of the features from import of SQL instead of in prepare steps.

- Prepare (can be viewed in prepare.py file)
    - filled N/As and missing data with Zero (0) [square_feet', 'lot_size', 'pool', 'zip_code', 'year_built', 'tax_value', 'tax_amount']
    - Coverted "bedrooms" to astype(int), "square_feet" to astype(int), "lot_size" to astype(int), "pool" to astype(int), "zip_code" to astype(int), "year_built" to astype(int), "fips" to astype
    (int), "tax_value" to astype(int), "tax_amount" to astype(int).
    - filtered data down to smaller subset to include: bathrooms <= 6, bedrooms <= 6, square_feet <= 3000, tax_value <= 1000000. This was over 90% of the data.
    - Added an additional "Month" feature which split the month from the transaction_date.
    - Labeled the three fips that were included by county: Los Angeles, Ventura, Orange.
    - Added 'tax_rate' feature which is tax_amount/tax_value).
    - Added these functions to one def to use when bringing in data to notebook.

- Explore
    - Performed univariate analysis on individual predictors of tax_value.
    - Performed bivariate and multivariate exploration on several features to find recommendations that drive tax_value.
    - Further explored features that I questioned in my initial hypothesis.
    - Visualized features of tax_amount by using countplots and stackedplots and kdeplots.

- Model
    - Train, validated, and tested the predictors/independent features.
    - Determined my baseline prediciton.
    - Trained on classification models:
        - Logistic Regression

## instructions on how to reproduce this project and findings

- Download acquire.py module and use it to acquire the data. Requires credentials to access the zillow database.
- Download prepare.py module and use its functions to prepare the data.
- Explore on your own.

## key findings, recommendations, and takeaways from project

- Drivers of the property value are:
    - Square_feet of home
    - Number of bathhrooms
    - Number of bedrooms
    - County the property is located
        - The average property value in LA County is significantly lower than Orange and Ventura County
