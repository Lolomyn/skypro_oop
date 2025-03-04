import pytest

from src.exception import ZeroQuantityException
from src.order import Order


def test_order_init(order):
    assert order.product == "Xiaomi POCO X3 Pro"
    assert order.cost == 300000.0


def test_order_zero_exception():
    with pytest.raises(ZeroQuantityException):
        Order("Xiaomi POCO X3 Pro", 0, 15000.0)


def test_order_add_product(order, product):
    assert order.add_product(product) is None
