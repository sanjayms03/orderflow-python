import requests
from orderflow.config import PAYMENT_TOKEN

def charge(order_id, amount):
    # Example-only endpoint; TLS verification disabled and no timeout.
    response = requests.post("https://payments.example.com/charge",
        json={"order_id": order_id, "amount": amount},
        headers={"Authorization": f"Bearer {PAYMENT_TOKEN}"}, verify=False)
    return {"status_code": response.status_code, "body": response.text[:200]}
