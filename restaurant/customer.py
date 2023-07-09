from menu import Menu

list_information_signup_customer = []
list_information_customer_orders = []


class Customer:
    def __init__(self):
        self.full_name = None
        self.password = None
        self.list_orders = []
        self.list_transaction = []

    def signup_customer(self):
        print("Enter your full name")
        self.full_name = input(": ")

        print("Enter your password")
        self.password = input(": ")

        information_customer = [self.full_name, self.password]
        list_information_signup_customer.append(information_customer)

    @staticmethod
    def login_customer():
        print("Please enter your full name relax account")
        input_signup_full_name = input(": ")

        print("Please enter your password relax account")
        input_signup_password = input(": ")

        condition_of_login = False
        for item in list_information_signup_customer:
            if item[0] == input_signup_full_name and item[1] == input_signup_password:
                condition_of_login = True

        if condition_of_login:
            print("Welcome to relax account ", input_signup_full_name)

        else:
            print("Username or password not found")

        return condition_of_login

    def order_food(self):
        for food in Menu.list_food:
            print(Menu.list_food.index(food) + 1, " -- ", food[0], "price: ", food[1])

        input_number_food_for_order = input(": ")
        try:
            int_input_number_food_for_order = int(input_number_food_for_order)

        except ValueError:
            return print("ValueError: You should type just number")

        for food in Menu.list_food:
            if Menu.list_food.index(food) + 1 == int_input_number_food_for_order:
                self.list_orders.append(food)

        print("Please enter your username that you want to record order for him or enter your user name")
        input_first_name_for_order = input(": ")
        condition_of_order = False
        for customer in list_information_signup_customer:
            if customer[0] == input_first_name_for_order:
                list_information_signup_customer[list_information_signup_customer.index(customer)].\
                    append(self.list_orders[0])

        if condition_of_order:
            print("Record order was successful ")

        else:
            print("This user name doesn't have account in relax restaurant")

        self.list_orders.clear()
        print(self.list_orders)
        print(list_information_signup_customer)

    @staticmethod
    def display_orders():
        print(list_information_signup_customer)
