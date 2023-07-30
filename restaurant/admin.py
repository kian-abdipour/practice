from super_admin import SupperAdmin
from customer import list_information_login_customer


class Admin:
    def __init__(self, first_name=None, last_name=None, admin_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.admin_code = admin_code

    @staticmethod
    # This method is for login admin with a code that super admin set
    def admin_login():
        print("Enter your admin code")
        input_admin_code = input(": ")

        # Make type safe
        try:
            int_input_admin_code = int(input_admin_code)

        except ValueError:
            return print("ValueError: You should just type number")

        condition_of_login_admin = False
        for admin in SupperAdmin.list_admin:
            if admin.admin_code == int_input_admin_code:
                condition_of_login_admin = True
                break

        if condition_of_login_admin:
            print("\n", admin.first_name, admin.last_name, "welcome to your admin panel\n")

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

    @staticmethod
    # This function is one of actions that super admin can do
    # This function is clear and append a new admin to list_admin
    def add_admin():
        print("Enter first name of admin {number_admin}".format(number_admin=len(SupperAdmin.list_admin) + 1))
        first_name_of_admin = input(": ")

        print("Enter last name of {first_name_admin}".format(first_name_admin=first_name_of_admin))
        last_name_of_admin = input(": ")

        print("Enter admin code's {full_name_admin}"
              .format(full_name_admin=first_name_of_admin + " " + last_name_of_admin))

        try:
            input_admin_code = int(input(": "))

        except ValueError:
            return print("ValueError: Your admin code must be number with out any space like: 3476.")

        admin = Admin(first_name_of_admin, last_name_of_admin, input_admin_code)
        SupperAdmin.list_admin.append(admin)

    def __repr__(self):
        return ("This model has 3 attribute and you can define it by positional argument like this"
                "admin = Admin('Kian', 'Abdipour', 12)")

    def __str__(self):
        return f"Admin= {self.first_name} {self.last_name} code = {self.admin_code}"

    def __bool__(self):
        if self.admin_code < 100:
            return True

        else:
            return False

