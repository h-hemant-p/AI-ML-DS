##### **Outliers:**

Data points significantly different from most data in a dataset, appearing as unusually high or low values.

---

##### **Exploratory Data Analysis (EDA):** 

EDA is an approach in statistics and data science to analyze and summarize datasets to understand their main characteristics, patterns, and anomalies, often using visual and statistical techniques.

**Purpose**:

- Uncover patterns, trends, and relationships in data.
- Identify outliers, missing values, and inconsistencies.
- Test assumptions and guide further analysis or modeling.
- Generate hypotheses for deeper investigation.

**Key Steps in EDA**:

1. **Data Collection and Understanding**:
   - Gather data and understand its structure (e.g., variables, data types).
   - Check data source and context.
2. **Data Cleaning**:
   - Handle missing values (impute, remove, or flag).
   - Detect and address outliers (e.g., using IQR, lower/upper fences).
   - Correct inconsistencies (e.g., typos, formatting issues).
3. **Descriptive Statistics**:
   - **Central Tendency**: Mean, median, mode.
   - **Dispersion**: Range, variance, standard deviation, IQR.
   - **Distribution**: Skewness, kurtosis, quantiles (e.g., Q1, Q3).
4. **Visualization**:
   - **Univariate**: Histograms, box plots (for distribution, outliers).
   - **Bivariate**: Scatter plots, correlation matrices, heatmaps.
   - **Multivariate**: Pair plots, parallel coordinates.
5. **Correlation Analysis**:
   - Measure relationships between variables (e.g., Pearson, Spearman correlation).
   - Identify multicollinearity in features.
6. **Outlier Detection**:
   - Use statistical methods (e.g., Z-score, IQR: Lower Fence = Q1 - 1.5*IQR, Upper Fence = Q3 + 1.5*IQR).
   - Visualize with box plots or scatter plots.
7. **Data Transformation**:
   - Normalize/scale data for consistency.
   - Apply transformations (e.g., log, square root) to handle skewed data.

**Example**:

- Dataset: [5, 10, 15, 20, 25, 200]
- **Descriptive Stats**:
  - Mean = 45.83, Median = 17.5, IQR = 15 (Q1 = 7.5, Q3 = 22.5).
  - Outlier: 200 (above Upper Fence = 22.5 + 1.5*15 = 45).
- **Visualization**: Box plot shows 200 as an outlier; histogram reveals right skew.
- **Correlation**: If paired with another variable, use scatter plot to check relationships.

---

##### **Quantiles**

Quantiles are values that divide a dataset into equal-sized, ordered subgroups based on rank or probability. They describe the distribution of data by splitting it into intervals.

**Key Types**:

- **Quartiles**: Divide data into 4 equal parts (25% each).
  - Q1 (25th percentile): Lower quartile.
  - Q2 (50th percentile): Median.
  - Q3 (75th percentile): Upper quartile.
- **Percentiles**: Divide data into 100 equal parts (e.g., 90th percentile = top 10%).
- **Deciles**: Divide data into 10 equal parts.
- **Quintiles**: Divide data into 5 equal parts.

**Purpose**:

- Summarize data distribution.
- Identify spread, central tendency, and outliers (e.g., using IQR: Q3 - Q1).
- Compare data points (e.g., test scores in percentiles).

**Calculation**:

1. Sort data in ascending order.
2. Determine position: For the k-th quantile in n data points, use rank = k * (n-1)/q + 1 (q = number of quantiles, e.g., 4 for quartiles).
3. Interpolate if needed for non-integer ranks.

**Example**:

- Dataset: [5, 10, 15, 20, 25]
- Quartiles:
  - Q1 (25th): 7.5 (between 5 and 10).
  - Q2 (50th): 15 (median).
  - Q3 (75th): 22.5 (between 20 and 25).
- Outlier detection: Values < Q1 - 1.5*IQR or > Q3 + 1.5*IQR are outliers.

##### **Interquartile Range (IQR):** 

The IQR is a measure of statistical dispersion, representing the range between the first quartile (Q1, 25th percentile) and the third quartile (Q3, 75th percentile) in a dataset. It captures the middle 50% of the data.

**Formula**:
IQR = Q3 - Q1

**Example**:

- Dataset: [5, 10, 15, 20, 25]
- Q1 = 7.5 (median of [5, 10]).
- Q3 = 22.5 (median of [20, 25]).
- IQR = 22.5 - 7.5 = **15**.

**Outlier Detection**:

- Outliers are values < Q1 - 1.5*IQR or > Q3 + 1.5*IQR.
- Example: For IQR = 15, outliers are < 7.5 - 1.5*15 = -15 or > 22.5 + 1.5*15 = 45.


##### **Lower Fence and Upper Fence:** 

The lower fence and upper fence are thresholds used in statistics to identify outliers in a dataset, based on the interquartile range (IQR). They are calculated using the first quartile (Q1) and third quartile (Q3).

**Formulas**:

- **Lower Fence** = Q1 - 1.5 * IQR
- **Upper Fence** = Q3 + 1.5 * IQR
- **IQR** = Q3 - Q1 (Interquartile Range).

**Calculation**:

1. Sort data in ascending order.
2. Find Q1 (25th percentile, median of lower half) and Q3 (75th percentile, median of upper half).
3. Calculate IQR = Q3 - Q1.
4. Compute:
   - Lower Fence = Q1 - 1.5 * IQR
   - Upper Fence = Q3 + 1.5 * IQR

**Example**:

- Dataset: [5, 10, 15, 20, 25]
- Q1 = 7.5 (median of [5, 10]).
- Q3 = 22.5 (median of [20, 25]).
- IQR = 22.5 - 7.5 = 15.
- **Lower Fence** = 7.5 - 1.5 * 15 = 7.5 - 22.5 = **-15**.
- **Upper Fence** = 22.5 + 1.5 * 15 = 22.5 + 22.5 = **45**.
- Outliers: Values < -15 or > 45 (none in this dataset).
