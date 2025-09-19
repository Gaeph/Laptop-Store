from cli import main_menu
from models.category import Category
from models.laptop import Laptop

if __name__ == "__main__":
    # Create tables if not exist
    Category.create_table()
    Laptop.create_table()
    main_menu()
