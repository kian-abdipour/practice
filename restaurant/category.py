from decorators import representing


class Category:
    categories = []

    def __init__(self, name=None):
        self.name = name
        self.items = []

    @classmethod
    @representing
    def add_category(cls):
        print("Enter name of category {number_category}".format(number_category=len(cls.categories) + 1))
        name_of_category = input(": ")

        category = Category(name_of_category)
        cls.categories.append(category)
        print("Add category was successful")

    @classmethod
    @representing
    def display_menu(cls):
        print("Enter a number\n1 -- All menu\n2 -- All category\n3 -- Number of each category that use")
        number_type_of_display = input(": ")
        if number_type_of_display == "1":
            for category in cls.categories:
                print(category.name, ":")
                if len(category.items) > 0:
                    for item in category.items:
                        print(category.items.index(item) + 1, " -- ", "(", item.name,
                              "category:", category.name, ")",
                              "price:", item.price)

                else:
                    print("We don't have any item in", category.name)

        elif number_type_of_display == "2":
            Category.display_categories()

        elif number_type_of_display == "3":
            for category in cls.categories:
                print(cls.categories.index(category) + 1, " -- ", category.name + ":", len(category.items))

        else:
            print("Number not found")

    @classmethod
    def display_categories(cls):
        if len(cls.categories) > 0:
            for category in cls.categories:
                print(cls.categories.index(category) + 1, " -- ", category.name)

        else:
            print("Now we don't have any category")

