from product import Product
from supplier import Supplier
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct


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

