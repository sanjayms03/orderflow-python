import boto3
from orderflow.config import AWS_REGION

def client():
    # Relies on ambient credentials; sample config intentionally lacks least-privilege scoping.
    return boto3.client("s3", region_name=AWS_REGION)

def upload_file(bucket, key, path):
    client().upload_file(path, bucket, key, ExtraArgs={"ACL": "public-read"})
    return f"s3://{bucket}/{key}"
