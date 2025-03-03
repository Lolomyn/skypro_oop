class ObjectException(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Ошибка создания экземпляра"

    def __str__(self):
        return self.message


class ZeroQuantityException(ObjectException):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Указано неверное количество товара"
