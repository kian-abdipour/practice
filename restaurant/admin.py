from super_admin import SupperAdmin
from decorators import representing


class Admin:
    def __init__(self, first_name=None, last_name=None, admin_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.admin_code = admin_code

    @staticmethod
    @representing
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

    @staticmethod
    @representing
    # This method is one of actions that super admin can do
    # This method is clear and append a new admin to list_admin
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

