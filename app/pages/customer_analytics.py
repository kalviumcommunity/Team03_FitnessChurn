import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Analytics",
    page_icon="📊",
    layout="wide"
)

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
        ["All Segments", "Highly Engaged", "Moderately Engaged", "Low Engagement"]
    )


st.divider()


# --------------------------------------------------
# ANALYTICS CHARTS
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("Churn Rate by Contract Period")

    contract_data = pd.DataFrame(
        {
            "Contract Period": [
                "1 Month",
                "6 Months",
                "12 Months"
            ],
            "Churn Rate": [
                42,
                18,
                9
            ]
        }
    )

    st.bar_chart(
        contract_data,
        x="Contract Period",
        y="Churn Rate"
    )

    st.info(
        "Insight: Contract duration can be compared with churn "
        "to identify higher-risk membership segments."
    )


with col2:

    st.subheader("Churn Rate by Group Visits")

    group_data = pd.DataFrame(
        {
            "Group Visit": [
                "No Group Visits",
                "Group Visits"
            ],
            "Members": [
                26.3,
                73.7
            ]
        }
    )

    st.bar_chart(
        group_data,
        x="Group Visit",
        y="Members"
    )

    st.success(
        "Insight: Group participation can be analysed "
        "to understand its relationship with retention."
    )


st.write("")

col3, col4 = st.columns(2)


with col3:

    st.subheader("Engagement Frequency vs Churn")

    engagement_data = pd.DataFrame(
        {
            "Visits / Week": [
                1,
                2,
                3,
                4,
                5
            ],
            "Churn Rate": [
                82,
                45,
                15,
                7,
                3
            ]
        }
    )

    st.line_chart(
        engagement_data,
        x="Visits / Week",
        y="Churn Rate"
    )


with col4:

    st.subheader("Member Lifetime Distribution")

    lifetime_data = pd.DataFrame(
        {
            "Lifetime (Months)": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8
            ],
            "Members": [
                30,
                70,
                120,
                150,
                100,
                60,
                45,
                35
            ]
        }
    )

    st.bar_chart(
        lifetime_data,
        x="Lifetime (Months)",
        y="Members"
    )


st.divider()

st.subheader("Analysis Status")

st.info(
    "The current charts use placeholder values for UI development. "
    "They will be connected to the cleaned dataset and calculated analytics "
    "before the final demo."
)