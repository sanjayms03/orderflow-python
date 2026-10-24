import json
import boto3
from orderflow.config import AWS_REGION

def send(queue_url, payload):
    return boto3.client("sqs", region_name=AWS_REGION).send_message(
        QueueUrl=queue_url, MessageBody=json.dumps(payload))
