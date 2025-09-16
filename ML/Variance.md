
# Variance

**Variance** is a statistical measure that tells us how much the values in a dataset differ (spread out) from the **mean (average)**.

---

## 📌 Formal Definition:
The variance of a random variable (or dataset) is the **average of the squared differences from the mean**.

### Population Variance:
For a population with values \(x_1, x_2, x_3, ..., x_N\):

\[
\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2
\]

- \(\sigma^2\) = population variance  
- \(x_i\) = each data point  
- \(\mu\) = population mean  
- \(N\) = number of data points  

### Sample Variance:
For a **sample** (instead of whole population):

\[
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
\]

- \(s^2\) = sample variance  
- \(\bar{x}\) = sample mean  
- \(n\) = sample size  

---

## 📌 Intuition:
- If variance = **0**, all data points are the same (no spread).  
- Higher variance = data points are **more spread out** from the mean.  

---

## 📌 Example:
Suppose we have data: **[2, 4, 6, 8]**  

1. Mean = \(\frac{2+4+6+8}{4} = 5\)  
2. Differences from mean = \([-3, -1, +1, +3]\)  
3. Squared differences = \([9, 1, 1, 9]\)  
4. Average of squared differences = \(\frac{20}{4} = 5\)  

✅ Variance = **5**  

---

## 📌 Relation to Standard Deviation:
- **Standard Deviation (σ)** is just the square root of variance.  
\[
\sigma = \sqrt{\sigma^2}
\]

So variance is in **squared units**, while standard deviation brings it back to original units.
