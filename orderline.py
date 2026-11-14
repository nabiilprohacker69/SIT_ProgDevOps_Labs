
from product import Product


class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def display_order_line(self) -> None:
        print(
            f"Product ID: {self.product.product_id} | "
            f"Name: {self.product.name} | "
            f"Quantity: {self.quantity} | "
            f"Subtotal: ${self.calculate_subtotal():.2f}"
        )

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

