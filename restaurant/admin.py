from menu import Menu
from super_admin import SupperAdmin
from customer import list_information_login_customer


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
        print("Enter name of food {number_food}".format(number_food=len(Menu.list_foods) + 1))
        input_new_name_food = input(": ")

        print("Enter price of {name_food} the type of money is dollar".format(name_food=input_new_name_food))
        input_new_price_food = input(": ")

        # Make type safe
        try:
            int_input_new_price_food = int(input_new_price_food)

        except ValueError:
            return print("ValueError: you should type just number")

        print("Enter number type of food \n1 -- food\n2 -- appetizer\n3 -- drinks")
        input_number_type_of_food = input(": ")

        if input_number_type_of_food == "1":
            food_and_price_and_type_food = [input_new_name_food, int_input_new_price_food, "food"]
            Menu.list_foods.append(food_and_price_and_type_food)

        elif input_number_type_of_food == "2":
            food_and_price_and_type_food = [input_new_name_food, int_input_new_price_food, "appetizer"]
            Menu.list_foods.append(food_and_price_and_type_food)

        elif input_number_type_of_food == "3":
            food_and_price_and_type_food = [input_new_name_food, int_input_new_price_food, "drinks"]
            Menu.list_foods.append(food_and_price_and_type_food)

        else:
            print("Number not found")

    # This method remove the food that user want
    @staticmethod
    def remove_food():
        for food in Menu.list_foods:
            print(len(Menu.list_foods), " -- ", "(", food[0], ")", "price: ", food[1])

        input_number_food_for_remove = input(": ")
        # Make type safe
        try:
            int_input_number_food_for_remove = int(input_number_food_for_remove)

        except ValueError:
            return print("ValueError: You should just type number")

        condition_of_remove = False
        for food in Menu.list_foods:
            if Menu.list_foods.index(food) + 1 == int_input_number_food_for_remove:
                Menu.list_foods.pop(int_input_number_food_for_remove - 1)
                condition_of_remove = True

        if condition_of_remove:
            print("Remove food was successful")

        else:
            print("Remove food was unsuccessful")

    # This method is clear and show the all food that we have in list_food
    @staticmethod
    def display_menu():
        for food in Menu.list_foods:
            print(Menu.list_foods.index(food) + 1, " -- ", "(", food[0], ",", "type: ", food[2], ")", "price:", food[1])

    # This method confirm the orders
    # First check that we have orders or not then get the username that admin want to confirm the order
    # After by a nested loop pop all orders that are in customer list and customer list is in list_information_login_
    # customer
    @staticmethod
    def confirmation_the_active_transaction():
        progress = True
        while progress:
            number_account_that_have_orders = 0
            print("Please enter username of user that you want to confirm his orders")
            for customer in list_information_login_customer:
                if len(customer) > 3:
                    print(list_information_login_customer.index(customer) + 1, " -- ", customer[0])
                    number_account_that_have_orders += 1

            input_username_for_admin = input(": ")
            if number_account_that_have_orders > 0:
                for customer in list_information_login_customer:
                    if len(customer) > 3 and input_username_for_admin == customer[0]:
                        while len(customer) != 3:
                            list_information_login_customer[list_information_login_customer.index(customer)].pop()
                print("Confirmation was successful")

            else:
                print("Now we don't have any order")

            if input_username_for_admin == "q":
                progress = False

    # This method show the customer that have already order
    @staticmethod
    def display_orders_of_user():
        number_account_that_have_orders = 0
        for customer in list_information_login_customer:
            if len(customer) > 3:
                print(list_information_login_customer.index(customer) + 1, " -- ", customer[0])
                number_account_that_have_orders += 1

        if number_account_that_have_orders > 0:
            pass

        else:
            print("Now we don't have any order")
