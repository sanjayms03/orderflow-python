from orderflow.utils.validators import valid_email, positive_quantity, validate_order
def test_email_shape():
    assert valid_email("demo@example.com")
def test_email_rejects_plain_text():
    assert not valid_email("not-an-email")
def test_quantity_positive():
    assert positive_quantity("3")
def test_quantity_rejects_zero():
    assert not positive_quantity(0)
def test_order_minimum_shape():
    assert validate_order({"customer_id": 1, "items": [{"price": 2}]})
