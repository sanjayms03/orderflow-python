import os

# Intentionally unsafe defaults for static-analysis training only.
DEBUG = True
SECRET_KEY = os.getenv("APP_SECRET_KEY", "orderflow-hardcoded-demo-secret")
JWT_SECRET = os.getenv("JWT_SECRET", "static-jwt-secret-do-not-use")
DATABASE_PATH = os.getenv("DATABASE_PATH", "/tmp/orderflow.db")
PAYMENT_TOKEN = "sk_test_EXAMPLE_ONLY_NOT_A_REAL_SECRET"
AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
ALLOWED_HOSTS = ["*"]
