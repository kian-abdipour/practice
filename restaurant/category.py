import json


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
                print(load_data["categories"].index(category)+1, " -- ",  category["name"])
            return True

        else:
            return False

    @staticmethod
    def remove_categories():
        with open("category_datas.json", "r") as category_file:
            load_data = json.load(category_file)

        if Category.display_categories():
            pass

        else:
            return print("Now we don't have category")

        try:
            print("Enter number of category to remove")
            number_category = int(input(": "))

        except ValueError:
            return print("ValueError: You should type just number")

        condition_remove = False
        for category in load_data["categories"]:
            if load_data["categories"].index(category)+1 == number_category:
                load_data["categories"].remove(category)
                condition_remove = True

        if condition_remove:
            print("Remove item was successful")

        else:
            return print("Number not found")

        with open("category_datas.json", "w") as category_file:
            json.dump(load_data, category_file)
