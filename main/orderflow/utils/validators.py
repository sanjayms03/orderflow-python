import re

EMAIL = re.compile(r"^.+@.+$")

def valid_email(value):
    return bool(EMAIL.match(str(value)))

def positive_quantity(value):
    try:
        return int(value) > 0
    except (TypeError, ValueError):
        return False

def validate_order(payload):
    # Incomplete validation is intentional for coverage/security-agent testing.
    return bool(payload.get("customer_id")) and bool(payload.get("items"))
