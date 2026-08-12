import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Profile",
    page_icon="👤",
    layout="wide"
)

st.title("Customer Profile")

st.caption("Detailed engagement and churn analysis for an individual member.")

st.divider()


# --------------------------------------------------
# MEMBER HEADER
# --------------------------------------------------

col1, col2 = st.columns([3, 1])

with col1:
    st.header("Member ID: M1024")
    st.caption("Last Active: 2 days ago • Member since July 2023")

with col2:
    st.metric("Churn Probability", "87%")


st.divider()


# --------------------------------------------------
# MEMBERSHIP DETAILS
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("Membership Details")

    st.metric("Contract Period", "1 Month")
    st.metric("Lifetime", "3 Months")
    st.metric("Months to End Contract", "0.5 Months")


with col2:

    st.subheader("Engagement Metrics")

    metric1, metric2 = st.columns(2)

    with metric1:
        st.metric("Avg Class Frequency", "2.5 / week")

    with metric2:
        st.metric("Current Month Frequency", "0.4 / week")

    metric3, metric4 = st.columns(2)

    with metric3:
        st.metric("Group Visits", "No")

    with metric4:
        st.metric("Additional Charges", "$12.50")


st.divider()


# --------------------------------------------------
# CHURN DRIVERS
# --------------------------------------------------

st.subheader("Churn Drivers Analysis")

st.warning(
    "Dramatic Usage Drop — Current engagement has decreased compared "
    "with the historical average."
)

st.warning(
    "Short Contract Duration — Shorter contracts may be associated "
    "with increased churn risk."
)

st.info(
    "Low Community Stickiness — No group class participation has "
    "been recorded."
)


st.divider()


# --------------------------------------------------
# RECOMMENDED STRATEGY
# --------------------------------------------------

st.subheader("Recommended Retention Strategy")

st.write(
    "Consider a targeted re-engagement strategy for this member "
    "based on their engagement pattern and churn risk."
)

st.button("Take Action")