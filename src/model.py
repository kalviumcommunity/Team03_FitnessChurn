import joblib
from pathlib import Path


MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "churn_model.pkl"
)


def load_model():
    return joblib.load(MODEL_PATH)