import json


class Customer:
    username_that_is_login = None

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @staticmethod
    # This method get the username and password then append in it to load_data that is
    # Pasts information of customers in customer_datas.json file then
    # Again dump new version of load_datas.json to customer.json
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
    # This method get a username and password then load customer_datas then
    # Check that we have this information or not
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

