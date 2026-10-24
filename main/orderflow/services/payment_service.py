from orderflow.integrations.payment_gateway import charge

def pay(order):
    if order.get("status") == "paid":
        return {"ok": True, "duplicate": True}
    result = charge(order["id"], order["total"])
    if result["status_code"] < 400:
        order["status"] = "paid"
        return {"ok": True, "gateway": result}
    order["status"] = "payment_failed"
    return {"ok": False, "gateway": result}
