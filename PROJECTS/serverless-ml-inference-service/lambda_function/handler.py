import json
import logging

from model.model import predict


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        body = event.get("body", event)

        if isinstance(body, str):
            body = json.loads(body)

        features = body.get("features")

        if not features:
            logger.warning("Prediction request missing features")

            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "features are required"
                })
            }

        result = predict(features)

        logger.info(
            "Prediction completed: prediction=%s score=%s",
            result["prediction"],
            result["score"]
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "prediction": result["prediction"],
                "score": result["score"]
            })
        }

    except Exception as e:
        logger.exception("Prediction request failed")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
