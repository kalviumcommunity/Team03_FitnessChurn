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


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Analytics",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = load_data()


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("Customer Analytics")

st.caption(
    "Explore customer behaviour and identify patterns associated with churn."
)

st.divider()


# --------------------------------------------------
# FILTERS
# --------------------------------------------------

st.subheader("Global Analysis Filters")

col1, col2, col3, col4 = st.columns(4)

with col1:
    contract_period = st.selectbox(
        "Contract Period",
        ["All Periods", "1 Month", "6 Months", "12 Months"]
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["All Genders", "Male", "Female"]
    )

with col3:
    group_visits = st.selectbox(
        "Group Visits",
        ["All Members", "Yes", "No"]
    )

with col4:
    engagement = st.selectbox(
        "Engagement Segment",
        [
            "All Segments",
            "Highly Engaged",
            "Moderately Engaged",
            "Low Engagement"
        ]
    )


st.divider()


# --------------------------------------------------
# ANALYTICS DATA
# --------------------------------------------------

contract_data = churn_rate_by_contract(df)

contract_data["Contract Period"] = contract_data[
    "Contract Period"
].map({
    1: "1 Month",
    6: "6 Months",
    12: "12 Months"
})


group_data = churn_rate_by_group_visits(df)


engagement_data = engagement_churn_relationship(df)

engagement_data = engagement_data.rename(
    columns={
        "Avg_class_frequency_current_month":
        "Average Visits / Month"
    }
)


lifetime_data = lifetime_churn_relationship(df)

lifetime_data = lifetime_data.rename(
    columns={
        "Lifetime":
        "Average Lifetime (Months)"
    }
)


# --------------------------------------------------
# ANALYTICS CHARTS
# --------------------------------------------------

col1, col2 = st.columns(2)


# --------------------------------------------------
# CHART 1 — CONTRACT PERIOD
# --------------------------------------------------

with col1:

    st.subheader("Churn Rate by Contract Period")

    st.bar_chart(
        contract_data,
        x="Contract Period",
        y="Churn Rate"
    )

    highest_contract = contract_data.loc[
        contract_data["Churn Rate"].idxmax()
    ]

    lowest_contract = contract_data.loc[
        contract_data["Churn Rate"].idxmin()
    ]

    st.info(
        f"Insight: {highest_contract['Contract Period']} "
        f"members have the highest churn rate at "
        f"{highest_contract['Churn Rate']:.2f}%, while "
        f"{lowest_contract['Contract Period']} members have "
        f"the lowest churn rate at "
        f"{lowest_contract['Churn Rate']:.2f}%."
    )


# --------------------------------------------------
# CHART 2 — GROUP VISITS
# --------------------------------------------------

with col2:

    st.subheader("Churn Rate by Group Visits")

    st.bar_chart(
        group_data,
        x="Group Visits",
        y="Churn Rate"
    )

    group_churn = group_data.loc[
        group_data["Group Visits"] == "Group Visits",
        "Churn Rate"
    ].iloc[0]

    no_group_churn = group_data.loc[
        group_data["Group Visits"] == "No Group Visits",
        "Churn Rate"
    ].iloc[0]

    difference = no_group_churn - group_churn

    st.success(
        f"Insight: Members with group visits have a "
        f"{group_churn:.2f}% churn rate compared with "
        f"{no_group_churn:.2f}% for members without group "
        f"visits — a difference of {difference:.2f} "
        f"percentage points."
    )


st.write("")


col3, col4 = st.columns(2)


# --------------------------------------------------
# CHART 3 — ENGAGEMENT VS CHURN
# --------------------------------------------------

with col3:

    st.subheader("Engagement Frequency vs Churn")

    st.bar_chart(
        engagement_data,
        x="Churn Status",
        y="Average Visits / Month"
    )

    retained_frequency = engagement_data.loc[
        engagement_data["Churn Status"] == "Retained",
        "Average Visits / Month"
    ].iloc[0]

    churned_frequency = engagement_data.loc[
        engagement_data["Churn Status"] == "Churned",
        "Average Visits / Month"
    ].iloc[0]

    st.info(
        f"Insight: Retained members average "
        f"{retained_frequency:.2f} visits per month, "
        f"compared with {churned_frequency:.2f} for "
        f"churned members."
    )


# --------------------------------------------------
# CHART 4 — MEMBER LIFETIME
# --------------------------------------------------

with col4:

    st.subheader("Member Lifetime by Churn Status")

    st.bar_chart(
        lifetime_data,
        x="Churn Status",
        y="Average Lifetime (Months)"
    )

    retained_lifetime = lifetime_data.loc[
        lifetime_data["Churn Status"] == "Retained",
        "Average Lifetime (Months)"
    ].iloc[0]

    churned_lifetime = lifetime_data.loc[
        lifetime_data["Churn Status"] == "Churned",
        "Average Lifetime (Months)"
    ].iloc[0]

    st.info(
        f"Insight: Retained members have an average lifetime "
        f"of {retained_lifetime:.2f} months, compared with "
        f"{churned_lifetime:.2f} months for churned members."
    )


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

st.divider()

st.subheader("Key Analytics Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)

with summary_col1:

    st.metric(
        "1-Month Churn Rate",
        f"{contract_data.loc[contract_data['Contract Period'] == '1 Month', 'Churn Rate'].iloc[0]:.2f}%"
    )

with summary_col2:

    st.metric(
        "Group Visit Churn Rate",
        f"{group_churn:.2f}%"
    )

with summary_col3:

    st.metric(
        "No Group Visit Churn Rate",
        f"{no_group_churn:.2f}%"
    )


# --------------------------------------------------
# DISCLAIMER
# --------------------------------------------------

st.divider()

st.caption(
    "Note: These insights represent statistical associations "
    "and predictive indicators. They do not imply direct causation."
)