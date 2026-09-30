# Lab 06 - Feature Extraction and Machine Learning with Image and Text Data
---

**Name:** Shaikh Mohammed Wasim  
**Student ID:** 202618007  
**Course:** Fundamentals of Machine Learning (DS605)


---
**Dataset:** [Asphalt Crack Dataset - 400 Images (Mendeley Data)](https://data.mendeley.com/datasets/xnzhj3x8v4/1)

- Total images: **400**
- Classes: **Crack / Non-Crack**
- Train/Test split: **80/20**
- Training images: **320**
- Test images: **80**
- Original image size: **448 × 448 × 3**
- Resized image size: **128 × 128**
- Grayscale conversion: **Yes**

## Part A — Baseline Representation

Each image was represented using 9 handcrafted features:

1. Mean brightness
2. Brightness standard deviation
3. Median intensity
4. Minimum intensity
5. Maximum intensity
6. Dark pixel ratio
7. Bright pixel ratio
8. Canny edge count
9. Canny edge density

Canny edge detection used thresholds:

```text
Low threshold  = 100
High threshold = 200
```

Features were standardized using `StandardScaler`, fitted only on the training set.

### Model

**Logistic Regression**

### Results

| Metric | Score |
|---|---:|
| Accuracy | **88.75%** |
| Precision | **89.74%** |
| Recall | **87.50%** |
| F1 Score | **88.61%** |

### Confusion Matrix

```text
                 Predicted
              Non-Crack  Crack
Actual
Non-Crack         36       4
Crack              5      35
```

- True Negatives: **36**
- False Positives: **4**
- False Negatives: **5**
- True Positives: **35**

Training time:

```text
0.008882701 seconds
```

Prediction time:

```text
0.000051023 seconds
```

---

## Part C — Improved Representation

The Canny edge detection thresholds were changed to make the representation more sensitive to weaker edges.

### Change

```text
Baseline:
Canny(100, 200)

Improved:
Canny(50, 150)
```

The number of features remained **9**, and the same train/test split and Logistic Regression model were used.

### Results

| Metric | Baseline | Improved |
|---|---:|---:|
| Accuracy | 88.75% | **90.00%** |
| Precision | 89.74% | **90.00%** |
| Recall | 87.50% | **90.00%** |
| F1 Score | 88.61% | **90.00%** |

### Confusion Matrix

```text
                 Predicted
              Non-Crack  Crack
Actual
Non-Crack         36       4
Crack              4      36
```

- True Negatives: **36**
- False Positives: **4**
- False Negatives: **4**
- True Positives: **36**

Training time:

```text
0.008384709 seconds
```

Prediction time:

```text
0.000356080 seconds
```

---

## Comparison

| Property | Baseline | Improved |
|---|---:|---:|
| Canny thresholds | 100, 200 | 50, 150 |
| Number of features | 9 | 9 |
| Accuracy | 88.75% | **90.00%** |
| Precision | 89.74% | **90.00%** |
| Recall | 87.50% | **90.00%** |
| F1 Score | 88.61% | **90.00%** |
| False Positives | 4 | 4 |
| False Negatives | 5 | **4** |

The threshold-tuned representation improved accuracy by **1.25 percentage points** and reduced false negatives from **5 to 4**, while keeping the number of features unchanged.
