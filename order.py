from product import Product
from orderline import OrderLine
from discount import DiscountStrategy, NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = discount

        if discount is None:
            self.discount = NoDiscount()
        else:
            self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None: ##->None means return nothing. if its -> int means return an int
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)
        
    def display_order(self) -> None:
        print(f"\nOrder ID: {self.order_id}")

        for order_line in self.order_lines:
            order_line.display_order_line()

        print(f"Order Total: ${self.calculate_total():.2f}")

    def calculate_total(self) -> float: 
        total = sum(line.calculate_subtotal() for line in self.order_lines) 
        return self.discount.apply(total) 

    def remove_order_line(self, index: int) -> bool:
        if index < 0 or index >= len(self.order_lines):
            return False

        self.order_lines.pop(index)
        return True

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount
