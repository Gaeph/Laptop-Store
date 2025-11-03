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
        if not value.strip():
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

    # --- ORM Methods ---
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
        return self

    def delete(self):
        if not self.id:
            raise ValueError("Laptop does not exist in DB.")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM laptops WHERE id=?", (self.id,))
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, name, price, category_id):
        lap = cls(name, price, category_id)
        lap.save()
        return lap

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category_id FROM laptops")
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], price=row[2], category_id=row[3]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category_id FROM laptops WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1], price=row[2], category_id=row[3])
        return None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category_id FROM laptops WHERE name=?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1], price=row[2], category_id=row[3])
        return None

    @classmethod
    def find_by_category_id(cls, category_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category_id FROM laptops WHERE category_id=?", (category_id,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], price=row[2], category_id=row[3]) for row in rows]

    # --- Related Object ---
    def category(self):
        return Category.find_by_id(self.category_id)
