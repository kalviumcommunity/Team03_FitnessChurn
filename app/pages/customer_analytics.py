import streamlit as st
import sys
import os

# --------------------------------------------------
# IMPORT PROJECT MODULES
# --------------------------------------------------

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
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

col1, col2, col3 = st.columns(3)


# --------------------------------------------------
# CONTRACT PERIOD FILTER
# --------------------------------------------------

with col1:

    contract_period = st.selectbox(
        "Contract Period",
        [
            "All Periods",
            "1 Month",
            "6 Months",
            "12 Months"
        ]
    )


# --------------------------------------------------
# GENDER FILTER
# --------------------------------------------------

with col2:

    gender = st.selectbox(
        "Gender",
        [
            "All Genders",
            "Male",
            "Female"
        ]
    )


# --------------------------------------------------
# GROUP VISITS FILTER
# --------------------------------------------------

with col3:

    group_visits = st.selectbox(
        "Group Visits",
        [
            "All Members",
            "Yes",
            "No"
        ]
    )


# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

filtered_df = df.copy()


# Contract Period

if contract_period != "All Periods":

    contract_map = {
        "1 Month": 1,
        "6 Months": 6,
        "12 Months": 12
    }

    selected_contract = contract_map[contract_period]

    filtered_df = filtered_df[
        filtered_df["Contract_period"] == selected_contract
    ]


# Gender

if gender != "All Genders":

    gender_map = {
        "Male": 1,
        "Female": 0
    }

    selected_gender = gender_map[gender]

    filtered_df = filtered_df[
        filtered_df["gender"] == selected_gender
    ]


# Group Visits

if group_visits != "All Members":

    group_map = {
        "Yes": 1,
        "No": 0
    }

    selected_group_visit = group_map[group_visits]

    filtered_df = filtered_df[
        filtered_df["Group_visits"] == selected_group_visit
    ]


# --------------------------------------------------
# FILTER SUMMARY
# --------------------------------------------------

st.write("")

st.caption(
    f"Showing {len(filtered_df):,} members based on the selected filters."
)

st.divider()


# --------------------------------------------------
# CHECK FOR EMPTY DATA
# --------------------------------------------------

if filtered_df.empty:

    st.warning(
        "No members match the selected filters. "
        "Please select different filter options."
    )

    st.stop()


# --------------------------------------------------
# ANALYTICS DATA
# --------------------------------------------------

contract_data = churn_rate_by_contract(filtered_df)

contract_data["Contract Period"] = contract_data[
    "Contract Period"
].map({
    1: "1 Month",
    6: "6 Months",
    12: "12 Months"
})


group_data = churn_rate_by_group_visits(filtered_df)


engagement_data = engagement_churn_relationship(filtered_df)

engagement_data = engagement_data.rename(
    columns={
        "Avg_class_frequency_current_month":
        "Average Visits / Month"
    }
)


lifetime_data = lifetime_churn_relationship(filtered_df)

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

    group_visit_rows = group_data[
        group_data["Group Visits"] == "Group Visits"
    ]

    no_group_visit_rows = group_data[
        group_data["Group Visits"] == "No Group Visits"
    ]

    if (
        not group_visit_rows.empty
        and not no_group_visit_rows.empty
    ):

        group_churn = group_visit_rows[
            "Churn Rate"
        ].iloc[0]

        no_group_churn = no_group_visit_rows[
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

    else:

        st.info(
            "Both group-visit categories are not available "
            "under the current filters."
        )


st.write("")


# --------------------------------------------------
# CHARTS 3 & 4
# --------------------------------------------------

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

    retained_rows = engagement_data[
        engagement_data["Churn Status"] == "Retained"
    ]

    churned_rows = engagement_data[
        engagement_data["Churn Status"] == "Churned"
    ]

    if (
        not retained_rows.empty
        and not churned_rows.empty
    ):

        retained_frequency = retained_rows[
            "Average Visits / Month"
        ].iloc[0]

        churned_frequency = churned_rows[
            "Average Visits / Month"
        ].iloc[0]

        st.info(
            f"Insight: Retained members average "
            f"{retained_frequency:.2f} visits per month, "
            f"compared with {churned_frequency:.2f} for "
            f"churned members."
        )

    else:

        st.info(
            "Both retained and churned members are not "
            "available under the current filters."
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

    retained_lifetime_rows = lifetime_data[
        lifetime_data["Churn Status"] == "Retained"
    ]

    churned_lifetime_rows = lifetime_data[
        lifetime_data["Churn Status"] == "Churned"
    ]

    if (
        not retained_lifetime_rows.empty
        and not churned_lifetime_rows.empty
    ):

        retained_lifetime = retained_lifetime_rows[
            "Average Lifetime (Months)"
        ].iloc[0]

        churned_lifetime = churned_lifetime_rows[
            "Average Lifetime (Months)"
        ].iloc[0]

        st.info(
            f"Insight: Retained members have an average "
            f"lifetime of {retained_lifetime:.2f} months, "
            f"compared with {churned_lifetime:.2f} months "
            f"for churned members."
        )

    else:

        st.info(
            "Both retained and churned members are not "
            "available under the current filters."
        )


# --------------------------------------------------
# KEY ANALYTICS SUMMARY
# --------------------------------------------------

st.divider()

st.subheader("Key Analytics Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)


# --------------------------------------------------
# SUMMARY — 1 MONTH CHURN
# --------------------------------------------------

with summary_col1:

    one_month_rows = contract_data[
        contract_data["Contract Period"] == "1 Month"
    ]

    if not one_month_rows.empty:

        one_month_churn = one_month_rows[
            "Churn Rate"
        ].iloc[0]

        st.metric(
            "1-Month Churn Rate",
            f"{one_month_churn:.2f}%"
        )

    else:

        st.metric(
            "1-Month Churn Rate",
            "N/A"
        )


# --------------------------------------------------
# SUMMARY — GROUP VISIT CHURN
# --------------------------------------------------

with summary_col2:

    if not group_visit_rows.empty:

        st.metric(
            "Group Visit Churn Rate",
            f"{group_churn:.2f}%"
        )

    else:

        st.metric(
            "Group Visit Churn Rate",
            "N/A"
        )


# --------------------------------------------------
# SUMMARY — NO GROUP VISIT CHURN
# --------------------------------------------------

with summary_col3:

    if not no_group_visit_rows.empty:

        st.metric(
            "No Group Visit Churn Rate",
            f"{no_group_churn:.2f}%"
        )

    else:

        st.metric(
            "No Group Visit Churn Rate",
            "N/A"
        )


# --------------------------------------------------
# DISCLAIMER
# --------------------------------------------------

st.divider()

st.caption(
    "Note: These insights represent statistical associations "
    "and predictive indicators. They do not imply direct causation."
)