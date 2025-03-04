from src.base_order import BaseOrder
from src.exception import ZeroQuantityException
from src.product import Product


class Order(BaseOrder):

    def __init__(self, product: Product, quantity: int, price: float):
        self.product = product
        if quantity <= 0:
            raise ZeroQuantityException
        self.cost = quantity * price

    def add_product(self, product: Product):
        pass
