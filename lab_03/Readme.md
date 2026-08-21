# Lab 3: Scikit-learn Preprocessing and Model Evaluation

**Name:** Shaikh Mohammed Wasim  
**Student ID:** 202618007  
**Course:** Fundamentals of Machine Learning (Lab 3)

## Dataset

**Hotel Booking Demand (Kaggle)**

Dataset Link: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

---

## Preprocessing Choices

- Removed the `company` column due to very high missing values (>90%).
- Removed `reservation_status` and `reservation_status_date` to prevent data leakage.
- Removed extreme outliers using the IQR method.
- Split the dataset using `train_test_split(test_size=0.2, stratify=y, random_state=42)`.
- Used **KNNImputer (k=5)** for numerical missing values.
- Used **SimpleImputer (most frequent)** for categorical missing values.
- Applied **OneHotEncoder(handle_unknown="ignore")** to categorical features.
- Built two preprocessing pipelines:
  - **Pipeline A:** KNNImputer + StandardScaler
  - **Pipeline B:** KNNImputer + MinMaxScaler

---

## Models Used

1. Logistic Regression (`max_iter=1000`)
2. Decision Tree Classifier (`random_state=42`)

Each model was trained with both preprocessing pipelines, resulting in four experiments.

---

## Results Summary

| Model | Test Accuracy | F1-Score |
|--------|--------------:|---------:|
| Logistic + StandardScaler | 0.7838 | 0.7016 |
| Logistic + MinMaxScaler | 0.7831 | 0.7006 |
| Decision Tree + StandardScaler | 0.8298 | 0.7814 |
| **Decision Tree + MinMaxScaler** | **0.8302** | **0.7845** |

---

## Final Observations

- Decision Tree with **MinMaxScaler** achieved the best overall performance.
- StandardScaler provided a slight improvement over MinMaxScaler for Logistic Regression.
- Feature scaling had minimal effect on Decision Tree performance.
- Logistic Regression generalized better with a very small train–test accuracy gap.
- Decision Tree achieved higher accuracy but showed signs of overfitting due to its near-perfect training accuracy.
