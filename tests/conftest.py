import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product():
    return Product("Xiaomi POCO X3 Pro", "256GB, Синий цвет, 120 FPS", 25000.0, 1)


@pytest.fixture()
def category_1():
    return Category("Часы", "Мои часы", [Product("Poco Watch", "Черный цвет, водонепроницаемые", 5000.0, 1)])


@pytest.fixture()
def category_2():
    return Category(
        "Смартфоны",
        "Мои устройства",
        [
            Product("Xiaomi POCO X3 Pro", "256GB, Синий цвет, 120 FPS", 25000.0, 1),
            Product("Iphone 13", "64GB, Белый цвет, 60 FPS", 60000.0, 3),
            Product("Samsung Galaxy S25", "512GB, Черный цвет, 120 FPS", 250000.0, 4),
        ],
    )


@pytest.fixture()
def test_data():
    return [
        {
            "name": "Category 1",
            "description": "description 1",
            "products": [
                {"name": "Product 1", "description": "desc", "price": 10.0, "quantity": 1},
                {"name": "Product 2", "description": "desc", "price": 20.0, "quantity": 2},
            ],
        }
    ]
