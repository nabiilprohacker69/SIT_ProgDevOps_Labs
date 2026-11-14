
##responsible for managing a collection of Product objects: add, search, update stock, display all


from product import Product


class Inventory:

    def __init__(self):
        self.__products: list[Product] = []    # list of Product objects, kept in memory

    def add_product(self, product: Product) ->None:
        if self.search_product(product.product_id) is not None:
            return False        # product ID already exists
        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        product = self.search_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def update_stock(self, product_id: str, quantity: int) -> bool:
        product = self.search_product(product_id)
        if product is None:
            return False
        return product.update_stock(quantity)   # the Product updates its own stock

    def display_all(self):
        if len(self.__products) == 0:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()

    def get_all_products(self):
        return list(self.__products)      
