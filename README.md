
# **Predicting and Preventing Customer Churn at Syriatel**  
*A Data-Driven Approach to Customer Retention*

## **Overview**

Customer churn poses a critical challenge for Syriatel, directly affecting both revenue and customer loyalty. This project leverages data science techniques to predict churn and recommend strategies for targeted customer retention. By identifying at-risk customers early, Syriatel can take proactive steps to minimize churn and strengthen customer relationships.

---

## **Business Problem and Stakeholders**

### **Business Problem**

The main business objective is to predict customer churn so Syriatel can:

- Implement timely and personalized retention strategies.
- Minimize revenue losses due to customer departures.
- Maximize the return on customer acquisition and service costs.

Accurately identifying potential churners allows for strategic intervention, helping to reduce the long-term churn rate.

### **Key Stakeholders**

- **Customer Retention Team:** Uses predictions to guide personalized outreach strategies.
- **Marketing & Customer Service Teams:** Implements customized offers and support based on churn signals.
- **Syriatel Management:** Informs strategic decisions to reduce churn and improve customer satisfaction.
- **Data Science & Analytics Teams:** Continuously improve the model and extract actionable insights.

---

## **Dataset and Methodology**

### **Dataset Description**

The analysis uses a dataset (`syriatel_churn.csv`) comprising:

- **Customer demographics**
- **Service usage patterns**
- **Subscription details**
- **Customer service interactions**
- **Churn status (target variable)**

This dataset is ideal for modeling churn as it includes meaningful predictors of customer behavior.

### **Modeling Techniques**

The project experimented with various machine learning models, ultimately emphasizing a **Decision Tree** model for interpretability and recall. Additional models explored:

- **Logistic Regression**
- **Random Forest**
- **Support Vector Machine (SVM)**

### **Preprocessing and Feature Engineering**

- **Handling missing values**
- **One-hot encoding of categorical features**
- **Feature scaling (standardization)**
- **Exploratory data analysis to uncover trends and outliers**

---

## **Key Findings – Drivers of Churn**

Top features influencing churn:

- **Total Day Minutes:** High daily usage correlates with higher churn probability.
- **Customer Service Calls:** More frequent calls often indicate dissatisfaction.
- **Contract Type:** Month-to-month contracts show higher churn rates.
- **International Plan:** Customers with this plan are more likely to churn.
- **Voicemail Plan:** Absence of this service is linked to increased churn risk.

These features provide critical insights into churn behavior and are central to effective retention strategies.

---

## **Model Evaluation and Predictive Power**

- **Recall:** 65.31% – effectively identifies the majority of churners (prioritized over precision).
- **Accuracy:** 92.51% – overall correctness of model predictions.

### **Performance Metrics Used**

- **Precision**
- **Recall**
- **F1-score**
- **AUC-ROC**

The **Random Forest** model was optimized using **RandomizedSearchCV**, but the **Decision Tree** was selected for final deployment due to its interpretability and solid performance in recall.

---

## **Retention Strategies Based on Insights**

### **Targeted Interventions**

- **High Usage Customers:** Offer customized data or call plans to add value.
- **Customer Service Issues:** Prioritize follow-ups and support for frequently calling customers.
- **Month-to-Month Contracts:** Introduce incentives for switching to long-term plans.
- **International Plan Holders:** Design better international packages or loyalty programs.
- **Voicemail Plan Non-Users:** Educate users on the value of voicemail and offer free trials.

### **Personalized Approach**

Use model outputs to design customer-specific offers and engagement plans, improving overall retention and satisfaction.

---

## **Conclusion and Next Steps**

### **Impact**

- Delivers a **high-recall model** for effective churn prediction.
- Provides **actionable insights** for designing personalized retention campaigns.
- Enhances **strategic decision-making** with data-backed evidence.

### **Next Steps**

- **Model Improvement:** Explore ensemble methods and advanced feature engineering.
- **Performance Monitoring:** Set up dashboards and monitoring systems to track real-time churn predictions.
- **Cross-Team Collaboration:** Engage stakeholders across departments for cohesive implementation of strategies.

---
