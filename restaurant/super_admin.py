from admin import Admin


class SupperAdmin:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.list_admin = []
        self.super_admin_code = "1386"

    def super_admin_login(self):
        print("Enter super admin code login")
        input_super_admin_code = input(": ")

        condition_of_login = False
        if input_super_admin_code == self.super_admin_code:
            condition_of_login = True

        else:
            print("super admin code not found")

        return condition_of_login

    def add_admin_by_super_admin(self):
        print("Enter first name of admin {number_admin}".format(number_admin=len(self.list_admin) + 1))
        input_first_name_of_admin = input(": ")

        print("Enter last name of {first_name_admin}".format(first_name_admin=input_first_name_of_admin))
        input_last_name_of_admin = input(": ")

        print("Enter admin code's {full_name_admin}"
              .format(full_name_admin=input_first_name_of_admin + " " + input_last_name_of_admin))
        input_admin_code = input(": ")
        try:
            int_input_admin_code = int(input_admin_code)

        except ValueError:
            return print("ValueError: Your admin code must be number with out any space like: 3476.")

        admin_obj = Admin(input_first_name_of_admin, input_last_name_of_admin, int_input_admin_code)

        list_information_admin = [admin_obj.first_name, admin_obj.last_name, admin_obj.admin_code]

        self.list_admin.append(list_information_admin)
        print(self.list_admin)

    def remove_admin_by_supper_admin(self):
        print("Enter number of admin that you want to remove")
        for admin in self.list_admin:
            print(self.list_admin.index(admin) + 1, " -- ", "(", admin[0], admin[1], ")", "code: ", admin[2])

        input_number_admin_for_remove = input(": ")
        try:
            int_input_number_admin_for_remove = int(input_number_admin_for_remove)

        except ValueError:
            return print("ValueError: You sold type number not letters or something else.")

        condition_of_remove = False
        for admin in self.list_admin:
            if self.list_admin.index(admin)+1 == int_input_number_admin_for_remove:
                self.list_admin.pop(int_input_number_admin_for_remove - 1)
                condition_of_remove = True

        if condition_of_remove:
            print("Successful remove")

        else:
            print("Admin not found try again")


# a = SupperAdmin("kian", "ali")
# a.add_admin_by_super_admin()
# a.add_admin_by_super_admin()
# a.remove_admin_by_supper_admin()

