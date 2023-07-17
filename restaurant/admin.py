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

    # This method confirm the orders
    # First check that we have orders or not then get the username that admin want to confirm the order
    # After by a nested loop pop all orders that are in customer list and customer list is in list_information_login_
    # customer
    @staticmethod
    def confirmation_the_orders():
        progress = True
        while progress:
            number_account_that_have_orders = 0
            print("Please enter username of user that you want to confirm his orders")
            for customer in list_information_login_customer:
                if len(customer.list_orders) > 0:
                    number_account_that_have_orders += 1
                    print(customer.username)

            condition_of_confirmation = False
            username_username_customer = input(": ")
            if number_account_that_have_orders > 0:
                for customer in list_information_login_customer:
                    if len(customer.list_orders) > 0 and username_username_customer == customer.username:
                        customer.list_orders.clear()
                        condition_of_confirmation = True

            else:
                print("We don't have any order")

            if condition_of_confirmation:
                print("Confirmation was successful")

            else:
                print("Username not found")

            if username_username_customer == "q":
                progress = False

    # This method show the customer that have already order
    @staticmethod
    def display_orders_of_customer():
        if len(list_information_login_customer) > 0:
            for customer in list_information_login_customer:
                for order in customer.list_orders:
                    print(customer.username, " -- ", order.name, "price:", order.price)

