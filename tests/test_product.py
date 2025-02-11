def test_product_init(product):
    assert product.name == "Xiaomi POCO X3 Pro"
    assert product.description == "256GB, Синий цвет, 120 FPS"
    assert product.price == 25000.0
    assert product.quantity == 1
