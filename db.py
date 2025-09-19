import sqlite3

def get_connection():
    conn = sqlite3.connect("laptops.db")
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS laptops (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )
    """)

    conn.commit()
    conn.close()
