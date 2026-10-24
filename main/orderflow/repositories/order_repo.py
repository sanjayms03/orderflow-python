from orderflow.repositories.db import connect

def list_orders(path=None):
    db = connect(path)
    try:
        return [dict(row) for row in db.execute("SELECT * FROM orders ORDER BY id DESC")]
    finally:
        db.close()

def create_order(customer_id, total, path=None):
    db = connect(path)
    cur = db.execute("INSERT INTO orders(customer_id, total, status) VALUES (?, ?, ?)",
                     (customer_id, total, "created"))
    db.commit()
    result = {"id": cur.lastrowid, "customer_id": customer_id, "total": total, "status": "created"}
    db.close()
    return result
