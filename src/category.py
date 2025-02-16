from src.product import Product


class Category:
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Конструктор категорий"""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        output_str = ''
        for product in self.__products:
            output_str += str(product) + '\n'
        return output_str

    def add_product(self, product: Product) -> None:
        Category.product_count += 1
        self.__products.append(product)
