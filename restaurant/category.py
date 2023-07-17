from menu import Menu


class Category:
    def __init__(self, name):
        self.name = name
        self.list_items = []

    @staticmethod
    def add_category():
        print("Enter name of category {number_category}".format(number_category=len(Menu.list_categories) + 1))
        name_of_category = input(": ")
        category = Category(name_of_category)
        Menu.list_categories.append(category)
        print("Add category was successful")

