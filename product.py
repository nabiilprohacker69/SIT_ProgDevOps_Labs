from abc import ABC, abstractmethod

from supplier import Supplier
##responsible for product data, i.e. updating stock and displaying product information.

class Product(ABC):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.__product_id=str(product_id)
        self.__name=str(name)
        self.__price=float(price)
        self.__stock=int(stock) 
        self.supplier: Supplier = supplier ##tells python and ME that supplier is an OBJECT also its PUBLIC

    # read-only access: other classes can look at the data but cannot change it directly
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        # the Product decides what is a valid stock level (it manages its own state)
        if quantity < 0:
            return False
        self.__stock = quantity
        return True

    @abstractmethod ##cant call product display information
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock} |  ",end="")
