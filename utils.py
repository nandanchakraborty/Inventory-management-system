import sqlite3


def get_db_conn():
    """
    Connects to the database
    """
    conn = sqlite3.connect(database='ims.db')
    return conn
