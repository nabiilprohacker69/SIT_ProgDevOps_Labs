
from abc import ABC, abstractmethod

class canBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass
