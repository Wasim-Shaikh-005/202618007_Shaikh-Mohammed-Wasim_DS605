# Lab 07 - PCA, Eigenfaces and Face Recognition
---


**Name:** Shaikh Mohammed Wasim  
**Student ID:** 202618007  
**Course:** Fundamentals of Machine Learning (DS605)


---
**Dataset:** [AT&T Database of Faces (ORL)](https://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html)

## Dataset

- Total images: **400**
- Subjects: **40**
- Images per subject: **10**
- Image dimensions: **112 × 92** grayscale
- Original features per image: **10,304**
- Train/test split: **80/20**, stratified by subject
- Training images: **320**
- Test images: **80**
- Random state: **42**

## Part A — Image Representation

Images were loaded as grayscale matrices and flattened into 10,304-dimensional feature vectors. Subject labels were extracted from the directory names. A reproducible stratified train-test split ensured that every subject appeared in both sets.

## Part B — PCA, Eigenfaces and Compression

PCA was implemented using **NumPy linear algebra**, without `sklearn.decomposition.PCA`.

- Computed the mean training face and centered the data.
- Compared covariance eigendecomposition using the dual covariance matrix with SVD.
- Both methods produced matching leading eigenvalues.
- **98 principal components** retained **90.06%** of the training variance.
- Visualized the first 10 eigenfaces.
- Reconstructed test faces from their PCA representations.

### Reconstruction and Compression Results

| Metric | Result |
|---|---:|
| PCA components | 98 |
| Explained variance retained | 90.06% |
| Reconstruction MSE | 329.9830 |
| Reconstruction RMSE | 18.1654 |
| Original features per image | 10,304 |
| Reduced features per image | 98 |
| Feature-count reduction | 99.05% |
| Original float64 storage per image | 82,432 bytes |
| PCA score storage per image | 784 bytes |
| Score-only storage ratio | 105.14× |

The storage ratio compares pixel values with PCA scores only. It excludes the shared mean face and PCA basis required for reconstruction.

## Part C — Face Recognition

Nearest-neighbor matching used Euclidean distance to identify the closest stored training face.

| Method | Features per image | Correct predictions | Accuracy |
|---|---:|---:|---:|
| Raw pixels + 1-NN | 10,304 | 76/80 | 95.00% |
| PCA (98 components) + 1-NN | 98 | 76/80 | 95.00% |

PCA reduced the feature count by **99.05%** while achieving the same recognition accuracy as raw-pixel matching on this test split.

## Part D — Traditional Machine-Learning Classifiers

KNN, SVM (RBF), and Logistic Regression were trained using standardized PCA features. Component counts of 20, 50, 98, 150, and 200 were evaluated.

### Best Observed Results

| Components | Classifier | Correct predictions | Accuracy |
|---:|---|---:|---:|
| 50 | Logistic Regression | 79/80 | **98.75%** |
| 50 | SVM (RBF) | 78/80 | 97.50% |
| 20 | SVM (RBF) | 77/80 | 96.25% |
| 98 | SVM (RBF) | 76/80 | 95.00% |
| 98 | Logistic Regression | 76/80 | 95.00% |

### Observations

- Logistic Regression achieved the highest observed accuracy: **98.75% with 50 components**.
- SVM with an RBF kernel achieved **97.50% with 50 components**.
- PCA-based nearest-neighbor matching matched raw-pixel matching at **95.00% accuracy**, using far fewer features.
- The component count that preserves 90% variance is not necessarily the one that maximizes classification accuracy.

**Evaluation note:** Results are from one stratified 80/20 train-test split. Classifier settings and component counts were compared using test accuracy, so the best observed score is exploratory rather than an unbiased estimate of generalization performance. Cross-validation on the training set would provide a more reliable basis for model selection.