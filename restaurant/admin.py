from menu import Menu
from super_admin import SupperAdmin
from customer import list_information_login_customer

menu_obj = Menu()


class Admin:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.admin_code = None

    # This method is for login admin with a code that super admin set
    def admin_login(self):

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
                self.first_name = admin[0]
                self.last_name = admin[1]
                self.admin_code = admin[2]

        if condition_of_login_admin:
            print("\n", self.first_name, self.last_name, "welcome to your admin panel\n")

        else:
            print("Admin code not found")
        return condition_of_login_admin

    # This method append food to list_food in menu class
    # With name food append a price of food by integer type
    @staticmethod
    def add_food():
        print("Enter name of food {number_food}".format(number_food=len(Menu.list_food) + 1))
        input_new_name_food = input(": ")

        print("Enter price of {name_food} the type of money is dollar".format(name_food=input_new_name_food))
        input_new_price_food = input(": ")

        # Make type safe
        try:
            int_input_new_price_food = int(input_new_price_food)

        except ValueError:
            return print("ValueError: you should type just number")

        food_and_price = [input_new_name_food, int_input_new_price_food]
        Menu.list_food.append(food_and_price)

    # This method remove the food that user want
    @staticmethod
    def remove_food():
        for food in Menu.list_food:
            print(len(Menu.list_food), " -- ", "(", food[0], ")", "price: ", food[1])

        input_number_food_for_remove = input(": ")
        # Make type safe
        try:
            int_input_number_food_for_remove = int(input_number_food_for_remove)

        except ValueError:
            return print("ValueError: You should just type number")

        condition_of_remove = False
        for food in Menu.list_food:
            if Menu.list_food.index(food) + 1 == int_input_number_food_for_remove:
                Menu.list_food.pop(int_input_number_food_for_remove - 1)
                condition_of_remove = True

        if condition_of_remove:
            print("Remove food was successful")

        else:
            print("Remove food was unsuccessful")

    # This method is clear and show the all food that we have in list_food
    @staticmethod
    def display_menu():
        for food in Menu.list_food:
            print(Menu.list_food.index(food) + 1, " -- ", "(", food[0], ")", "price: ", food[1])

    # This method confirm the orders
    # First check that we have orders or not then get the username that admin want to confirm the order
    # After by a nested loop pop all orders that are in customer list and customer list is in list_information_login_
    # customer
    @staticmethod
    def confirmation_the_active_transaction():
        while_response = True
        while while_response:
            number_account_that_have_orders = 0
            print("Please enter username of user that you want to confirm his orders")
            for customer in list_information_login_customer:
                if len(customer) > 2:
                    print(list_information_login_customer.index(customer) + 1, " -- ", customer[0])
                    number_account_that_have_orders += 1

            input_username_for_admin = input(": ")
            if number_account_that_have_orders > 0:
                for customer in list_information_login_customer:
                    if len(customer) > 2 and input_username_for_admin == customer[0]:
                        while len(customer) != 2:
                            list_information_login_customer[list_information_login_customer.index(customer)].pop()
                print("Confirmation was successful")

            else:
                print("Now we don't have any order")

            if input_username_for_admin == "q":
                while_response = False

    # This method show the customer that have already order
    @staticmethod
    def display_orders_of_user():
        number_account_that_have_orders = 0
        print("Please enter username of user that you want to confirm his orders")
        for customer in list_information_login_customer:
            if len(customer) > 2:
                print(list_information_login_customer.index(customer) + 1, " -- ", customer[0])
                number_account_that_have_orders += 1

        if number_account_that_have_orders > 0:
            pass

        else:
            print("Now we don't have any order")
