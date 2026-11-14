from product import Product
from orderline import OrderLine

class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None: ##->None means return nothing. if its -> int means return an int
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)
