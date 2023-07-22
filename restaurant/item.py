from menu import Menu


class Item:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    # This method append food to list_food in menu class
    # With name food append a price of food by integer type
    @staticmethod
    def add_item():
        Menu.display_categories()
        try:
            print("Enter number of category that you want")
            index_category_of_item = int(input(": "))

        except ValueError:
            return print("You should type just number")

        print("Enter name of item")
        name_of_item = input(": ")

        try:
            print("Enter price of {name_item} the currency of money is dollar".format(name_item=name_of_item))
            price_of_item = int(input(": "))

        except ValueError:
            return print("ValueError: You should type just number")

        for category in Menu.list_categories:
            if index_category_of_item - 1 == Menu.list_categories.index(category):
                item = Item(name_of_item, price_of_item)
                category.list_items.append(item)
                print("Add item was successful ")

    @staticmethod
    # This method remove the food that user want
    def remove_item():
        Menu.display_categories()

        try:
            print("Enter number of category that food is in it")
            number_category = int(input(": ")) - 1

        except ValueError:
            return print("You must enter just number")

        for item in Menu.list_categories[number_category].list_items:
            print(Menu.list_categories[number_category].list_items.index(item) + 1, " -- ", item.name)

        try:
            print("Enter number of item that you want to remove")
            number_item = int(input(": ")) - 1

        except ValueError:
            return print("You must type just number")

        condition_of_remove_item = False
        for item in Menu.list_categories[number_category].list_items:
            if Menu.list_categories[number_category].list_items.index(item) == number_item:
                Menu.list_categories[number_category].list_items.remove(item)
                condition_of_remove_item = True

        if condition_of_remove_item:
            print("Remove item was successful")

        else:
            print("Number not found")

