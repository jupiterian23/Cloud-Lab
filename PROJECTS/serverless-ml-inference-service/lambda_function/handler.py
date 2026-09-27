import json
from model.model import predict


def lambda_handler(event, context):
    try:
        body = event.get("body", event)

        if isinstance(body, str):
            body = json.loads(body)

        features = body.get("features")

        if not features:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "features are required"
                })
            }

        result = predict(features)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "prediction": result["prediction"],
                "score": result["score"]
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
