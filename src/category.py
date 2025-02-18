from typing import Self

from src.product import Product


class Category:
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Конструктор категорий"""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count = len(self.__products)

    @property
    def products(self) -> str:
        output_str = ""
        for product in self.__products:
            output_str += str(product) + "\n"
        return output_str

    def add_product(self, product: Product) -> None:
        Category.product_count += 1
        self.__products.append(product)

    def __str__(self) -> str:
        quantity = 0

        for product in self.__products:
            quantity += product.quantity

        return f"{self.name}, количество продуктов: {quantity}"

    def __iter__(self) -> "CheckCategory":
        return CheckCategory(self)


class CheckCategory:
    def __init__(self, category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self):
        if self.index < len(self.category._Category__products):
            product = self.category._Category__products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
