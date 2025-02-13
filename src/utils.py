import json
import os

from src.category import Category
from src.product import Product


def read_data(path: str) -> dict:
    """Чтение JSON-файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def create_objects_from_json(data: dict) -> list:
    """Создание объекта из JSON содержимого"""
    categories_list = []
    for category in data:
        products_list = []

        for product in category["products"]:
            products_list.append(Product(**product))

        category["products"] = products_list
        categories_list.append(Category(**category))
    return categories_list
