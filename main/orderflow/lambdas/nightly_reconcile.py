def handler(event, context=None):
    rows = event.get("payments", [])
    discrepancies = []
    for row in rows:
        if float(row.get("captured", 0)) != float(row.get("expected", 0)):
            discrepancies.append({"payment_id": row.get("id"), "delta": float(row.get("captured", 0))-float(row.get("expected", 0))})
    return {"checked": len(rows), "discrepancies": discrepancies}
