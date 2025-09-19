from db import CURSOR, CONN
import sqlite3

class Category:
    def __init__(self, id: int | None, name: str):
        self.id = id
        self.name = name.strip()
        self._validate()

    def __repr__(self) -> str:
        return f"<Category {self.id}: {self.name}>"

    def _validate(self):
        if not self.name:
            raise ValueError("Category name cannot be empty.")

    @classmethod
    def create_table(cls) -> None:
        CURSOR.execute(
            "CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)"
        )
        CONN.commit()

    @classmethod
    def create(cls, name: str) -> "Category":
        try:
            CURSOR.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            CONN.commit()
            return cls(CURSOR.lastrowid, name)
        except sqlite3.IntegrityError:
            raise ValueError(f"Category '{name}' already exists.")

    @classmethod
    def get_all(cls) -> list["Category"]:
        rows = CURSOR.execute("SELECT id, name FROM categories").fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id: int) -> "Category | None":
        row = CURSOR.execute("SELECT id, name FROM categories WHERE id=?", (id,)).fetchone()
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id: int) -> bool:
        CURSOR.execute("DELETE FROM categories WHERE id=?", (id,))
        CONN.commit()
        return CURSOR.rowcount > 0
