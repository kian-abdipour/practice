from decorators import representing


class Customer:
    information_customers = []
    username_login_customer_for_now = None

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @classmethod
    @representing
    # This method get the user's username and password then append to list_information_login_customer
    def signup_customer(cls):
        print("Enter your username")
        username = input(": ")

        print("Enter your password")
        password = input(": ")

        customer = Customer(username, password)
        cls.information_customers.append(customer)

    @classmethod
    @representing
    # This method check that we have this username pass or not if we don't have customer can't see the next
    # Page
    def login_customer(cls):
        print("Please enter username of your relax account")
        login_username = input(": ")

        print("Please enter password of your relax account")
        login_password = input(": ")

        cls.username_login_customer_for_now = login_username
        condition_of_login = False
        for customer in cls.information_customers:
            if customer.username == login_username and customer.password == login_password:
                condition_of_login = True

        if condition_of_login:
            print("Welcome to relax account ", login_username)

        else:
            print("Username or password not found")

        return condition_of_login

