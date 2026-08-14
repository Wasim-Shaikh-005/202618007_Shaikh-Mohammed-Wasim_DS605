# Lab 2 – NumPy and Pandas

## Student Information

- **Name:** Shaikh Mohammed Wasim
- **Student ID:** 202618007
- **Course:** Fundamentals of Machine Learning
- **Lab Assignment:** Lab 2 – Vectorized Programming with NumPy & Data Wrangling with Pandas

---

## Dataset

**Dataset Name:** Titanic Training Dataset (`train.csv`)

The dataset contains passenger information from the Titanic, including demographic details, ticket information, fare, passenger class, and survival status. It is used for practicing data manipulation, filtering, aggregation, feature engineering, and visualization using Pandas and NumPy.

---

## Project Details


### Part A – NumPy

The following concepts were implemented using vectorized NumPy operations:

- Random array generation with reproducible seed
- Statistical measures (mean, median, min, max, standard deviation)
- Array creation using `arange()`, `zeros()`, `ones()`, and `linspace()`
- 2D and 3D array indexing and slicing
- Reshaping and flattening arrays
- Matrix addition, element-wise multiplication, and matrix multiplication
- Transpose, determinant, inverse, and verification using `np.allclose()`
- Normal distribution generation and histogram visualization

### Part B – Pandas (Titanic Dataset)

The following operations were performed:

- Data loading and inspection
- Row and column selection using `loc` and `iloc`
- Boolean filtering and querying
- GroupBy aggregation and survival analysis
- Missing value analysis and imputation
- Fare outlier detection using the IQR method
- Feature engineering (`FamilySize` and `IsAlone`)
- Pivot table creation
- Correlation heatmap and other visualizations

---

## Key Observations

1. Female passengers had a significantly higher survival rate than male passengers.
2. First-class passengers showed the highest probability of survival.
3. Passenger class and fare were positively associated with survival outcomes.
4. The **Age** and **Cabin** columns contained the largest number of missing values.
5. Filling missing ages with the mean removed all missing values from the Age column.
6. The Fare column contained several high-value outliers identified using the IQR method.
7. Family-related features provided additional insight into passenger survival patterns.


