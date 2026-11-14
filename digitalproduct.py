from product import Product

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, file_size):
        super().__init__(product_id, name, price, stock)
        self.__file_size = float(file_size)

    @property
    def file_size(self):
        return self.__file_size

    def display_information(self):
        super().display_information()
        print(f"File Size: {self.__file_size} MB")

    def get_fulfilment_info(self):
        return f"Download size: {self.__file_size} MB"