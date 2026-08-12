import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Churn Prediction",
    page_icon="⚡",
    layout="wide"
)

st.title("Churn Risk Prediction")

st.caption(
    "Identify members who are most likely to churn based on behavioural patterns."
)

st.divider()


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Members Analysed", "4,000")

with col2:
    st.metric("High Risk", "437")

with col3:
    st.metric("Medium Risk", "892")

with col4:
    st.metric("Low Risk", "2,671")


st.divider()


# --------------------------------------------------
# PREDICTION TABLE
# --------------------------------------------------

st.subheader("Predictive Churn Register")

st.caption(
    "Risk classification: High >70% | Medium 30–70% | Low <30%"
)

prediction_data = pd.DataFrame(
    {
        "Member ID": [
            "M1024",
            "M1048",
            "M1091",
            "M1105",
            "M1122",
            "M1156",
            "M1189"
        ],
        "Churn Probability": [
            "87%",
            "74%",
            "42%",
            "12%",
            "58%",
            "25%",
            "91%"
        ],
        "Contract Period": [
            "1 Month",
            "3 Months",
            "6 Months",
            "12 Months",
            "3 Months",
            "12 Months",
            "1 Month"
        ],
        "Class Frequency": [
            "0.4/week",
            "0.8/week",
            "2.1/week",
            "4.5/week",
            "1.2/week",
            "3.2/week",
            "0.2/week"
        ],
        "Lifetime": [
            "3 Months",
            "5 Months",
            "8 Months",
            "14 Months",
            "4 Months",
            "18 Months",
            "2 Months"
        ],
        "Risk Status": [
            "High Risk",
            "High Risk",
            "Medium Risk",
            "Low Risk",
            "Medium Risk",
            "Low Risk",
            "High Risk"
        ],
        "Action": [
            "Intervene",
            "Intervene",
            "Review",
            "Details",
            "Review",
            "Details",
            "Intervene"
        ]
    }
)

st.dataframe(
    prediction_data,
    use_container_width=True,
    hide_index=True
)


st.divider()


st.info(
    "The prediction values shown here are temporary UI data. "
    "They will be replaced by the trained machine learning model."
)


col1, col2 = st.columns(2)

with col1:
    st.button("Export Prediction CSV")

with col2:
    st.button("Refresh Model")