from model.model import predict


def test_high_prediction():
    result = predict([0.8, 0.7, 0.9])

    assert result["prediction"] == "HIGH"
    assert result["score"] == 0.8


def test_low_prediction():
    result = predict([0.1, 0.2, 0.3])

    assert result["prediction"] == "LOW"
    assert result["score"] == 0.2
