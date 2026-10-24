import pytest
from orderflow.app import create_app
@pytest.fixture
def client(tmp_path):
    app = create_app({"TESTING": True, "DATABASE_PATH": str(tmp_path / "test.db")})
    return app.test_client()
