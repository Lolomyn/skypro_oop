import pytest

from src.category import Category, CheckCategory


def test_category_init(category_1, category_2):
    assert category_1.name == "Часы"
    assert category_1.description == "Мои часы"

    assert category_2.name == "Смартфоны"
    assert category_2.description == "Мои устройства"

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_add_product(category_1, product):
    assert category_1.product_count == 1
    category_1.add_product(product)
    assert category_1.product_count == 2


def test_category_products(category_1):
    assert category_1.products == "Poco Watch, 5000.0 руб. Остаток: 1 шт.\n"


def test_category_str(category_1):
    assert str(category_1) == "Часы, количество продуктов: 1"


def test_category_add_product_typeerror(category_1):
    new_product = "i am a new product, trust me"
    with pytest.raises(TypeError):
        category_1.add_product(new_product)


def test_check_category_iterator(product, another_product):
    category = Category("Test Category", "Test", [product, another_product])

    iterator = CheckCategory(category)

    assert next(iterator) == product
    assert next(iterator) == another_product

    try:
        next(iterator)
        assert False, "Итератор не вызвал StopIteration"
    except StopIteration:
        pass

    products_from_iterator = []
    for products in CheckCategory(category):
        products_from_iterator.append(products)

    assert products_from_iterator == [product, another_product]


def test_check_category_empty():
    category = Category("Empty Category", "Empty", [])

    iterator = CheckCategory(category)

    try:
        next(iterator)
        assert False
    except StopIteration:
        pass

    products_from_iterator = []
    for product in CheckCategory(category):
        products_from_iterator.append(product)

    assert products_from_iterator == []
