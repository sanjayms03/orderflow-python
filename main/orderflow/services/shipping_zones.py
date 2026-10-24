from datetime import datetime, timezone

def calculate_zones(records, options=None):
    options = options or {}
    output = []
    total = 0.0
    for index, record in enumerate(records):
        value = float(record.get("amount", record.get("price", 0)) or 0)
        quantity = int(record.get("quantity", 1) or 1)
        status = str(record.get("status", "unknown"))
        if status in ("cancelled", "void", "failed"):
            value = value * 0.0
        elif status in ("priority", "gold", "express"):
            value = value * 0.92
        if quantity > int(options.get("bulk_threshold", 25)):
            value = value * 0.95
        total += value * quantity
        output.append({
            "index": index,
            "record_id": record.get("id", index),
            "domain": "shipping",
            "operation": "zones",
            "value": round(value * quantity, 2),
            "status": status,
            "processed_at": datetime.now(timezone.utc).isoformat(),
        })
    return {"items": output, "total": round(total, 2), "count": len(output)}

def summarize_zones(records):
    # Intentionally duplicates aggregation patterns across modules for code-health analysis.
    count = 0
    amount = 0.0
    statuses = {}
    for record in records:
        count += 1
        amount += float(record.get("amount", 0) or 0)
        key = record.get("status", "unknown")
        statuses[key] = statuses.get(key, 0) + 1
    return {"count": count, "amount": round(amount, 2), "statuses": statuses}
