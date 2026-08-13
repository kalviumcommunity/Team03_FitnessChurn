import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from src.analytics import (
    load_data,
    churn_rate_by_contract,
    churn_rate_by_group_visits,
    engagement_churn_relationship,
    lifetime_churn_relationship
)

st.set_page_config(
    page_title="Insights",
    page_icon="💡",
    layout="wide"
)

# --------------------------------------------------
# LOAD ANALYTICS DATA
# --------------------------------------------------

df = load_data()

contract_data = churn_rate_by_contract(df)
group_data = churn_rate_by_group_visits(df)
engagement_data = engagement_churn_relationship(df)
lifetime_data = lifetime_churn_relationship(df)

# --------------------------------------------------
# CALCULATE KEY VALUES
# --------------------------------------------------

one_month_churn = contract_data.loc[
    contract_data["Contract Period"] == 1,
    "Churn Rate"
].iloc[0]

six_month_churn = contract_data.loc[
    contract_data["Contract Period"] == 6,
    "Churn Rate"
].iloc[0]

twelve_month_churn = contract_data.loc[
    contract_data["Contract Period"] == 12,
    "Churn Rate"
].iloc[0]

group_churn = group_data.loc[
    group_data["Group Visits"] == "Group Visits",
    "Churn Rate"
].iloc[0]

no_group_churn = group_data.loc[
    group_data["Group Visits"] == "No Group Visits",
    "Churn Rate"
].iloc[0]

retained_frequency = engagement_data.loc[
    engagement_data["Churn Status"] == "Retained",
    "Avg_class_frequency_current_month"
].iloc[0]

churned_frequency = engagement_data.loc[
    engagement_data["Churn Status"] == "Churned",
    "Avg_class_frequency_current_month"
].iloc[0]

retained_lifetime = lifetime_data.loc[
    lifetime_data["Churn Status"] == "Retained",
    "Lifetime"
].iloc[0]

churned_lifetime = lifetime_data.loc[
    lifetime_data["Churn Status"] == "Churned",
    "Lifetime"
].iloc[0]

group_churn_difference = no_group_churn - group_churn

# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("Business Insights & Recommendations")

st.caption(
    "Actionable indicators based on behavioural analysis and "
    "observed patterns in the customer dataset."
)

st.divider()

# --------------------------------------------------
# INSIGHT CARDS
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.error("HIGH PRIORITY")

    st.subheader("Contract Period Correlation")

    st.write(
        f"Customers with 1-month contracts have a churn rate of "
        f"{one_month_churn:.2f}%, compared with {six_month_churn:.2f}% "
        f"for 6-month contracts and {twelve_month_churn:.2f}% "
        f"for 12-month contracts."
    )

    st.caption(
        "The 1-month contract segment shows the highest observed churn."
    )


with col2:

    st.warning("BEHAVIOURAL ALERT")

    st.subheader("Activity Variance Alert")

    st.write(
        f"Retained members average {retained_frequency:.2f} visits per month "
        f"in the current month, compared with {churned_frequency:.2f} "
        f"for churned members."
    )

    st.caption(
        "Lower recent activity is associated with higher churn in this dataset."
    )


col3, col4 = st.columns(2)

with col3:

    st.success("RETENTION DRIVER")

    st.subheader("Community Participation")

    st.write(
        f"Members with group visits have a {group_churn:.2f}% churn rate, "
        f"compared with {no_group_churn:.2f}% for members without group visits."
    )

    st.caption(
        f"Observed difference: {group_churn_difference:.2f} percentage points."
    )


with col4:

    st.info("STRATEGY TIP")

    st.subheader("Proactive Re-engagement")

    st.write(
        f"Churned members have an average lifetime of {churned_lifetime:.2f} "
        f"months, compared with {retained_lifetime:.2f} months for retained members."
    )

    st.caption(
        "Members showing lower engagement may be useful candidates for proactive re-engagement."
    )

# --------------------------------------------------
# KEY ANALYTICS SUMMARY
# --------------------------------------------------

st.divider()

st.subheader("Key Analytics Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "1-Month Churn",
        f"{one_month_churn:.2f}%"
    )

with col2:
    st.metric(
        "12-Month Churn",
        f"{twelve_month_churn:.2f}%"
    )

with col3:
    st.metric(
        "Group Visit Churn",
        f"{group_churn:.2f}%"
    )

with col4:
    st.metric(
        "No Group Visit Churn",
        f"{no_group_churn:.2f}%"
    )

# --------------------------------------------------
# DISCLAIMER
# --------------------------------------------------

st.divider()

st.caption(
    "Note: These insights represent statistical associations and "
    "predictive indicators. They do not imply direct causation."
)