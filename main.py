from src.category import Category
from src.product import Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1)

    print()

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    for product in category1:
        print(product)

    product_5 = Product.new_product(
        {
            "name": "Xiaomi POCO X3 Pro",
            "description": "description",
            "price": 27000.0,
            "quantity": 1,
        }
    )

    print()

    print(product_5.price)
    print(product_5.quantity)
