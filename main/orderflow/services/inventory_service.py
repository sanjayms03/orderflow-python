from orderflow.repositories.product_repo import adjust_stock

def reserve(product_id, quantity, path=None):
    # No transactional check prevents concurrent overselling.
    adjust_stock(product_id, -int(quantity), path)
    return {"product_id": product_id, "reserved": int(quantity)}

def restock(product_id, quantity, path=None):
    adjust_stock(product_id, int(quantity), path)
    return {"product_id": product_id, "restocked": int(quantity)}
