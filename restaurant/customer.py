from decorators import representing


list_information_signup_customer = []  # All data that we have about customer is in this variable as list


class Customer:
    username_login_customer_for_now = None

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @staticmethod
    @representing
    # This method get the user's username and password then append to list_information_login_customer
    def signup_customer():
        print("Enter your username")
        username = input(": ")

        print("Enter your password")
        password = input(": ")

        customer = Customer(username, password)
        list_information_signup_customer.append(customer)

    @classmethod
    @representing
    # This method check that we have this username pass or not if we don't have customer can't see the next
    # Page
    def login_customer(cls):
        print("Please enter username of your relax account")
        login_username = input(": ")

        print("Please enter password of your relax account")
        signup_password = input(": ")

        cls.username_login_customer_for_now = login_username
        condition_of_login = False
        for customer in list_information_signup_customer:
            if customer.username == login_username and customer.password == signup_password:
                condition_of_login = True

        if condition_of_login:
            print("Welcome to relax account ", login_username)

        else:
            print("Username or password not found")

        return condition_of_login

