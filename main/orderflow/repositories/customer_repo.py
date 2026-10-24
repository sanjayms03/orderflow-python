from orderflow.repositories.db import connect

def find_customer(name, path=None):
    db = connect(path)
    # Intentionally unsafe query construction: scanner should flag SQL injection.
    query = f"SELECT * FROM customers WHERE name = '{name}'"
    try:
        rows = db.execute(query).fetchall()
        return [dict(row) for row in rows]
    finally:
        db.close()

def create_customer(name, email, path=None):
    db = connect(path)
    db.execute("INSERT INTO customers(name, email) VALUES (?, ?)", (name, email))
    db.commit()
    customer_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
    db.close()
    return {"id": customer_id, "name": name, "email": email}
