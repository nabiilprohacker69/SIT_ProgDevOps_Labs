from abc import ABC, abstractmethod

class DiscountStrategy(ABC): 
    @abstractmethod 
    def apply(self, total: float) -> float: 
        pass

def NoDiscount() -> DiscountStrategy: 
    class NoDiscountStratergy(DiscountStrategy):
        def apply(self, total: float) -> float:
            return total
    return NoDiscountStratergy()

def PercentageDiscount(percentage: float) -> DiscountStrategy: 
    class PercentageDiscountStrategy(DiscountStrategy): 
        def apply(self, total: float) -> float: 
            return total * (1 - percentage / 100) 
    return PercentageDiscountStrategy()

def BulkDiscount(threshold: float, discount_amount: float) -> DiscountStrategy: 
    class BulkDiscountStrategy(DiscountStrategy): 
        def apply(self, total: float) -> float: 
            if total >= threshold: 
                return total - discount_amount 
            return total 
    return BulkDiscountStrategy()

# Create discount strategies
discount = NoDiscount()
percentage = PercentageDiscount(20)
bulk = BulkDiscount(500, 50)

# # Original purchase total
# total = 600

# # Apply different discounts
# print("Original price:", total)

# print("No discount:", discount.apply(total))

# print("20% discount:", percentage.apply(total))

# print("Bulk discount:", bulk.apply(total))