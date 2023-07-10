from menu import Menu

list_information_login_customer = []  # All data that we have about customer is in this variable as list


class Customer:
    def __init__(self):
        self.username = None
        self.password = None
        self.list_orders = []
    username_of_login_for_now = None

    # This method get the user's username and password then append to list_information_login_customer
    def signup_customer(self):
        print("Enter your username")
        self.username = input(": ")

        print("Enter your password")
        self.password = input(": ")

        information_customer = [self.username, self.password]
        list_information_login_customer.append(information_customer)

    @classmethod
    # This method check that we have this username pass or not if we don't have customer can't see the next
    # Page
    def login_customer(cls):
        print("Please enter username of your relax account")
        input_login_username = input(": ")

        print("Please enter password of your relax account")
        input_signup_password = input(": ")

        cls.username_of_login_for_now = input_login_username
        condition_of_login = False
        for item in list_information_login_customer:
            if item[0] == input_login_username and item[1] == input_signup_password:
                condition_of_login = True

        if condition_of_login:
            print("Welcome to relax account ", input_login_username)

        else:
            print("Username or password not found")

        return condition_of_login

    # This method first display menu then get the number of food that customer want to order
    # Then add this food to list_customer that are in list_information_login_customer
    def order_food(self):
        for food in Menu.list_foods:
            print(Menu.list_foods.index(food) + 1, " -- ", food[0], "price: ", food[1])

        if Menu.list_foods == 0:
            print("Sorry but now we don't have any food now")

        input_number_food_for_order = input(": ")
        try:
            int_input_number_food_for_order = int(input_number_food_for_order)

        except ValueError:
            return print("ValueError: You should type just number")

        try:
            # This variable is for handle index error
            last_item_list_food = Menu.list_foods[int_input_number_food_for_order - 1]

        except IndexError:
            return print("IndexError: Number not found")

        for food in Menu.list_foods:
            if Menu.list_foods.index(food) + 1 == int_input_number_food_for_order:
                self.list_orders.append(food)

        condition_of_order = False
        for customer in list_information_login_customer:
            if customer[0] == self.username_of_login_for_now:
                list_information_login_customer[list_information_login_customer.index(customer)].\
                    append(self.list_orders[0])
                condition_of_order = True

        if condition_of_order:
            print("Record order was successful ")

        else:
            print("This user name doesn't have account in relax restaurant try again")

        self.list_orders.clear()

    @classmethod
    # This method display order of account that user say and show the total of fee's order
    def display_orders_and_receipt(cls):
        for customer in list_information_login_customer:
            if customer[0] == cls.username_of_login_for_now:
                if len(customer) > 3:
                    print("You have ordered this foods:")
                    for information in customer:
                        if type(information) == list:
                            print(customer[0], " -- ", information[0], "price: ", information[1])

                else:
                    print("You don't have any orders")

        print(list_information_login_customer)
        total = 0
        for customer_2 in list_information_login_customer:
            if customer_2[0] == cls.username_of_login_for_now:
                if len(customer_2) > 3:
                    for information_2 in customer_2:
                        if type(information_2) == list:
                            total = information_2[1] + total

        print("Total: ", total)

