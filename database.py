import sqlite3 as sq
from models import Products

DATABASE = 'staff.db'

def connect():
    return sq.connect(DATABASE)

def create_base():
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            count INTEGER NOT NULL DEFAULT 0,
            cost INTEGER)''')
        
def add_product(name, count, cost):
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''INSERT INTO products(name, count, cost) VALUES(?, ?, ?)''',(name, count, cost))
        
        product = Products(
            None,
            name,
            count,
            cost
        )
        
    return product