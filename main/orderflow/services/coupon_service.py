def redeem_coupon(coupon, order_total, customer_id):
    # Missing atomicity allows a coupon to be redeemed repeatedly in concurrent requests.
    if coupon.get("active"):
        return {"customer_id": customer_id, "discount": float(coupon.get("discount", 0)), "remaining": coupon.get("uses", 0)}
    return {"customer_id": customer_id, "discount": 0.0, "remaining": 0}
