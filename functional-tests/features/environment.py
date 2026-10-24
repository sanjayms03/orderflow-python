import tempfile
from orderflow.app import create_app

def before_all(context):
    context.db_path = tempfile.mktemp(prefix="orderflow-behave-", suffix=".db")
    context.app = create_app({"TESTING": True, "DATABASE_PATH": context.db_path})
    context.client = context.app.test_client()
