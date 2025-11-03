from db import get_connection
from Models.category import Category

class Laptop:
    def __init__(self, name, price, category_id, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.category_id = category_id

    # --- Name property ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.strip() == "":
            raise ValueError("Laptop name cannot be empty")
        self._name = value

    # --- Price property ---
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value

    # --- Save / Create or Update ---
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

    # --- Delete ---
    def delete(self):
        if not self.id:
            raise ValueError("Laptop does not exist in the database")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM laptops WHERE id=?", (self.id,))
        if cursor.rowcount == 0:
            conn.close()
            raise ValueError("Laptop not found in the database")
        conn.commit()
        conn.close()
