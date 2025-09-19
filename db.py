import sqlite3

CONN = sqlite3.connect("laptops.db")
CURSOR = CONN.cursor()
