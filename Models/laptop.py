from db import CURSOR, CONN
from models.category import Category

class Laptop:
    def __init__(self, id: int | None, name: str, brand: str, price: float, stock: int, category_id: int):
        self.id = id
        self.name = name.strip()
        self.brand = brand.strip()
        self.price = float(price)
        self.stock = int(stock)
        self.category_id = int(category_id)
        self._validate()

    def __repr__(self) -> str:
        return f"<Laptop {self.id}: {self.name} ({self.brand}) - ${self.price} - Stock: {self.stock} - Category {self.category_id}>"

    def _validate(self):
        if not self.name:
            raise ValueError("Laptop name cannot be empty.")
        if not self.brand:
            raise ValueError("Laptop brand cannot be empty.")
        if self.price < 0:
            raise ValueError("Price must be >= 0.")
        if self.stock < 0:
            raise ValueError("Stock must be >= 0.")
        if not Category.find_by_id(self.category_id):
            raise ValueError(f"Category ID {self.category_id} does not exist.")

    @classmethod
    def create_table(cls) -> None:
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS laptops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                brand TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                category_id INTEGER NOT NULL,
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        """)
        CONN.commit()

    @classmethod
    def create(cls, name: str, brand: str, price: float, stock: int, category_id: int) -> "Laptop":
        laptop = cls(None, name, brand, price, stock, category_id)
        CURSOR.execute(
            "INSERT INTO laptops (name, brand, price, stock, category_id) VALUES (?, ?, ?, ?, ?)",
            (laptop.name, laptop.brand, laptop.price, laptop.stock, laptop.category_id)
        )
        CONN.commit()
        laptop.id = CURSOR.lastrowid
        return laptop

    @classmethod
    def get_all(cls) -> list["Laptop"]:
        rows = CURSOR.execute("SELECT id, name, brand, price, stock, category_id FROM laptops").fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id: int) -> "Laptop | None":
        row = CURSOR.execute(
            "SELECT id, name, brand, price, stock, category_id FROM laptops WHERE id=?", (id,)
        ).fetchone()
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id: int) -> bool:
        CURSOR.execute("DELETE FROM laptops WHERE id=?", (id,))
        CONN.commit()
        return CURSOR.rowcount > 0

    @classmethod
    def find_by_category(cls, category_id: int) -> list["Laptop"]:
        rows = CURSOR.execute(
            "SELECT id, name, brand, price, stock, category_id FROM laptops WHERE category_id=?", (category_id,)
        ).fetchall()
        return [cls(*row) for row in rows]
