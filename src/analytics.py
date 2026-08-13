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
    """Calculate the difference in churn rate between non-group and group visitors."""

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