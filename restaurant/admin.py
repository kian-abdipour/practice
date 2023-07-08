from menu import Menu
from super_admin import SupperAdmin

menu_obj = Menu()


class Admin:
    first_name = None
    last_name = None
    admin_code = None

    # This function is for login admin with a code that super admin set
    @classmethod
    def admin_login(cls):
        print("Enter your admin code")
        input_admin_code = input(": ")

        # Make type safe
        try:
            int_input_admin_code = int(input_admin_code)

        except ValueError:
            return print("ValueError: You should just type number")

        condition_of_login_admin = False
        for admin in SupperAdmin.list_admin:
            if admin[2] == int_input_admin_code:
                condition_of_login_admin = True
                cls.first_name = admin[0]
                cls.last_name = admin[1]
                cls.admin_code = admin[2]

        if condition_of_login_admin:
            print("\n", cls.first_name, cls.last_name, "welcome to your admin panel\n")

        else:
            print("Admin code not found")
        return condition_of_login_admin

    # This function append food to list_food in menu class
    # With name food append a price of food by integer type
    @staticmethod
    def add_food():
        print("Enter name of food {number_food}".format(number_food=len(menu_obj.list_food) + 1))
        input_new_name_food = input(": ")

        print("Enter price of {name_food} the type of money is tooman".format(name_food=input_new_name_food))
        input_new_price_food = input(": ")

        # Make type safe
        try:
            int_input_new_price_food = int(input_new_price_food)

        except ValueError:
            return print("ValueError: you should type just number")

        food_and_price = [input_new_name_food, int_input_new_price_food]
        menu_obj.list_food.append(food_and_price)

    # This function remove the food that user want
    @staticmethod
    def remove_food():
        for food in menu_obj.list_food:
            print(len(menu_obj.list_food), " -- ", "(", food[0], ")", "price: ", food[1])

        input_number_food_for_remove = input(": ")
        # Make type safe
        try:
            int_input_number_food_for_remove = int(input_number_food_for_remove)

        except ValueError:
            return print("ValueError: You should just type number")

        condition_of_remove = False
        for food in menu_obj.list_food:
            if menu_obj.list_food.index(food) + 1 == int_input_number_food_for_remove:
                menu_obj.list_food.pop(int_input_number_food_for_remove - 1)
                condition_of_remove = True

        if condition_of_remove:
            print("Remove food was successful")

        else:
            print("Remove food was unsuccessful")

    # This function is clear and show the all food that we have in list_food
    @staticmethod
    def display_menu():
        for food in menu_obj.list_food:
            print(len(menu_obj.list_food), " -- ", "(", food[0], ")", "price: ", food[1])

    @staticmethod
    def confirmation_the_active_transaction():
        pass

