import json
import os
from product import Product
from inventory import Inventory

FILENAME = "inventory.json"


## ---------- file handling (for now it lives in the main program) ----------

def load_inventory(inventory):
    with open(FILENAME, "r") as file:
        records = json.load(file)
    for record in records:
        price = float(str(record["Price"]).replace("$", ""))   # older files stored prices like "$1200"
        inventory.add_product(Product(record["ID"], record["Name"], price, record["Stock"]))


def save_inventory(inventory):
    records = []
    for product in inventory.get_all_products():
        records.append({
            "ID": product.product_id,
            "Name": product.name,
            "Price": product.price,
            "Stock": product.stock
        })
    with open(FILENAME, "w") as file:
        json.dump(records, file, indent=4)


## ---------- menu and user input ----------

def data_representation(inventory):
    print("==================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("==================================================\n")

    if os.path.exists(FILENAME):
        load_inventory(inventory)
        print("inventory.json found")
        print("Inventory loaded successfully.\n")
    else:
        print("inventory.json not found. Creating a new inventory file...")
        inventory.add_product(Product("P001", "Laptop", 1200.00, 50))
        inventory.add_product(Product("P002", "Mouse", 25.50, 30))
        inventory.add_product(Product("P003", "Keyboard", 45.00, 20))
        save_inventory(inventory)
        print("New inventory file created successfully.\n")

    print("--------------MENU---------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------------\n")


def ask_whole_number(prompt):
    while True:
        text = input(prompt)
        if text.isdigit():
            return int(text)
        print("Please enter a whole number (0 or more).")


def ask_price(prompt):
    while True:
        text = input(prompt).replace("$", "").strip()
        try:
            price = float(text)
            if price >= 0:
                return price
        except ValueError:
            pass
        print("Please enter a valid price.")


def option_2(inventory):
    print("Add New Product")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = ask_price("Price: ")
    product_stock = ask_whole_number("Stock Quantity: ")
    product = Product(product_id, product_name, product_price, product_stock)
    if inventory.add_product(product):
        print("Product added successfully.\n")
        return True
    print("Product ID already exists.\n")
    return False


def option_3(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product is None:
        print("Product ID not found.\n")
        return False
    new_stock_quantity = ask_whole_number("New stock quantity: ")
    inventory.update_stock(product_id, new_stock_quantity)
    print("Stock updated successfully!\n")
    return True


def option_4(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product is None:
        print("Product ID not found.\n")
    else:
        print("\nProduct Found")
        print("---------------------------------")
        product.display_information()
        print("---------------------------------\n")


def option_5(inventory):
    print("Saving Inventory...")
    save_inventory(inventory)
    print("Inventory saved successfully.\n")


def main():
    inventory = Inventory()
    data_representation(inventory)
    unsaved_changes = False

    while True:
        user_input = input("Enter Option: ")

        if user_input == "1":
            inventory.display_all()
            print()
        elif user_input == "2":
            if option_2(inventory):
                unsaved_changes = True
        elif user_input == "3":
            if option_3(inventory):
                unsaved_changes = True
        elif user_input == "4":
            option_4(inventory)
        elif user_input == "5":
            option_5(inventory)
            unsaved_changes = False
        elif user_input == "6":
            if unsaved_changes:
                answer = input("You have unsaved changes. Save before exit? (y/n): ")
                if answer.strip().lower() == "y":
                    option_5(inventory)
            print("Thank you for using Inventory Management System.\nProgram terminated.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
