from product import Product
from supplier import Supplier
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct
from inventory import Inventory
from orderline import OrderLine
from order import Order


def test_supplier_display_information():

    supplier1 = Supplier("S001", "ABC Company", "abc@gmail.com")

    physical_product = PhysicalProduct(
        "P001", "Keyboard", 50.0, 10, supplier1, 0.5
    )

    digital_product = DigitalProduct(
        "D001", "Python Ebook", 20.0, 5, supplier1, 10
    )

    # Display supplier through PhysicalProduct
    physical_product.supplier.display_information()

    # Display supplier through DigitalProduct
    digital_product.supplier.display_information()

def test_add_remove_product():
    # 1. Create a Supplier
    supplier1 = Supplier("S001", "ABC Company", "abc@gmail.com")

    # 2. Create a Product independently
    product1 = PhysicalProduct(
        "P001", "Keyboard", 50.0, 10, supplier1, 0.5
    )

    print("===== PRODUCT CREATED =====")
    product1.display_information()


    # 3. Create two separate Inventories
    inventory_a = Inventory()
    inventory_b = Inventory()


    # 4. Add Product to Inventory A
    print("\n===== ADD TO INVENTORY A =====")

    inventory_a.add_product(product1)

    print("Product in Inventory A:",
          inventory_a.search_product("P001") is not None)
    print("Product in Inventory B:",
              inventory_b.search_product("P001") is not None)


    # 5. Remove Product from Inventory A
    print("\n===== REMOVE FROM INVENTORY A =====")

    result = inventory_a.remove_product("P001")

    print("Removal successful:", result)
    print("Product in Inventory A:",
          inventory_a.search_product("P001") is not None)
    print("Product in Inventory B:",
              inventory_b.search_product("P001") is not None)


    # 6. Check whether Product still exists
    print("\n===== CHECK PRODUCT STILL EXISTS =====")

    product1.display_information()


    # 7. Add the SAME Product to Inventory B
    print("\n===== ADD TO INVENTORY B =====")

    inventory_b.add_product(product1)

    print("Product in Inventory A:",
        inventory_a.search_product("P001") is not None)
    print("Product in Inventory B:",
        inventory_b.search_product("P001") is not None)


    # 8. Confirm it is the SAME Product object
    print("\n===== CHECK OBJECT IDENTITY =====")

    print("Same Product object:",
          inventory_b.search_product("P001") is product1)

def test_order():

    supplier1 = Supplier("S001", "ABC Company", "abc@gmail.com")

    product1 = PhysicalProduct("P001", "Keyboard", 50.0, 10, supplier1, 5.0)
    product2 = DigitalProduct("D001", "Python Ebook", 20.0, 5, supplier1, 5.0)
    product3 = PhysicalProduct("P002", "Mouse", 30.0, 15, supplier1, 5.0)
    product4 = DigitalProduct("D002", "Java Ebook", 25.0, 8, supplier1, 5.0)

    order_line1 = OrderLine(product1)
    order_line2 = OrderLine(product2)
    order_line3 = OrderLine(product3)
    order_line4 = OrderLine(product4)
    print("===== ORDER TEST =====")
    print("Product 1:")
    order_line1.display_order_line()
    print("Product 2:")
    order_line2.display_order_line()
    print("Product 3:")
    order_line3.display_order_line()
    print("Product 4:")
    order_line4.display_order_line()

#test_supplier_display_information()
#test_add_remove_product()
test_order()