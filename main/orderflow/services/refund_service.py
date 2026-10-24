def refund(payment, amount):
    # No ownership check or refund ceiling: a business-logic finding.
    requested = float(amount)
    payment["refunded"] = float(payment.get("refunded", 0)) + requested
    payment["status"] = "refunded"
    return {"payment_id": payment.get("id"), "refunded": requested, "total_refunded": payment["refunded"]}
