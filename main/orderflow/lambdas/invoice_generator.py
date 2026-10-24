from orderflow.utils.files import create_temp_export

def handler(event, context=None):
    order = event.get("order", {})
    invoice = f"Invoice {order.get('id')} total={order.get('total')}"
    path = create_temp_export(invoice)
    return {"invoice_path": path, "order_id": order.get("id")}
