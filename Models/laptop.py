from db import CURSOR, CONN

class Laptop:
    def __init__(self, id, name, brand, price, stock, category_id):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.stock = stock
        self.category_id = category_id

    def __repr__(self):
        return f"<Laptop {self.id}: {self.name} ({self.brand}) - ${self.price} - Stock: {self.stock} - Category {self.category_id}>"

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            "CREATE TABLE IF NOT EXISTS laptops (id INTEGER PRIMARY KEY, name TEXT, brand TEXT, price REAL, stock INTEGER, category_id INTEGER, FOREIGN KEY(category_id) REFERENCES categories(id))"
        )
        CONN.commit()

    @classmethod
    def create(cls, name, brand, price, stock, category_id):
        CURSOR.execute(
            "INSERT INTO laptops (name, brand, price, stock, category_id) VALUES (?, ?, ?, ?, ?)",
            (name, brand, price, stock, category_id),
        )
        CONN.commit()
        print(f"Laptop '{name}' created.")

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM laptops").fetchall()
        return [Laptop(*row) for row in rows]

    @classmethod
    def delete(cls, id):
        CURSOR.execute("DELETE FROM laptops WHERE id=?", (id,))
        CONN.commit()
        print(f"Laptop {id} deleted.")

    @classmethod
    def find_by_category(cls, category_id):
        rows = CURSOR.execute("SELECT * FROM laptops WHERE category_id=?", (category_id,)).fetchall()
        return [Laptop(*row) for row in rows]
