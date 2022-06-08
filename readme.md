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

instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on their own?)

key findings, recommendations, and takeaways from your project.