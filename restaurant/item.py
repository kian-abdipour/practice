import json
from category import Category


class Item:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    # This method append food to list_food in menu class
    # With name food append a price of food by integer type
    @staticmethod
    def add_item():
        with open("category_datas.json", "r") as category_file:
            load_data = json.load(category_file)

        if Category.display_categories():
            pass

        else:
            return print("Now we dont have any category first you should add category")

        try:
            print("Enter number of category that you want")
            number_category_of_item = int(input(": "))

            print("Enter name of item")
            name_of_item = input(": ")

            print(f"Enter price of {name_of_item} the currency of money is dollar")
            price_of_item = int(input(": "))

        except ValueError:
            return print("You should type just number")

        item = Item(name_of_item, price_of_item)
        data = {
            "name": item.name,
            "price": item.price
        }
        for category in load_data["categories"]:
            if load_data["categories"].index(category)+1 == number_category_of_item:
                category["list_items"].append(data)

        with open("category_datas.json", "w") as category_file:
            json.dump(load_data, category_file)

        print("Add item was successful")

    @staticmethod
    def display_items():
        with open("category_datas.json", "r") as category_file:
            load_data = json.load(category_file)

        if Category.display_categories():
            pass

        else:
            return print("Now we don't have any category")

        try:
            number_category = int(input(": "))

        except ValueError:
            return print("Category not found")

        category = load_data["categories"][number_category-1]
        if len(category["list_items"]) > 0:
            for item in category["list_items"]:
                print(category["list_items"].index(item)+1, item["name"], "price:", item["price"])

        else:
            print(f"Now we don't have any item in {category['name']}")

        return number_category

    @staticmethod
    # This method remove the food that user want
    def remove_item():
        with open("category_datas.json", "r") as category_file:
            load_data = json.load(category_file)

        number_category = Item.display_items()
        if len(load_data["categories"]) == 0:
            return

        try:
            print("Enter number item")
            number_item = int(input(": "))

        except ValueError:
            return print("ValueError: You should type just number")

        for category in load_data["categories"]:
            if load_data["categories"].index(category) == number_category-1:
                category["list_items"].pop(number_item-1)
                with open("category_datas.json", "w") as category_file:
                    json.dump(load_data, category_file)
                return print("Remove item was successful")

        return print("Number not found")

