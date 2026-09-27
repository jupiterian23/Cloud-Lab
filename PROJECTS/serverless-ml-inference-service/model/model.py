import json
from pathlib import Path


CONFIG_PATH = Path(__file__).parent / "model_config.json"


def load_model():
    """Load the trained model configuration."""

    with open(CONFIG_PATH, "r") as file:
        return json.load(file)


def predict(features):
    """Run inference using the trained model configuration."""

    model = load_model()
    threshold = model["threshold"]

    score = sum(features) / len(features)

    prediction = "HIGH" if score >= threshold else "LOW"

    return {
        "prediction": prediction,
        "score": round(score, 4)
    }
