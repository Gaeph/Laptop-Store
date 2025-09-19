from models.category import Category
from models.laptop import Laptop

def get_valid_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main_menu():
    while True:
        print("\n=== Laptop Store CLI ===")
        print("1. Manage Categories")
        print("2. Manage Laptops")
        print("0. Exit")
        choice = input("> ")

        if choice == "1":
            category_menu()
        elif choice == "2":
            laptop_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

def category_menu():
    while True:
        print("\n--- Categories ---")
        print("1. Add Category")
        print("2. View All Categories")
        print("3. Delete Category")
        print("0. Back")
        choice = input("> ")

        if choice == "1":
            name = input("Category name: ").strip()
            if not name:
                print("Category name cannot be empty.")
                continue
            try:
                cat = Category.create(name)
                print(f"Category '{cat.name}' created with ID {cat.id}.")
            except ValueError as e:
                print(e)
        elif choice == "2":
            cats = Category.get_all()
            if not cats:
                print("No categories found.")
            else:
                for c in cats:
                    print(c)
        elif choice == "3":
            cid = get_valid_int("Category ID to delete: ")
            if Category.delete(cid):
                print(f"Category {cid} deleted successfully.")
            else:
                print("Category not found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def laptop_menu():
    while True:
        print("\n--- Laptops ---")
        print("1. Add Laptop")
        print("2. View All Laptops")
        print("3. Delete Laptop")
        print("4. View Laptops by Category")
        print("0. Back")
        choice = input("> ")

        if choice == "1":
            name = input("Laptop name: ").strip()
            brand = input("Brand: ").strip()
            price = get_valid_float("Price: ")
            stock = get_valid_int("Stock: ")
            category_id = get_valid_int("Category ID: ")

            if not Category.find_by_id(category_id):
                print("Category ID not found. Cannot create laptop.")
                continue

            try:
                laptop = Laptop.create(name, brand, price, stock, category_id)
                print(f"Laptop '{laptop.name}' created with ID {laptop.id}.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            laptops = Laptop.get_all()
            if not laptops:
                print("No laptops found.")
            else:
                for l in laptops:
                    print(l)

        elif choice == "3":
            lid = get_valid_int("Laptop ID to delete: ")
            if Laptop.delete(lid):
                print(f"Laptop {lid} deleted successfully.")
            else:
                print("Laptop not found.")

        elif choice == "4":
            cid = get_valid_int("Category ID: ")
            cat = Category.find_by_id(cid)
            if not cat:
                print("Category not found.")
                continue
            laptops = Laptop.find_by_category(cid)
            if not laptops:
                print(f"No laptops in category '{cat.name}'.")
            else:
                print(f"Laptops in category '{cat.name}':")
                for l in laptops:
                    print(l)

        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
