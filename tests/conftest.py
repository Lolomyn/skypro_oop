import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture()
def product():
    return Product("Xiaomi POCO X3 Pro", "256GB, Синий цвет, 120 FPS", 25000.0, 1)


@pytest.fixture()
def order():
    return Order("Xiaomi POCO X3 Pro", 12, 25000.0)


@pytest.fixture()
def another_product():
    return Product("Iphone 15 Pro Max", "512GB, Розовый цвет, 60 FPS", 150000.0, 1)


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
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture()
def lawngrass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


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
