from decorators import representing


class Admin:
    admins = []

    def __init__(self, first_name=None, last_name=None, admin_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.admin_code = admin_code

    @staticmethod
    @representing
    # This method is for login admin with a code that super admin set
    def admin_login():
        # Make type safe
        try:
            print("Enter your admin code")
            input_admin_code = int(input(": "))

        except ValueError:
            return print("ValueError: You should just type number")

        condition_of_login_admin = False
        for admin in Admin.admins:
            if admin.admin_code == input_admin_code:
                condition_of_login_admin = True
                break

        if condition_of_login_admin:
            print("\n", admin.first_name, admin.last_name, "welcome to your admin panel\n")

        else:
            print("Admin code not found")
        return condition_of_login_admin

    @classmethod
    @representing
    # This method is one of actions that super admin can do
    # This method is clear and append a new admin to list_admin
    def add_admin(cls):
        print("Enter first name of admin {number_admin}".format(number_admin=len(cls.admins) + 1))
        first_name_of_admin = input(": ")

        print("Enter last name of {first_name_admin}".format(first_name_admin=first_name_of_admin))
        last_name_of_admin = input(": ")

        print("Enter admin code's {full_name_admin}"
              .format(full_name_admin=first_name_of_admin + " " + last_name_of_admin))

        try:
            admin_code = int(input(": "))

        except ValueError:
            return print("ValueError: Your admin code must be number with out any space like: 3476.")

        admin = Admin(first_name_of_admin, last_name_of_admin, admin_code)
        cls.admins.append(admin)

    @classmethod
    @representing
    # This method remove an admin from list_admin in SuperAdmin model that super admin want
    def remove_admin(cls):
        print("Enter number of admin that you want to remove")

        # This loop is for display each admin information to user choose intended admin
        for admin in cls.admins:
            print(cls.admins.index(admin) + 1, " -- ",
                  "(", admin.first_name, admin.last_name, ")",
                  "code: ", admin.admin_code)

        # This try except is our type safe part of this function
        try:
            number_admin_for_remove = int(input(": "))

        except ValueError:
            return print("ValueError: You should type number not letters or something else.")

        condition_of_remove = False
        for admin in cls.admins:
            if cls.admins.index(admin)+1 == number_admin_for_remove:
                cls.admins.pop(number_admin_for_remove - 1)
                condition_of_remove = True

        if condition_of_remove:
            print("Successful remove")

        else:
            print("Admin not found try again")

    @classmethod
    @representing
    # This function is for display each admin information to user choose intended admin
    def display_admins(cls):
        for admin in cls.admins:
            print(cls.admins.index(admin) + 1, " -- ", "(", admin.first_name, admin.last_name, ")",
                  "code: ", admin.admin_code)

