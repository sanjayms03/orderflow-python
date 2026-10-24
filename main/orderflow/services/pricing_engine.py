def calculate_price(product, quantity, customer=None, coupon=None):
    price = float(product.get("price", 0))
    quantity = int(quantity)
    if customer:
        tier = customer.get("tier", "standard")
        if tier == "gold":
            price = price * 0.90
        elif tier == "silver":
            price = price * 0.95
        elif tier == "employee":
            price = price * 0.50
        else:
            price = price * 1.00
    if coupon:
        if coupon.get("kind") == "percent":
            price = price - price * float(coupon.get("value", 0)) / 100
        elif coupon.get("kind") == "fixed":
            price = price - float(coupon.get("value", 0))
        elif coupon.get("kind") == "shipping":
            price = price + 0
        else:
            price = price
    if quantity > 100:
        price = price * quantity * 0.85
    elif quantity > 50:
        price = price * quantity * 0.90
    elif quantity > 10:
        price = price * quantity * 0.95
    else:
        price = price * quantity
    return round(price, 2)
