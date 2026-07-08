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
        
        product_id = cur.lastrowid
        
        product = Products(
            product_id,
            name,
            count,
            cost
        )
        
    return product

def find_by_id(product_id):
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''SELECT * FROM products WHERE product_id = ?''',(product_id,))
        
        for row in cur:
            product = Products(
                row['product_id'],
                row['name'],
                row['count'],
                row['cost']
            )
    return product

def new_count(product_id, delta):
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''UPDATE products SET cost = cost + ? WHERE product_id = ?''',(delta, product_id))
        cur.execute('''SELECT * FROM products WHERE product_id = ?''',(product_id,))
        
        for row in cur:
            product = Products(
                row['product_id'],
                row['name'],
                row['count'],
                row['cost']
            )
    return product

def new_cost(product_id, delta):
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''UPDATE products SET count = count + ? WHERE product_id = ?''',(delta, product_id))
        cur.execute('''SELECT * FROM products WHERE product_id = ?''',(product_id,))
        
        for row in cur:
            product = Products(
                row['product_id'],
                row['name'],
                row['count'],
                row['cost']
            )
    return product