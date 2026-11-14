from product import Product
from canbeshipped import canBeShipped
from supplier import Supplier

class PhysicalProduct(Product):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight=float(weight)

    @property
    def weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg  |  Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self):
        return f"Shipping weight: {self.__weight} kg"

    def calculate_shipping_cost(self):
        # Example shipping cost calculation based on weight
        base_cost = 5.00  # base shipping cost
        cost_per_kg = 2.00  # cost per kilogram
        shipping_cost = base_cost + (self.__weight * cost_per_kg)
        return shipping_cost