import json
from menu import Menu
from decorators import representing


class Category:
    def __init__(self, name=None):
        self.name = name
        self.list_items = []

    @staticmethod
    def add_category():
        with open("category_datas.json", "r") as category_file:
            load_data = json.load(category_file)

        print(f"Enter name of category {len(load_data['categories']) + 1}")
        name_of_category = input(": ")

        category = Category(name_of_category)
        data = {"name": category.name,
                "list_items": category.list_items
                }

        with open("category_datas.json", "w") as category_file:
            load_data["categories"].append(data)
            json.dump(load_data, category_file)

        print("Add category was successful")

    @staticmethod
    def display_categories():
        with open("category_datas.json", "r") as category_file:
            load_data = json.load(category_file)

        if len(load_data["categories"]) > 0:
            for category in load_data["categories"]:
                print(load_data["categories"].index(category)+1, category["name"])

        else:
            print("Now we don't have category")

