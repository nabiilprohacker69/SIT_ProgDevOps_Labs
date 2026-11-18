from product import Product
from supplier import Supplier
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct
from inventory import Inventory
from orderline import OrderLine
from order import Order
from discount import PercentageDiscount, BulkDiscount


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

def test_order_line():
    # Create supplier
    print("test order line")

    supplier1 = Supplier("S001", "ABC Company", "abc@gmail.com")

    # Create products
    product1 = PhysicalProduct("P001", "Keyboard", 50.0, 10, supplier1, 0.5)
    product2 = PhysicalProduct("P002", "Mouse", 20.0, 15, supplier1, 0.2)
    product3 = PhysicalProduct("P003", "FC26", 100.0, 100, supplier1, 0.5)
    product4 = PhysicalProduct("P004", "GTA VI", 100.0, 200, supplier1, 0.2)

    # Create Orders
    order1 = Order("O001")
    order2 = Order("O002")

    # Add two products
    order1.add_order_line(product1, 2)
    order1.add_order_line(product2, 3)
    order2.add_order_line(product3, 1)
    order2.add_order_line(product4, 1)

    # Display Orders with no discount
    print("NO DISCOUNT: ")
    order1.display_order()
    order2.display_order()

    # Apply 10% discount on both orders and display
    print("10% DISCOUNT: ")
    order1.set_discount(PercentageDiscount(10))
    order2.set_discount(PercentageDiscount(10))
    order1.display_order()
    order2.display_order()

    # Apply bulk discount on both orders and display
    print("BULK DISCOUNT: ")
    order1.set_discount(BulkDiscount(200,30))
    order2.set_discount(BulkDiscount(200,30))
    order1.display_order()
    order2.display_order()


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

def test_lsp():
    supplier1 = Supplier("S001", "ABC Company", "abc@gmail.com")

    physical_product = PhysicalProduct(
        "P001", "Keyboard", 50.0, 10, supplier1, 0.5
    )

    digital_product = DigitalProduct(
        "D001", "Python Ebook", 20.0, 5, supplier1, 10
    )

    show_product_details(physical_product)
    show_product_details(digital_product)


#test_supplier_display_information()
#test_add_remove_product()
test_order_line()
#test_lsp()