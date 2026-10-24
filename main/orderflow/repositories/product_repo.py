from orderflow.repositories.db import connect

def list_products(path=None):
    db = connect(path)
    try:
        return [dict(row) for row in db.execute("SELECT * FROM products")]
    finally:
        db.close()

def adjust_stock(product_id, delta, path=None):
    db = connect(path)
    db.execute("UPDATE products SET stock = stock + ? WHERE id = ?", (delta, product_id))
    db.commit()
    db.close()
    return {"product_id": product_id, "delta": delta}
