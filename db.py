import sqlite3

# Koneksyon ak baz done SQLite
CONN = sqlite3.connect("laptops.db")
CONN.execute("PRAGMA foreign_keys = ON;")  # aktive foreign keys
CURSOR = CONN.cursor()
