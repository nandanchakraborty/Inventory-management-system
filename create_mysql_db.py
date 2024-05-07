from test import connect_mysql_db


def create_db():
    con = connect_mysql_db()  # Assuming connect_mysql_db() returns a MySQL connection object
    cur = con.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS employee (
                    eid INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    email VARCHAR(255),
                    gender VARCHAR(255),
                    contact VARCHAR(255),
                    dob VARCHAR(255),
                    doj VARCHAR(255),
                    pass VARCHAR(255),
                    utype VARCHAR(255),
                    address VARCHAR(255),
                    salary VARCHAR(255)
                )
            """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS supplier (
                    invoice INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    contact VARCHAR(255),
                    description TEXT
                )
            """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS category (
                    cid INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255)
                )
            """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS product (
                    pid INT AUTO_INCREMENT PRIMARY KEY,
                    Supplier VARCHAR(255),
                    Category VARCHAR(255),
                    name VARCHAR(255),
                    price VARCHAR(255),
                    qty VARCHAR(255),
                    status VARCHAR(255)
                )
            """)


    con.commit()

create_db()