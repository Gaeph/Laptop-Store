import sqlite3

DB_NAME = "laptops.db"

def get_connection():
    """Return a SQLite3 database connection."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    """Create tables for categories and laptops if they don't exist."""
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
            price REAL NOT NULL CHECK(price > 0),
            category_id INTEGER,
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )
    """)

    conn.commit()
    conn.close()
    print("Database tables created (if not exist).")

if __name__ == "__main__":
    create_tables()
