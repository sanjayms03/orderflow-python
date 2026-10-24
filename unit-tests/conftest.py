import pytest
@pytest.fixture
def sample_lines():
    return [{"price": "10.00", "quantity": 2}, {"price": "3.50", "quantity": 1}]
