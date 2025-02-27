from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_mixin_log(capsys):
    Product("Iphone 15 Pro Max", "512GB, Розовый цвет, 60 FPS", 150000.0, 1)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15 Pro Max, 512GB, Розовый цвет, 60 FPS, 150000.0, 1)"

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
