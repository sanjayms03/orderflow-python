import json
from orderflow.services.order_service import submit_order

def handler(event, context=None):
    payload = json.loads(event.get("body", "{}")) if isinstance(event.get("body"), str) else event
    return {"statusCode": 201, "body": json.dumps(submit_order(payload))}
