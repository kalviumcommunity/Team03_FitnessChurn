import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Fitness Retain AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #f8fafc;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e5e7eb;
        padding: 20px;
        border-radius: 12px;
    }

    /* Remove excessive top spacing */
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <h2 style="color:white; margin-bottom:5px;">
            📊 Retain AI
        </h2>
        <p style="color:#9ca3af;">
            Fitness Retention Analytics
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.page_link(
        "app.py",
        label="Dashboard",
        icon="🏠"
    )

    st.page_link(
        "pages/customer_analytics.py",
        label="Customer Analytics",
        icon="📊"
    )

    st.page_link(
        "pages/churn_prediction.py",
        label="Churn Prediction",
        icon="⚡"
    )

    st.page_link(
        "pages/customer_profile.py",
        label="Customer Profile",
        icon="👤"
    )

    st.page_link(
        "pages/insights.py",
        label="Insights",
        icon="💡"
    )

    st.divider()

    st.write("⚙️ Settings")

    st.markdown(
        """
        <div style="
            margin-top:40px;
            padding:10px;
            color:#d1d5db;
        ">
            <b>Alex Jensen</b><br>
            <small>Manager</small>
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# DASHBOARD HEADER
# --------------------------------------------------

st.title("Retention Overview")

st.caption(
    "Monitor customer retention, engagement and churn risk."
)

st.write("")


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Members",
        value="4,000",
        delta="12%"
    )

with col2:
    st.metric(
        label="Overall Churn Rate",
        value="26.4%",
        delta="2.1%",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="Avg Member Lifetime",
        value="4.7 mo",
        delta="0.4"
    )

with col4:
    st.metric(
        label="High-Risk Members",
        value="437",
        delta="Stable"
    )


st.write("")
st.divider()


# --------------------------------------------------
# CHURN + ENGAGEMENT OVERVIEW
# --------------------------------------------------

left_col, right_col = st.columns(2)


# --------------------------------------------------
# CHURN OVERVIEW
# --------------------------------------------------

with left_col:

    st.subheader("Churn Overview")

    churn_data = pd.DataFrame(
        {
            "Status": ["Retained", "Churned"],
            "Members": [2944, 1056]
        }
    )

    st.bar_chart(
        churn_data,
        x="Status",
        y="Members"
    )


# --------------------------------------------------
# ENGAGEMENT OVERVIEW
# --------------------------------------------------

with right_col:

    st.subheader("Engagement Overview")

    metric_a, metric_b = st.columns(2)

    with metric_a:
        st.metric(
            "Avg Class Frequency",
            "2.8 visits / week"
        )

    with metric_b:
        st.metric(
            "Current Month Frequency",
            "2.1 visits / week"
        )

    metric_c, metric_d = st.columns(2)

    with metric_c:
        st.metric(
            "Avg Contract Period",
            "4.6 months"
        )

    with metric_d:
        st.metric(
            "Group Visit Rate",
            "41%"
        )


st.write("")
st.divider()


# --------------------------------------------------
# AT-RISK MEMBERS
# --------------------------------------------------

st.subheader("At-Risk Members")

st.caption(
    "Members identified based on engagement and churn pattern analysis."
)


# Mock data for UI development.
# This will be replaced with real model output later.

risk_data = pd.DataFrame(
    {
        "Member ID": [
            "M1024",
            "M1048",
            "M1091",
            "M1105"
        ],
        "Contract Period": [
            "1 Month",
            "3 Months",
            "6 Months",
            "12 Months"
        ],
        "Engagement Level": [
            "Critical",
            "Declining",
            "Active",
            "Critical"
        ],
        "Churn Probability": [
            "87%",
            "74%",
            "42%",
            "12%"
        ],
        "Risk Status": [
            "🔴 High Risk",
            "🔴 High Risk",
            "🟡 Medium Risk",
            "🟢 Low Risk"
        ],
        "Action": [
            "Review",
            "Review",
            "Review",
            "Review"
        ]
    }
)

st.dataframe(
    risk_data,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.write("")

st.caption(
    "Fitness Retain AI • Customer Retention Analytics"
)