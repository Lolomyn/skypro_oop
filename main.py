from src.utils import create_objects_from_json, read_data

if __name__ == "__main__":
    categories = read_data("data/products.json")
    users_data = create_objects_from_json(categories)
