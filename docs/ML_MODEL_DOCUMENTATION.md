# ML Model Documentation

## 1. Model Used

The final model used for churn prediction is a **Random Forest Classifier**.

The trained model is saved as:

`models/churn_model.pkl`

The application loads the saved model using `src/model.py` rather than retraining it during prediction.

---

## 2. Model Comparison

Two classification models were evaluated:

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9250 | 0.8800 | 0.8302 | 0.8544 | 0.9775 |
| Random Forest | 0.9275 | 0.8929 | 0.8255 | 0.8578 | 0.9712 |

---

## 3. Why Random Forest Was Selected

Random Forest was selected because it achieved the highest accuracy, precision, and F1-score among the evaluated models.

Although Logistic Regression achieved slightly higher recall and ROC-AUC, Random Forest provided a stronger overall balance between accuracy, precision, and F1-score.

Since the application needs to classify customers according to their likelihood of churn, Random Forest was selected as the final model.

---

## 4. Model Performance

The final Random Forest model achieved:

- **Accuracy:** 0.9275
- **Precision:** 0.8929
- **Recall:** 0.8255
- **F1 Score:** 0.8578
- **ROC-AUC:** 0.9712

---

## 5. Prediction Pipeline

The prediction pipeline works as follows:

```text
Customer Features
       ↓
Saved Random Forest Model
       ↓
load_model()
       ↓
predict_proba()
       ↓
Churn Probability
       ↓
Risk Classification
       ↓
Low / Medium / High