import json

from lambda_function.handler import lambda_handler


def test_lambda_high_prediction():
    event = {
        "features": [0.8, 0.7, 0.9]
    }

    response = lambda_handler(event, None)

    assert response["statusCode"] == 200

    body = json.loads(response["body"])

    assert body["prediction"] == "HIGH"
    assert body["score"] == 0.8


def test_lambda_low_prediction():
    event = {
        "features": [0.1, 0.2, 0.3]
    }

    response = lambda_handler(event, None)

    assert response["statusCode"] == 200

    body = json.loads(response["body"])

    assert body["prediction"] == "LOW"
    assert body["score"] == 0.2


def test_lambda_missing_features():
    event = {}

    response = lambda_handler(event, None)

    assert response["statusCode"] == 400

    body = json.loads(response["body"])

    assert body["error"] == "features are required"
