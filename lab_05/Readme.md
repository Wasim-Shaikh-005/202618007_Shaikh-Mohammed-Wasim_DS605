## Lab 05 : Machine Learning with Scikit-learn and From Scratch

**Dataset:** UCI Productivity Prediction of Garment Employees

---

**Name:** Shaikh Mohammed Wasim  
**Student ID:** 202618007  
**Course:** Fundamentals of Machine Learning (DS605)

---

## Objective

Implement regression and classification using:

- Scikit-learn
- NumPy + Pandas from scratch

The same train-test split is used for both implementations.

### Tasks

- Regression: predict `actual_productivity`
- Classification: predict `MeetsTarget`
- Compare performance and execution time
- Perform basic feature engineering and optimization

---

## Dataset

- Samples: **1197**
- Original features: **15**
- Train samples: **957**
- Test samples: **240**
- Train-test split: **80/20**
- Random state: **42**

### Classification Target

`MeetsTarget = 1` if:

`actual_productivity >= targeted_productivity`

Otherwise:

`MeetsTarget = 0`

`actual_productivity` is not used as an input feature for classification.

---

# Part A — Scikit-learn

## Preprocessing

- Median imputation for missing `wip`
- StandardScaler for numerical features
- OneHotEncoder for categorical features
- `date` excluded from the model
- `over_time` replaced by `overtime_per_worker`

### Regression

Model: `LinearRegression`

| Metric | Score |
|---|---:|
| MAE | **0.110717** |
| RMSE | **0.149154** |
| R² | **0.162147** |

### Classification

Model: `LogisticRegression`

| Metric | Score |
|---|---:|
| Accuracy | **0.770833** |
| Precision | **0.799020** |
| Recall | **0.920904** |
| F1-score | **0.855643** |

---

# Part B — From Scratch

Implemented using only **NumPy and Pandas**.

### Implemented

- Missing-value handling
- One-hot encoding
- Feature scaling
- Linear Regression
- Logistic Regression
- Sigmoid function
- Gradient descent
- Prediction
- MAE
- RMSE
- R²
- Accuracy
- Precision
- Recall
- F1-score

### Regression

| Implementation | MAE | RMSE | R² |
|---|---:|---:|---:|
| Scikit-learn | 0.110717 | 0.149154 | 0.162147 |
| Manual | 0.110717 | 0.149154 | 0.162147 |

### Classification

| Implementation | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Scikit-learn | 0.770833 | 0.799020 | 0.920904 | 0.855643 |
| Manual | 0.766667 | 0.776256 | 0.960452 | 0.858586 |

---

# Execution Time

| Model | Implementation | Training Time (s) | Prediction Time (s) |
|---|---|---:|---:|
| Linear Regression | Scikit-learn | 0.009663 | 0.000051 |
| Linear Regression | Manual | 0.008883 | 0.000051 |
| Logistic Regression | Scikit-learn | 0.019332 | 0.003746 |
| Logistic Regression | Manual | 0.203106 | 0.000084 |

---

# Feature Engineering

### Overtime per Worker

Replaced:

`over_time`

with:

`overtime_per_worker = over_time / no_of_workers`

This produced a modest improvement over the original baseline.

### WIP Log Transformation

Tested:

`log1p(wip)`

Result: no meaningful improvement.

### Style Change as Categorical

Tested `no_of_style_change` as categorical.

Result: slight classification improvement in the manual model, but regression performance decreased. The numerical representation was therefore retained.

---

# Key Results

- Manual Linear Regression reproduced the Scikit-learn results.
- Manual Logistic Regression produced similar but not identical results due to the custom gradient-descent implementation.
- Overtime-per-worker was the most useful tested feature-engineering change.
- Current regression performance: **R² = 0.1621**
- Current classification performance: **F1 = 0.8556**
- Further optimization can be performed later using feature interactions, regularization, feature selection, and improved optimization.

---

## Technologies

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook
