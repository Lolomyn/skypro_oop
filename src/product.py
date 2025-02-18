class Product:
    name: str
    description: str
    __price: float
    quantity: int

    all_objects = {}

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Конструктор продуктов"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_objects[name] = self

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        if product_data.get("name") in Product.all_objects:
            existing_product = Product.all_objects[product_data.get("name")]
            existing_product.quantity += product_data.get("quantity")
            if existing_product.price != product_data['price']:
                existing_product.price = max(existing_product.price, product_data['price'])
        else:
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
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                answer = input('Новая цена ниже текущей. Введите "y", чтобы подтвердить свое намерение: ')
                if answer == 'y':
                    self.__price = new_price
                else:
                    print("Изменение отменено.")
            else:
                self.__price = new_price

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price + other.__price
