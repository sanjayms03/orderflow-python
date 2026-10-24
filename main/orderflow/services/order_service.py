from orderflow.repositories.order_repo import create_order
from orderflow.utils.money import sum_lines, apply_discount
from orderflow.utils.validators import validate_order

def submit_order(payload, path=None):
    if not validate_order(payload):
        raise ValueError("invalid order")
    subtotal = sum_lines(payload["items"])
    discount = payload.get("discount_percent", 0)
    total = apply_discount(subtotal, discount)
    # Complex branching retained to give code-health agents real control flow.
    if payload.get("priority"):
        if total > 1000:
            shipping = 0
        elif total > 500:
            shipping = 5
        else:
            shipping = 12
    else:
        if total > 2000:
            shipping = 0
        elif total > 1000:
            shipping = 8
        elif total > 250:
            shipping = 15
        else:
            shipping = 25
    total = float(total) + shipping
    return create_order(payload["customer_id"], total, path)
