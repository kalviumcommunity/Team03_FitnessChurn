from pathlib import Path
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
# LOAD CLEANED DATA
# --------------------------------------------------

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "processed" / "cleaned_data.csv"

df = pd.read_csv(DATA_PATH)
# --------------------------------------------------
# DATA CALCULATIONS
# --------------------------------------------------

total_members = len(df)

churn_rate = df["Churn"].mean() * 100

average_lifetime = df["Lifetime"].mean()

average_class_frequency = df["Avg_class_frequency_total"].mean()

current_month_frequency = df[
    "Avg_class_frequency_current_month"
].mean()

average_contract_period = df[
    "Contract_period"
].mean()

group_visit_rate = df["Group_visits"].mean() * 100

churned_members = df["Churn"].sum()

retained_members = total_members - churned_members
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
# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Members",
        value=f"{total_members:,}"
    )

with col2:
    st.metric(
        label="Overall Churn Rate",
        value=f"{churn_rate:.1f}%"
    )

with col3:
    st.metric(
        label="Avg Member Lifetime",
        value=f"{average_lifetime:.1f} mo"
    )

with col4:
    st.metric(
        label="High-Risk Members",
        value="Pending Model"
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

    # --------------------------------------------------
# CHURN OVERVIEW
# --------------------------------------------------

churn_data = pd.DataFrame({
    "Status": ["Retained", "Churned"],
    "Members": [
        retained_members,
        churned_members
    ]
})

st.bar_chart(
    churn_data,
    x="Status",
    y="Members"
)

# --------------------------------------------------
## --------------------------------------------------
# ENGAGEMENT OVERVIEW
# --------------------------------------------------

metric_a, metric_b = st.columns(2)

with metric_a:
    st.metric(
        "Avg Class Frequency",
        f"{average_class_frequency:.1f} visits / week"
    )

with metric_b:
    st.metric(
        "Current Month Frequency",
        f"{current_month_frequency:.1f} visits / week"
    )

metric_c, metric_d = st.columns(2)

with metric_c:
    st.metric(
        "Avg Contract Period",
        f"{average_contract_period:.1f} months"
    )

with metric_d:
    st.metric(
        "Group Visit Rate",
        f"{group_visit_rate:.1f}%"
    )
# --------------------------------------------------
# --------------------------------------------------
# AT-RISK MEMBERS
# --------------------------------------------------

st.subheader("At-Risk Members")

st.caption(
    "Members identified through the churn prediction model."
)

st.info(
    "Churn risk predictions will appear here once the "
    "machine learning model is integrated."
)