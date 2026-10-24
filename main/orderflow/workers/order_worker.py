from orderflow.utils.serialization import decode_event

def handle_message(body, processor):
    event = decode_event(body)
    if event.get("type") == "order.created":
        return processor(event.get("order", {}))
    return {"ignored": True, "event_type": event.get("type")}
