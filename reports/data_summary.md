# Dataset Summary Report

## Project
Fitness Customer Retention Analytics

---

## Dataset Overview

- **Dataset Name:** Gym Customers Features and Churn
- **Source:** Kaggle
- **Objective:** Analyze customer engagement patterns and identify the factors that influence customer churn and long-term retention.

---

## Target Variable

**Churn**

- 0 = Customer Retained
- 1 = Customer Churned

This is the target variable that will be used for prediction.

---

## Features in the Dataset

The dataset contains customer demographic, membership, and engagement information.

### Customer Information
- Gender
- Age

### Membership Information
- Near_Location
- Partner
- Promo_friends
- Contract_period
- Lifetime

### Engagement Information
- Group_visits
- Avg_class_frequency_total
- Avg_class_frequency_current_month

### Financial Information
- Month_to_end_contract

### Target
- Churn

---

## Initial Findings

### Missing Values
No missing values were found in the dataset.

### Duplicate Records
No duplicate records were found.

### Data Types
- Integer columns
- Float columns
- Boolean/Binary columns

The dataset is clean and ready for analysis.

---

## Key Observations

- Customer engagement is measured using class attendance frequency.
- Membership duration (Lifetime) may have an impact on customer retention.
- Contract period can influence churn behaviour.
- Group visits may indicate stronger customer engagement.
- Promotional referrals may affect customer loyalty.
- Age may also contribute to customer retention.

---

## Next Steps

- Perform Exploratory Data Analysis (EDA)
- Visualize customer behaviour
- Identify features influencing churn
- Engineer new features if required
