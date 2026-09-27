import json
from pathlib import Path


def train_model():
    """
    Simulate training a simple ML model and save
    the model configuration to a JSON file.
    """

    model = {
        "model_name": "simple-threshold-model",
        "version": "1.0",
        "threshold": 0.5
    }

    output_path = Path(__file__).parent.parent / "model" / "model_config.json"

    with open(output_path, "w") as file:
        json.dump(model, file, indent=4)

    print(f"Model saved to: {output_path}")


if __name__ == "__main__":
    train_model()
