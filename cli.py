from Models.category import Category
from Models.laptop import Laptop

def main_menu():
    while True:
        print("\n=== Laptop Store CLI ===")
        print("1. Manage Categories")
        print("2. Manage Laptops")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            category_menu()
        elif choice == "2":
            laptop_menu()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid option, try again.")

def category_menu():
    while True:
        print("\n--- Categories ---")
        print("1. Show all categories")
        print("2. Add category")
        print("3. Delete category")
        print("4. Show laptops in category")
        print("5. Back")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            for cat in Category.all():
                print(f"{cat.id}: {cat.name}")
        elif choice == "2":
            name = input("Category name: ").strip()
            try:
                Category.create(name)
                print("Category added.")
            except Exception as e:
                print(e)
        elif choice == "3":
            id = int(input("Category ID to delete: "))
            cat = Category.find_by_id(id)
            if cat:
                cat.delete()
                print("Category deleted.")
            else:
                print("Category not found.")
        elif choice == "4":
            id = int(input("Category ID: "))
            cat = Category.find_by_id(id)
            if cat:
                laptops = cat.laptops()
                if laptops:
                    for lap in laptops:
                        print(f"{lap.id}: {lap.name}, ${lap.price}")
                else:
                    print("No laptops in this category.")
            else:
                print("Category not found.")
        elif choice == "5":
            break
        else:
            print("Invalid option.")

def laptop_menu():
    while True:
        print("\n--- Laptops ---")
        print("1. Show all laptops")
        print("2. Add laptop")
        print("3. Delete laptop")
        print("4. Back")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            for lap in Laptop.all():
                cat = lap.category()
                cat_name = cat.name if cat else "Unknown"
                print(f"{lap.id}: {lap.name}, ${lap.price}, Category: {cat_name}")
        elif choice == "2":
            name = input("Laptop name: ").strip()
            price = float(input("Price: "))
            for cat in Category.all():
                print(f"{cat.id}: {cat.name}")
            category_id = int(input("Category ID: "))
            try:
                Laptop.create(name, price, category_id)
                print("Laptop added.")
            except Exception as e:
                print(e)
        elif choice == "3":
            id = int(input("Laptop ID to delete: "))
            lap = Laptop.find_by_id(id)
            if lap:
                lap.delete()
                print("Laptop deleted.")
            else:
                print("Laptop not found.")
        elif choice == "4":
            break
        else:
            print("Invalid option.")
