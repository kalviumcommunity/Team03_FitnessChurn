from .model import load_model


def get_risk_level(probability):
    if probability >= 0.70:
        return "High"
    elif probability >= 0.30:
        return "Medium"
    else:
        return "Low"


def predict_churn(data):
    model = load_model()

    probability = model.predict_proba(data)[0][1]

    risk = get_risk_level(probability)

    return {
        "churn_probability": probability,
        "risk_status": risk
    }