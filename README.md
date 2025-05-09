# Syriatel Telecom Customer Churn Prediction

## Overview

This project aims to predict customer churn for Syriatel Telecom using machine learning. It involves data exploration, preprocessing, feature engineering, model training, evaluation, and optimization. The project uses a dataset containing information about Syriatel's customers and whether they churned or not.

## Business and Data Understanding

### Stakeholder Audience

The primary stakeholders for this project are:

* **Syriatel Telecom's management team:** They can use the insights from this project to understand the factors driving customer churn and develop strategies to reduce it.
* **Marketing and customer service teams:** They can use the predictions to identify customers at high risk of churn and proactively engage with them to improve retention.
* **Data science and analytics teams:** They can leverage this project as a template for building other churn prediction models.

### Dataset Choice

The dataset used in this project is named "syriatel_churn.csv". It contains information about Syriatel Telecom customers, including demographics, service usage patterns, and churn status. This dataset is suitable for building a churn prediction model because it includes the necessary features to understand and predict customer behavior.

## Modeling

The project explores three different classification models for churn prediction:

1. **Logistic Regression:** A simple and interpretable linear model.
2. **Random Forest:** A robust ensemble model known for its accuracy.
3. **Support Vector Machine (SVM):** A powerful model capable of handling complex relationships.

The models are trained on a prepared dataset that has undergone preprocessing steps, including:

* **Handling missing values:** Missing values were addressed.
* **Converting categorical features:** Categorical features were converted to numerical representations using one-hot encoding.
* **Scaling numerical features:** Numerical features were scaled using standardization.

## Evaluation

The trained models are evaluated on a validation set using the following metrics:

* **Accuracy:** The overall correctness of the predictions.
* **Precision:** The proportion of correctly predicted churned customers out of all customers predicted to churn.
* **Recall:** The proportion of correctly predicted churned customers out of all actual churned customers.
* **F1-score:** A balanced measure considering both precision and recall.
* **AUC-ROC:** The area under the receiver operating characteristic curve, indicating the model's ability to distinguish between churned and non-churned customers.

The Random Forest model is further optimized using RandomizedSearchCV to find the best hyperparameters and improve its performance.

## Conclusion

The project provides a comprehensive analysis of customer churn for Syriatel Telecom. The results can be used to guide decision-making and implement strategies to improve customer retention. The project highlights the importance of data preprocessing, feature engineering, and model optimization in building accurate and reliable churn prediction models.
