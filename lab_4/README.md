# Lab 4 : End-to-End Machine Learning Project: Airbnb Price Prediction

**Name:** Shaikh Mohammed Wasim  
**Student ID:** 202618007  
**Project:** [Airbnb Price Prediction — Streamlit App](https://202618007shaikh-mohammed-wasimds605-oty899wsgqgrhklxmjiuru.streamlit.app/)  
**Course:** Fundamentals of Machine Learning (DS605)

## Project Overview

This project focuses on predicting the nightly price of Airbnb listings using machine learning. The project follows an end-to-end machine learning workflow, starting with exploratory data analysis and data preprocessing and ending with a trained model that can be used through a Streamlit web application.

The main objective is to understand the factors that influence Airbnb prices and build a regression model that can estimate the price of a new listing.

---

## Dataset

The project uses the **New York City Airbnb Open Data (2019)** dataset.

The dataset contains information about Airbnb listings such as:

* Listing location
* Neighbourhood
* Room type
* Minimum number of nights
* Number of reviews
* Reviews per month
* Host listing count
* Availability
* Price

The original dataset contains **48,895 listings and 16 columns**.

Dataset file:

```text
AB_NYC_2019.csv
```

---

## Project Workflow

The project was completed in the following stages:

1. Exploratory Data Analysis
2. Data Cleaning
3. Feature Engineering
4. Feature Selection
5. Data Preprocessing
6. Model Training
7. Model Comparison
8. Model Evaluation
9. Overfitting Analysis
10. Saving the Final Model
11. Streamlit Application

---

## 1. Exploratory Data Analysis

The dataset was first examined to understand its structure and identify possible problems.

The analysis included:

* Dataset shape and data types
* Descriptive statistics
* Missing-value analysis
* Duplicate-value analysis
* Price distribution
* Price outlier analysis
* Average price by room type
* Average price by neighbourhood group
* Correlation between numerical features and price
* Relationship between location and price
* Relationship between reviews and price

### Important observations

The price distribution is strongly right-skewed. Most listings have relatively moderate prices, while a small number of listings have very high prices.

Room type and location also show noticeable differences in average listing prices. Entire homes/apartments generally have higher prices than private or shared rooms, while prices also vary considerably between neighbourhood groups.

---

## 2. Data Cleaning

The following cleaning steps were performed:

### Zero-price listings

Listings with a price of zero were removed because a zero nightly price is not meaningful for the prediction task.

### Extreme prices

The upper 0.5% of prices were removed using the 99.5th percentile as the cutoff.

This was done because a small number of extremely expensive listings can have a large influence on a regression model.

The cutoff was calculated directly from the dataset rather than using a fixed value.

### Missing values

Missing numerical values are handled using median imputation.

Categorical missing values are handled using the most frequent category.

This preprocessing is included inside the machine learning pipeline so that the same transformations are applied when predicting new listings.

---

## 3. Feature Engineering

A `has_review` feature was created from the `reviews_per_month` column.

It indicates whether a listing has review history:

```text
1 → Review history available
0 → No review history
```

This allows the model to capture information contained in the missingness of the review data.

---

## 4. Features Used

The following features were selected for prediction:

```text
neighbourhood_group
neighbourhood
latitude
longitude
room_type
minimum_nights
number_of_reviews
reviews_per_month
calculated_host_listings_count
availability_365
has_review
```

Features such as listing ID, host ID, host name, listing name and the raw last-review date were not used because they were not considered useful generalizable predictors for this application.

---

## 5. Preprocessing

The preprocessing workflow uses a `ColumnTransformer`.

### Numerical features

Numerical features are:

* Filled using median imputation
* Standardized using `StandardScaler`

### Categorical features

Categorical features are:

* Filled using the most frequent category
* Converted to numerical values using one-hot encoding

`handle_unknown="ignore"` is used in the encoder so that the model can handle previously unseen categories when making predictions on new listings.

---

## 6. Target Transformation

Airbnb prices have a highly skewed distribution.

Therefore, the model is trained using:

```python
np.log1p(price)
```

The predictions are converted back to the original price scale using:

```python
np.expm1(prediction)
```

This reduces the influence of very large prices during model training.

---

## 7. Model

The main regression model used in the current implementation is a **Random Forest Regressor**.

The model uses:

```text
n_estimators = 100
min_samples_leaf = 2
max_features = 0.8
random_state = 42
```

The complete preprocessing and model are stored together in a single scikit-learn pipeline.

---

## 8. Model Evaluation

The data was divided into:

```text
80% → Training data
20% → Testing data
```

A fixed random state of 42 was used to make the experiment reproducible.

### Final Model Results

| Metric | Training | Testing |
| ------ | -------: | ------: |
| R²     |   0.7712 |  0.4529 |
| RMSE   |   $55.66 |  $87.37 |

The test MAE for the final model is approximately:

```text
$45.30
```

### Interpretation

The model achieved an R² of approximately **0.45 on the test set**, meaning that it explains a meaningful portion of the variation in Airbnb prices on unseen data.

The difference between the training R² (0.77) and testing R² (0.45) indicates some overfitting. The higher test RMSE also supports this observation.

However, Airbnb pricing depends on many factors that are not present in this dataset, so some prediction error is expected.

---

## 9. Model Limitations

There are several limitations to this model.

* The dataset contains NYC Airbnb listings from **2019**, so the predictions should not be interpreted as current market prices.
* Important factors such as amenities, property size, number of bedrooms, cleaning fees and seasonal demand are not included.
* The model is trained only on NYC listings.
* Extremely high-priced listings were removed during preprocessing.
* The model may perform worse for listing types or neighbourhoods that are poorly represented in the training data.
* The train/test performance gap indicates some degree of overfitting.

---

## 10. Saved Model

The trained preprocessing and prediction pipeline is saved as:

```text
airbnb_price_pipeline.joblib
```

Using a saved pipeline ensures that new inputs go through the same preprocessing steps used during training.

---

## 11. Streamlit Application

A Streamlit application was created to make the model easier to use.

The application accepts information such as:

* Neighbourhood group
* Neighbourhood
* Latitude
* Longitude
* Room type
* Minimum nights
* Number of reviews
* Reviews per month
* Host listing count
* Availability

It then returns an estimated nightly Airbnb price.

### Run the application locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

The application will open in the browser.

---

## 12. Project Structure

```text
airbnb-price-prediction/
│
├── Airbnb_Price_Prediction.ipynb
├── app.py
├── airbnb_price_pipeline.joblib
├── model_comparison.csv
├── requirements.txt
├── README.md
│
└── plots/
    ├── price_distribution.png
    ├── actual_vs_predicted.png
    └── residuals.png
```

---

## 13. Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

---

## 14. Conclusion

This project demonstrates a complete machine learning workflow for Airbnb price prediction.

The dataset was explored and cleaned, relevant features were selected and engineered, numerical and categorical variables were preprocessed, and a Random Forest regression model was trained.

The final model achieved a test R² of approximately **0.453** and a test RMSE of approximately **$87.37**. Although there is some overfitting between the training and testing results, the model is able to capture several important patterns in Airbnb pricing.

The trained model was saved as a reusable pipeline and integrated into a Streamlit application for making predictions on new listing information.
