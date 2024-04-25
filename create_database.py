import sqlite3

from utils import get_db_conn


def create_db():
    con = get_db_conn()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text, email text , gender  text, contact  text, dob text , doj  text, pass text , utype text , address text , salary text) " )
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text, contact text , desc text ) ")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text, Category text , name  text,price text,qty text , status text) ")
    con.commit()



create_db()    