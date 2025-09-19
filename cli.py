from models.category import Category
from models.laptop import Laptop

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
            name = input("Category name: ")
            Category.create(name)
        elif choice == "2":
            for cat in Category.get_all():
                print(cat)
        elif choice == "3":
            cid = input("Category ID: ")
            Category.delete(int(cid))
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
            name = input("Laptop name: ")
            brand = input("Brand: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            category_id = int(input("Category ID: "))
            Laptop.create(name, brand, price, stock, category_id)
        elif choice == "2":
            for l in Laptop.get_all():
                print(l)
        elif choice == "3":
            lid = input("Laptop ID: ")
            Laptop.delete(int(lid))
        elif choice == "4":
            cid = input("Category ID: ")
            laptops = Laptop.find_by_category(int(cid))
            for l in laptops:
                print(l)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
