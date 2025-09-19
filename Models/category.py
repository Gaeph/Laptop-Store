from db import CURSOR, CONN

class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            "CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, name TEXT UNIQUE)"
        )
        CONN.commit()

    @classmethod
    def create(cls, name):
        CURSOR.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        CONN.commit()
        print(f"Category '{name}' created.")

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM categories").fetchall()
        return [Category(*row) for row in rows]

    @classmethod
    def delete(cls, id):
        CURSOR.execute("DELETE FROM categories WHERE id=?", (id,))
        CONN.commit()
        print(f"Category {id} deleted.")
