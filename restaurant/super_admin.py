from decorators import representing


class SupperAdmin:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    list_admin = []
    super_admin_code = "1386"

    # This function is for login super admin, and we have just one super admin in this program
    # If condition of login will be true user can continue ass super admin
    @representing
    def super_admin_login(self):
        print("Enter super admin code login")
        super_admin_code = input(": ")

        condition_of_login_super_admin = False
        if super_admin_code == self.super_admin_code:
            condition_of_login_super_admin = True

        else:
            print("super admin code not found")

        return condition_of_login_super_admin

    @classmethod
    @representing
    # This method remove an admin from list_admin in SuperAdmin model that super admin want
    def remove_admin_by_supper_admin(cls):
        print("Enter number of admin that you want to remove")

        # This loop is for display each admin information to user choose intended admin
        for admin in cls.list_admin:
            print(cls.list_admin.index(admin) + 1, " -- ",
                  "(", admin.first_name, admin.last_name, ")",
                  "code: ", admin.admin_code)

        # This try except is our type safe part of this function
        try:
            number_admin_for_remove = int(input(": "))

        except ValueError:
            return print("ValueError: You should type number not letters or something else.")

        condition_of_remove = False
        for admin in cls.list_admin:
            if cls.list_admin.index(admin)+1 == number_admin_for_remove:
                cls.list_admin.pop(number_admin_for_remove - 1)
                condition_of_remove = True

        if condition_of_remove:
            print("Successful remove")

        else:
            print("Admin not found try again")

    @classmethod
    @representing
    # This function is for display each admin information to user choose intended admin
    def display_admins(cls):
        for admin in cls.list_admin:
            print(cls.list_admin.index(admin) + 1, " -- ", "(", admin.first_name, admin.last_name, ")",
                  "code: ", admin.admin_code)

