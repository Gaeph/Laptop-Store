from db import get_connection
from Models.category import Category

class Laptop:
    def __init__(self, name, price, category_id, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.category_id = category_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Laptop name cannot be empty")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute(
                "UPDATE laptops SET name=?, price=?, category_id=? WHERE id=?",
                (self.name, self.price, self.category_id, self.id)
            )
        else:
            cursor.execute(
                "INSERT INTO laptops (name, price, category_id) VALUES (?, ?, ?)",
                (self.name, self.price, self.category_id)
            )
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    def delete(self):
        if self.id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM laptops WHERE id=?", (self.id,))
            conn.commit()
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category_id FROM laptops")
        rows = cursor.fetchall()
        conn.close()
        return [Laptop(id=row[0], name=row[1], price=row[2], category_id=row[3]) for row in rows]

    @staticmethod
    def find_by_id(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category_id FROM laptops WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Laptop(id=row[0], name=row[1], price=row[2], category_id=row[3])
        return None
