import json
import os
from product import Product
from inventory import Inventory
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from supplier import Supplier
from productfactory import ProductFactory
from order import Order
from orderline import OrderLine
from discount import PercentageDiscount, BulkDiscount

FILENAME = "inventory.json"


## ---------- file handling (for now it lives in the main program) ----------

def get_positive_float(prompt: str) -> float: 
    while True: 
        try: 
            value = float(input(prompt)) 
            if value <= 0: 
                print("Please enter a number greater than zero.") 
                continue 
            return value 
        except ValueError: 
            print("Please enter a valid number, e.g. 12.50") 

def load_inventory(inventory):
    supplier1 = Supplier("S001", "ABC Company", "abc@company.com")
    with open(FILENAME, "r") as file:
        records = json.load(file)
    for record in records:
        product_id = record["ID"]
        name = record["Name"]
        price = record["Price"]
        stock = record["Stock"]

        supplier_id = record["Supplier ID"]
        supplier_name = record["Supplier Name"]
        supplier_email = record["Supplier Email"]
        supplier1 = Supplier(supplier_id, supplier_name, supplier_email)

        if record["Type"] == "P":
            extra_value = record["Weight"]
            product = PhysicalProduct(product_id, name, price, stock, supplier1, extra_value)
        elif record["Type"] == "D":
            extra_value = record["File Size"]
            product = DigitalProduct(product_id, name, price, stock, supplier1, extra_value)
        else:
            continue  # skip unknown product types

        inventory.add_product(product)


def save_inventory(inventory):
    records = []

    for product in inventory.get_all_products():
        record = {
            "ID": product.product_id,
            "Name": product.name,
            "Price": product.price,
            "Stock": product.stock,
            "Supplier ID": product.supplier.supplier_id,
            "Supplier Name": product.supplier.supplier_name,
            "Supplier Email": product.supplier.supplier_email
        }

        if isinstance(product, PhysicalProduct):
            record["Type"] = "P"
            record["Weight"] = product.extra_value

        elif isinstance(product, DigitalProduct):
            record["Type"] = "D"
            record["File Size"] = product.extra_value

        records.append(record)

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
        save_inventory(inventory)
        print("New inventory file created successfully.\n")

    print("--------------MENU---------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Remove Product")
    print("5. Search Product")
    print("6. Save Inventory")
    print("7. Create Order")
    print("8. Exit")
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
    print("Add New Product, (P)hysical or (D)igital?")
    product_type = input("Enter type (P/D): ").strip().upper()

    if product_type not in ("P", "D"):
        print("Invalid product type.\n")
        return False

    product_id = input("Product ID: ")
    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.\n")
        return False
    
    product_name = input("Product Name: ")
    product_price = get_positive_float("Price: ")
    product_stock = ask_whole_number("Stock Quantity: ")
    supplier1 = Supplier("S001", "ABC Company", "abc@company.com")

    if product_type == "P":
        extra_value = ask_whole_number("Weight (kg): ")
        factory_type="physical"
    else:
        extra_value = ask_whole_number("File Size (MB): ")
        factory_type="digital"

    product = ProductFactory.create(factory_type, product_id, product_name, product_price, product_stock, supplier1, extra_value)

    if inventory.add_product(product):
        print("Product added successfully.\n")
        return True


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
    print("Remove Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product is None:
            print("Product ID not found.\n")
            return False
    inventory.remove_product(product_id)
    print("Product removed successfully.\n")
    return True

def option_5(inventory):
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


def option_6(inventory):
    print("Saving Inventory...")
    save_inventory(inventory)
    print("Inventory saved successfully.\n")

def option_7(inventory):
    print("Create New Order")

    order_id = input("Enter Order ID: ")
    order = Order(order_id)

    while True:
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)

        if product is None:
            print("Product ID not found.")
            continue

        quantity = ask_whole_number("Enter quantity: ")

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        order_line = OrderLine(product, quantity)
        order.add_order_line(product, quantity)

        answer = input("Add another product? (y/n): ")

        if answer.strip().lower() != "y":
            break

    order.display_order()
    order.set_discount(PercentageDiscount(10))
    print(f"10% Discount applied: ${order.calculate_total():.2f}")
    order.set_discount(BulkDiscount(200,50))
    print(f"Bulk Discount applied (if elligible): ${order.calculate_total():.2f}")

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
        elif user_input == "6":
            option_6(inventory)
            unsaved_changes = False
        elif user_input == "7":
            option_7(inventory)
        elif user_input == "8":
            if unsaved_changes:
                answer = input("You have unsaved changes. Save before exit? (y/n): ")
                if answer.strip().lower() == "y":
                    option_6(inventory)
            print("Thank you for using Inventory Management System.\nProgram terminated.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
