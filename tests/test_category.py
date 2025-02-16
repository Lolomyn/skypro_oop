from src.category import Category


def test_category_init(category_1, category_2):
    assert category_1.name == "Часы"
    assert category_1.description == "Мои часы"

    assert category_2.name == "Смартфоны"
    assert category_2.description == "Мои устройства"

    assert Category.category_count == 2
    assert Category.product_count == 4


def test_category_add_product(category_1, product):
    assert category_1.product_count == 5
    category_1.add_product(product)
    assert category_1.product_count == 6
