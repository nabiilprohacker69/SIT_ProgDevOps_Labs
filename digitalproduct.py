from product import Product
from supplier import Supplier

class DigitalProduct(Product):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, extra_value: float):
        super().__init__(product_id, name, price, stock, supplier) 
        self.__file_size=float(extra_value)

    @property
    def extra_value(self):
        return self.__file_size

    def display_information(self):
        super().display_information()
        print(f"File Size: {self.__file_size} MB")

    def get_fulfilment_info(self):
        return f"Download size: {self.__file_size} MB"