import json


class Customer:
    username_that_is_login = None

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @staticmethod
    # This method get the user's username and password then append to list_information_login_customer
    def signup_customer():
        with open("customer_datas.json", "r") as customer_file:
            load_data = json.load(customer_file)

        print("Enter your username")
        username = input(": ")

        print("Enter your password")
        password = input(": ")

        customer = Customer(username, password)
        data = {
            "username": customer.username,
            "password": customer.password
        }
        load_data["customers"].append(data)

        with open("customer_datas.json", "w") as customer_file:
            json.dump(load_data, customer_file)
            print("You successfully create a relax account now do login")

    @staticmethod
    # This method check that we have this username pass or not if we don't have customer can't see the next
    # Page
    def login_customer():
        with open("customer_datas.json", "r") as customer_file:
            load_data = json.load(customer_file)

        print("Please enter username of your relax account")
        login_username = input(": ")

        print("Please enter password of your relax account")
        login_password = input(": ")

        for customer in load_data["customers"]:
            if login_username == customer["username"] and login_password == customer["password"]:
                print(f"{login_username} welcome to your relax account")
                Customer.username_that_is_login = login_username
                return True

        print("Try again username or password not found")
        return False

