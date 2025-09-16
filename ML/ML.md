* **Supervise Learning :** When we have labeled data then we use supervise learning.

  * **Regression :** Regression is a machine learning task where the goal is to predict a continuous numerical value based on input features. The output is a real number (Contineous values).

    * Real number output : Infinite (uncountable).
    * **Examples** :

      * Predicting house prices based on size, location, and number of bedrooms.
      * Forecasting sales revenue for a company.
      * Estimating a person’s age from biometric data.
  * **Classification** : Classification is a machine learning task where the goal is to predict the category or class label of a data point based on its features. The output is discrete (categorical).

    * Descrete output : countable values.
    * **Examples** :

      * Predicting whether an email is spam or not spam (binary classification).
      * Classifying an image as a dog, cat, or bird (multi-class classification).
      * Determining if a patient has a disease (e.g., positive or negative).
* Dependent Feature
* Independent Feature
* ML Workflow

  * 1> Load and Understand the Dataset
  * 2> Data Cleaning
  * 3> Data Preprocessing
    * Labeled Encoding
    * One Hot Encoding
  * 4> Featurre Engineering
  * 5> Model Training
  * 6> Model Evaluation
  * 7> Deployment
* 

---

##### **Confusion Matrix:**

The confusion matrix is a matrix used to determine the performance of the classification models for a given set of test data.

|                           | Predicted Positive  | Predicted Negative  |
| ------------------------- | ------------------- | ------------------- |
| **Actual Positive** | True Positive (TP)  | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN)  |

* **True Negative:** Model has given prediction No, and the real or actual value was also No.
* **True Positive:** The model has predicted yes, and the actual value was also true.
* **False Negative:** The model has predicted no, but the actual value was Yes, it is also called as  **Type-II error** .
* **False Positive:** The model has predicted Yes, but the actual value was No. It is also called a **Type-I error.**

**Calculations using Confusion Matrix:**

* **Classification Accuracy:** It is one of the important parameters to determine the accuracy of the classification problems.
  * $\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$
  * 
* **Misclassification rate:** the error rate is a metric that quantifies the proportion of incorrect predictions made by a classification model.
  * $\text{Error Rate} = \frac{FP + FN}{TP + TN + FP + FN}$
  * 
* **Precision:** It can be defined as the number of correct outputs provided by the model or out of all positive classes that have predicted correctly by the model, how many of them were actually true.
  * $\text{Precision} = \frac{TP}{TP + FP}$
  * 
* **Recall:** It is defined as the out of total positive classes, how our model predicted correctly. The recall must be as high as possible.
  * $\text{Recall} = \frac{TP}{TP + FN}$
  * 
* **F1-Score:** If two models have low precision and high recall or vice versa, it is difficult to compare these models. So, for this purpose, we can use F1-score. This score helps us to evaluate the recall and precision at the same time. The F1-score is maximum if the recall is equal to the precision.
  * $\text{F1-Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$
  *
