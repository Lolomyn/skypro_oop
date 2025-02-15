from unittest.mock import patch

from src.product import Product


def test_product_init(product):
    assert product.name == "Xiaomi POCO X3 Pro"
    assert product.description == "256GB, Синий цвет, 120 FPS"
    assert product.price == 25000.0
    assert product.quantity == 1


def test_product_new_product():
    product_2 = Product.new_product(
        {
            "name": "name",
            "description": "description",
            "price": 100.0,
            "quantity": 1,
        }
    )
    assert product_2.name == "name"
    assert product_2.description == "description"
    assert product_2.price == 100.0
    assert product_2.quantity == 1


def test_product_new_product_existing(product):
    product_2 = Product.new_product(
        {
            "name": "Xiaomi POCO X3 Pro",
            "description": "description",
            "price": 27000.0,
            "quantity": 1,
        }
    )

    assert product.price == 27000.0
    assert product.quantity == 2


def test_product_set_new_price_correct(product):
    with patch("builtins.input", return_value="y"):
        product.price = 1000.0
        assert product.price == 1000.0


def test_product_set_new_price_incorrect(capsys, product):
    product.price = -150
    print_result = capsys.readouterr()
    assert print_result.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_set_new_price_correct_cancelled(product):
    with patch("builtins.input", return_value="no"):
        product.price = 1000.0
        assert product.price == 1000.0


def test_product_repr(capsys, product):
    expected_repr = "Xiaomi POCO X3 Pro, 25000.0 руб. Остаток: 1 шт."
    assert repr(product) == expected_repr


def test_product_repr_change_data(capsys, product):
    with patch("builtins.input", return_value="y"):
        expected_repr = "Xiaomi POCO X3 Pro, 25000.0 руб. Остаток: 1 шт."
        assert repr(product) == expected_repr

        product.price = 1234.5
        expected_repr = "Xiaomi POCO X3 Pro, 1234.5 руб. Остаток: 1 шт."
        assert repr(product) == expected_repr
