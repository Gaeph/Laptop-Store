from db import get_connection
from Models.laptop import Laptop

class Category:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Category name cannot be empty")
        self._name = value

    # --- ORM Methods ---
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE categories SET name=? WHERE id=?", (self.name, self.id))
        else:
            cursor.execute("INSERT INTO categories (name) VALUES (?)", (self.name,))
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return self

    def delete(self):
        if not self.id:
            raise ValueError("Category does not exist in DB.")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categories WHERE id=?", (self.id,))
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, name):
        cat = cls(name)
        cat.save()
        return cat

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories")
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1])
        return None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories WHERE name=?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1])
        return None

    # --- Related Objects ---
    def laptops(self):
        return Laptop.find_by_category_id(self.id)
