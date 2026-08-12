import streamlit as st

st.set_page_config(
    page_title="Insights",
    page_icon="💡",
    layout="wide"
)

st.title("Business Insights & Recommendations")

st.caption(
    "Actionable indicators based on predictive modelling and behavioural analysis."
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
        "Members with shorter contract periods can be analysed "
        "for higher churn risk compared with long-term members."
    )

    st.caption("View Segment →")


with col2:

    st.warning("BEHAVIOURAL ALERT")

    st.subheader("Activity Variance Alert")

    st.write(
        "Members whose current-month activity decreases compared "
        "with their historical average may require early intervention."
    )

    st.caption("Risk Report →")


col3, col4 = st.columns(2)


with col3:

    st.success("RETENTION DRIVER")

    st.subheader("Community Participation")

    st.write(
        "Analyse whether group-visit behaviour is associated "
        "with higher retention rates."
    )

    st.caption("Optimization Tips →")


with col4:

    st.info("STRATEGY TIP")

    st.subheader("Proactive Re-engagement")

    st.write(
        "Prioritize re-engagement strategies for members "
        "showing declining activity trends."
    )

    st.caption("Setup Workflow →")


st.divider()


# --------------------------------------------------
# DISCLAIMER
# --------------------------------------------------

st.caption(
    "Note: These insights represent statistical associations and "
    "predictive indicators. They do not imply direct causation."
)