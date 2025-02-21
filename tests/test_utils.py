import json
import os

from src.category import Category
from src.utils import create_objects_from_json, read_data


def test_read_data(test_data):
    file_path = "test_data.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f)

    result = read_data(file_path)

    assert isinstance(result, list)

    assert len(result) == 1
    assert result[0]["name"] == "Category 1"
    assert len(result[0]["products"]) == 2

    os.remove(file_path)


def test_create_objects_from_json(test_data):
    categories = create_objects_from_json(test_data)

    assert isinstance(categories, list)
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
