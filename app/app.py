from pathlib import Path

import streamlit as st
import pandas as pd
import altair as alt


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

DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "cleaned_data.csv"
)

df = pd.read_csv(DATA_PATH)


# --------------------------------------------------
# LOAD ML PREDICTIONS
# --------------------------------------------------

PREDICTION_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "churn_predictions.csv"
)

predictions_df = pd.read_csv(PREDICTION_PATH)


# --------------------------------------------------
# DATA CALCULATIONS
# --------------------------------------------------

total_members = len(df)

churn_rate = df["Churn"].mean() * 100

average_lifetime = df["Lifetime"].mean()

average_class_frequency = (
    df["Avg_class_frequency_total"].mean()
)

current_month_frequency = (
    df["Avg_class_frequency_current_month"].mean()
)

average_contract_period = (
    df["Contract_period"].mean()
)

group_visit_rate = (
    df["Group_visits"].mean() * 100
)

churned_members = int(df["Churn"].sum())

retained_members = total_members - churned_members


# --------------------------------------------------
# ML RISK COUNTS
# --------------------------------------------------

high_risk_count = (
    predictions_df["risk_status"] == "High"
).sum()

medium_risk_count = (
    predictions_df["risk_status"] == "Medium"
).sum()

low_risk_count = (
    predictions_df["risk_status"] == "Low"
).sum()


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* --------------------------------------------------
       MAIN APP
    -------------------------------------------------- */

    .stApp {
        background-color: #f5f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* --------------------------------------------------
       SIDEBAR
       -------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: #f9fafb;
    }

    section[data-testid="stSidebar"] hr {
        border-color: #374151;
    }


    /* --------------------------------------------------
       SIDEBAR PAGE LINKS
       -------------------------------------------------- */

    section[data-testid="stSidebar"] a {
        border-radius: 8px;
        padding: 8px 10px;
    }


    /* --------------------------------------------------
       HEADINGS
       -------------------------------------------------- */

    h1 {
        color: #111827;
        font-weight: 700;
    }

    h2 {
        color: #111827;
        font-weight: 650;
    }

    h3 {
        color: #1f2937;
        font-weight: 600;
    }


    /* --------------------------------------------------
       CAPTIONS
       -------------------------------------------------- */

    .stCaption {
        color: #6b7280;
    }


    /* --------------------------------------------------
       KPI CARDS
       -------------------------------------------------- */

    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 20px 20px 18px 20px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    div[data-testid="stMetric"] label {
        color: #6b7280 !important;
        font-weight: 500 !important;
    }

    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #111827 !important;
        font-weight: 700 !important;
    }

    div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
        color: #6b7280 !important;
    }


    /* --------------------------------------------------
       DATAFRAME
       -------------------------------------------------- */

    div[data-testid="stDataFrame"] {
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        overflow: hidden;
    }


    /* --------------------------------------------------
       INFO / ALERT BOXES
       -------------------------------------------------- */

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }


    /* --------------------------------------------------
       DIVIDERS
       -------------------------------------------------- */

    hr {
        border-color: #e5e7eb;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div style="margin-bottom: 5px;">
            <h2 style="
                color: white;
                margin-bottom: 4px;
                font-size: 24px;
            ">
                📊 Retain AI
            </h2>

            <p style="
                color: #9ca3af;
                margin-top: 0px;
                font-size: 14px;
            ">
                Fitness Retention Analytics
            </p>
        </div>
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

    st.markdown(
        """
        <div style="
            color: #9ca3af;
            font-size: 13px;
            margin-top: 20px;
        ">
            ⚙️ Settings
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            margin-top: 40px;
            padding: 10px;
            color: #d1d5db;
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
        value=f"{high_risk_count:,}"
    )


st.write("")

st.divider()


# --------------------------------------------------
# CHURN + ENGAGEMENT OVERVIEW
# --------------------------------------------------

left_col, right_col = st.columns(
    [1.4, 1],
    gap="large"
)


# --------------------------------------------------
# CHURN OVERVIEW
# --------------------------------------------------

with left_col:

    st.subheader("Churn Overview")

    churn_data = pd.DataFrame(
        {
            "Status": [
                "Retained",
                "Churned"
            ],
            "Members": [
                retained_members,
                churned_members
            ]
        }
    )

    churn_chart = (
        alt.Chart(churn_data)
        .mark_bar(
            cornerRadiusTopLeft=6,
            cornerRadiusTopRight=6
        )
        .encode(
            x=alt.X(
                "Status:N",
                title=None,
                axis=alt.Axis(
                    labelColor="#4b5563",
                    labelFontSize=12
                )
            ),
            y=alt.Y(
                "Members:Q",
                title="Members",
                axis=alt.Axis(
                    labelColor="#6b7280",
                    titleColor="#4b5563"
                )
            ),
            tooltip=[
                alt.Tooltip(
                    "Status:N",
                    title="Status"
                ),
                alt.Tooltip(
                    "Members:Q",
                    title="Members"
                )
            ]
        )
        .properties(
            height=330,
            background="#ffffff"
        )
    )

    st.altair_chart(
        churn_chart,
        use_container_width=True
    )


# --------------------------------------------------
# ENGAGEMENT OVERVIEW
# --------------------------------------------------

with right_col:

    st.subheader("Engagement Overview")

    st.metric(
        "Avg Class Frequency",
        f"{average_class_frequency:.1f} visits / week"
    )

    st.write("")

    st.metric(
        "Current Month Frequency",
        f"{current_month_frequency:.1f} visits / week"
    )

    st.write("")

    st.metric(
        "Avg Contract Period",
        f"{average_contract_period:.1f} months"
    )

    st.write("")

    st.metric(
        "Group Visit Rate",
        f"{group_visit_rate:.1f}%"
    )


st.write("")

st.divider()


# --------------------------------------------------
# AT-RISK MEMBERS
# --------------------------------------------------

st.subheader("At-Risk Members")

st.caption(
    "Members identified as having a high predicted churn risk."
)


at_risk_members = predictions_df[
    predictions_df["risk_status"] == "High"
].copy()


at_risk_members = at_risk_members.sort_values(
    "churn_probability",
    ascending=False
)


if at_risk_members.empty:

    st.info(
        "No high-risk members were identified."
    )

else:

    display_data = at_risk_members[
        [
            "Contract_period",
            "engagement_level",
            "churn_probability",
            "risk_status"
        ]
    ].copy()

    display_data["churn_probability"] = (
        display_data["churn_probability"] * 100
    ).round(1).astype(str) + "%"

    display_data = display_data.rename(
        columns={
            "Contract_period":
                "Contract Period",

            "engagement_level":
                "Engagement Level",

            "churn_probability":
                "Churn Probability",

            "risk_status":
                "Risk Status"
        }
    )

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )


# --------------------------------------------------
# RISK SUMMARY
# --------------------------------------------------

st.write("")

risk_col1, risk_col2, risk_col3 = st.columns(3)


with risk_col1:

    st.metric(
        "High Risk",
        f"{high_risk_count:,}"
    )


with risk_col2:

    st.metric(
        "Medium Risk",
        f"{medium_risk_count:,}"
    )


with risk_col3:

    st.metric(
        "Low Risk",
        f"{low_risk_count:,}"
    )