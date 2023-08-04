class Menu:
    list_categories = []

    @classmethod
    def display_menu(cls):
        print("Enter a number\n1 -- All menu\n2 -- All category\n3 -- Number of each category that use")
        number_type_of_display = input(": ")
        if number_type_of_display == "1":
            for category in cls.list_categories:
                print(category.name, ":")
                if len(category.list_items) > 0:
                    for item in category.list_items:
                        print(category.list_items.index(item) + 1, " -- ", "(", item.name,
                              "category:", category.name, ")",
                              "price:", item.price)

                else:
                    print("We don't have any food in", category.name)

        elif number_type_of_display == "2":
            Menu.display_categories()

        elif number_type_of_display == "3":
            for category in cls.list_categories:
                print(cls.list_categories.index(category) + 1, " -- ", category.name + ":", len(category.list_items))

        else:
            print("Number not found")

    @classmethod
    def display_categories(cls):
        if len(cls.list_categories) > 0:
            for category in Menu.list_categories:
                print(Menu.list_categories.index(category) + 1, " -- ", category.name)

        else:
            print("Now we don't have any category")

