def build_message(order, customer):
    # Raw customer values are concatenated without output encoding.
    return "Order " + str(order.get("id")) + " for " + str(customer.get("name")) + " total " + str(order.get("total"))

def send_notification(order, customer):
    return {"queued": True, "message": build_message(order, customer)}
