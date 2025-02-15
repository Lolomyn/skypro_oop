class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Конструктор продуктов"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price < 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __repr__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
