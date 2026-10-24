import sqlite3
from orderflow.config import DATABASE_PATH

def connect(path=None):
    conn = sqlite3.connect(path or DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def bootstrap(path=None):
    db = connect(path)
    db.executescript('''
        CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT, email TEXT);
        CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER);
        CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, customer_id INTEGER, total REAL, status TEXT);
    ''')
    db.execute("INSERT OR IGNORE INTO products VALUES (1, 'Demo Widget', 19.95, 50)")
    db.commit()
    db.close()
