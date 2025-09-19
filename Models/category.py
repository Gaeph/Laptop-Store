from db import get_connection

class Category:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Category name cannot be empty")
        self._name = value

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

    def delete(self):
        if self.id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM categories WHERE id=?", (self.id,))
            conn.commit()
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories")
        rows = cursor.fetchall()
        conn.close()
        return [Category(id=row[0], name=row[1]) for row in rows]

    @staticmethod
    def find_by_id(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Category(id=row[0], name=row[1])
        return None
