from src.exception import ObjectException, ZeroQuantityException


def test_object_exception_default_message():
    exception = ObjectException()
    assert str(exception) == "Ошибка создания экземпляра"


def test_object_exception_custom_message():
    custom_message = "Сообщение об ошибке"
    exception = ObjectException(custom_message)
    assert str(exception) == custom_message


def test_object_exception_raise():
    try:
        raise ObjectException("Тестовая ошибка")
    except ObjectException as e:
        assert str(e) == "Тестовая ошибка"


def test_zero_quantity_exception_default_message():
    exception = ZeroQuantityException()
    assert str(exception) == "Указано неверное количество товара"


def test_zero_quantity_exception_custom_message():
    custom_message = "Сообщение о нулевом количестве"
    exception = ZeroQuantityException(custom_message)
    assert str(exception) == custom_message


def test_zero_quantity_exception_raise():
    try:
        raise ZeroQuantityException("Тестовая ошибка нулевого количества")
    except ZeroQuantityException as e:
        assert str(e) == "Тестовая ошибка нулевого количества"
