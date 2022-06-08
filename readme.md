# Predicting propery tax assessed values of Single Family Properties

- project description with goals

    The goal of this project is to find the key drivers of property tax value for single family properties that had a transaction in 2017. The scenario is that a Zillow Data Science Team has a model ready, but they are looking for insights that can help improve it. This project will give recommendations on a way to make a better model. It will also give me an opportunity to practice the data science pipeline to include Acquire, Prepare, Exploring, and Modeling.


- initial hypotheses:

#### 𝐻0 there is no relationship between tax values and number of bedrooms, bathrooms and square_feet
#### 𝐻𝑎: There is a relationship between tax values and number of bedrooms, bathrooms and square_feet

- data dictionary (only features used in exploration):

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


- project planning:
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
    - Determined my baseline prediciton at 73%.
    - Trained on three different classification models.
        - Logistic Regression
        - Random Forest
        - K-Nearest Neighbors
    - Validated on two since they were nearly identical.
        - KNN and Random Forest
    - Chose Random Forest for Test model after highest accuracy on validate.

## instructions on how to reproduce this project and findings

- Copy the acquire.py, prepare.py, and telco_analysis.ipynb
- Run telco_analysis.ipynb then further explore or reprepare data to your liking.

## key findings, recommendations, and takeaways from project

- It is evident that contract type is the highest indicator for customers to churn. My suggestion would be to offer a discount for subscribing to a one-year thus showing the customer they would save money in the long run.
- There is currently no option to bundle packages for internet service to include online_security, device_protection, and tech_support. It was evident that if a customer did not have one of these they were more likely to churn. My suggestion would be to bundle all these together at a discounted rate.
- Our best performing model obtained an accuracy of 76% ~3% higher than baseline.

*** NOTE: With more time we can determine the amount of revenue we can increase with my recommendations.

instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on their own?)

key findings, recommendations, and takeaways from your project.