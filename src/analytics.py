import pandas as pd


DATA_PATH = "data/processed/cleaned_data.csv"


def load_data(path=DATA_PATH):
    """Load the cleaned fitness churn dataset."""
    return pd.read_csv(path)


def churn_rate_by_contract(df):
    """Calculate churn rate for each contract period."""

    result = (
        df.groupby("Contract_period")["Churn"]
        .mean()
        .reset_index()
    )

    result["Churn Rate"] = result["Churn"] * 100

    result = result.rename(
        columns={"Contract_period": "Contract Period"}
    )

    return result[["Contract Period", "Churn Rate"]]


def churn_rate_by_group_visits(df):
    """Compare churn rates for members with and without group visits."""

    result = (
        df.groupby("Group_visits")["Churn"]
        .mean()
        .reset_index()
    )

    result["Churn Rate"] = result["Churn"] * 100

    result["Group Visits"] = result["Group_visits"].map({
        1: "Group Visits",
        0: "No Group Visits"
    })

    return result[["Group Visits", "Churn Rate"]]


def engagement_churn_relationship(df):
    """Analyse the relationship between class frequency and churn."""

    result = (
        df.groupby("Churn")["Avg_class_frequency_current_month"]
        .mean()
        .reset_index()
    )

    result["Churn Status"] = result["Churn"].map({
        0: "Retained",
        1: "Churned"
    })

    return result[
        [
            "Churn Status",
            "Avg_class_frequency_current_month"
        ]
    ]


def lifetime_churn_relationship(df):
    """Analyse average member lifetime by churn status."""

    result = (
        df.groupby("Churn")["Lifetime"]
        .mean()
        .reset_index()
    )

    result["Churn Status"] = result["Churn"].map({
        0: "Retained",
        1: "Churned"
    })

    return result[
        [
            "Churn Status",
            "Lifetime"
        ]
    ]


def group_visit_retention_difference(df):
    """Calculate the difference in churn rate between
    non-group and group visitors.
    """

    result = churn_rate_by_group_visits(df)

    group_churn = result.loc[
        result["Group Visits"] == "Group Visits",
        "Churn Rate"
    ].iloc[0]

    no_group_churn = result.loc[
        result["Group Visits"] == "No Group Visits",
        "Churn Rate"
    ].iloc[0]

    return no_group_churn - group_churn


def get_insights(df):
    """Return data-backed retention insights for the dashboard."""

    contract = churn_rate_by_contract(df)
    group = churn_rate_by_group_visits(df)
    engagement = engagement_churn_relationship(df)
    lifetime = lifetime_churn_relationship(df)

    # Highest churn contract period
    highest_contract = contract.loc[
        contract["Churn Rate"].idxmax()
    ]

    # Group visit churn
    group_churn = group.loc[
        group["Group Visits"] == "Group Visits",
        "Churn Rate"
    ].iloc[0]

    no_group_churn = group.loc[
        group["Group Visits"] == "No Group Visits",
        "Churn Rate"
    ].iloc[0]

    # Engagement
    retained_frequency = engagement.loc[
        engagement["Churn Status"] == "Retained",
        "Avg_class_frequency_current_month"
    ].iloc[0]

    churned_frequency = engagement.loc[
        engagement["Churn Status"] == "Churned",
        "Avg_class_frequency_current_month"
    ].iloc[0]

    # Lifetime
    retained_lifetime = lifetime.loc[
        lifetime["Churn Status"] == "Retained",
        "Lifetime"
    ].iloc[0]

    churned_lifetime = lifetime.loc[
        lifetime["Churn Status"] == "Churned",
        "Lifetime"
    ].iloc[0]

    return {
        "contract": (
            f"{int(highest_contract['Contract Period'])}-month contracts "
            f"have the highest observed churn at "
            f"{highest_contract['Churn Rate']:.2f}%."
        ),

        "group_visits": (
            f"Members with group visits have {group_churn:.2f}% churn "
            f"compared with {no_group_churn:.2f}% without group visits."
        ),

        "engagement": (
            f"Retained members average {retained_frequency:.2f} visits "
            f"per month compared with {churned_frequency:.2f} "
            f"for churned members."
        ),

        "lifetime": (
            f"Retained members have an average lifetime of "
            f"{retained_lifetime:.2f} months compared with "
            f"{churned_lifetime:.2f} months for churned members."
        )
    }