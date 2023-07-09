class SupperAdmin:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    list_admin = []
    super_admin_code = "1386"

    # This function is for login super admin, and we have just one super admin in this program
    # If condition of login will be true user can continue ass super admin
    def super_admin_login(self):
        print("Enter super admin code login")
        input_super_admin_code = input(": ")

        condition_of_login_super_admin = False
        if input_super_admin_code == self.super_admin_code:
            condition_of_login_super_admin = True

        else:
            print("super admin code not found")

        return condition_of_login_super_admin

    # This function is one of actions that super admin can do
    # This function is clear and append a new admin to list_admin
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

        list_information_admin = [input_first_name_of_admin, input_last_name_of_admin, int_input_admin_code]

        self.list_admin.append(list_information_admin)

    # This function is second action that super admin can do
    # It work like previous function but the difference is that this function pop admin from list_admin
    def remove_admin_by_supper_admin(self):
        print("Enter number of admin that you want to remove")

        # This loop is for display each admin information to user choose intended admin
        for admin in self.list_admin:
            print(self.list_admin.index(admin) + 1, " -- ", "(", admin[0], admin[1], ")", "code: ", admin[2])

        # This try except is our type safe part of this function
        input_number_admin_for_remove = input(": ")
        try:
            int_input_number_admin_for_remove = int(input_number_admin_for_remove)

        except ValueError:
            return print("ValueError: You should type number not letters or something else.")

        condition_of_remove = False
        for admin in self.list_admin:
            if self.list_admin.index(admin)+1 == int_input_number_admin_for_remove:
                self.list_admin.pop(int_input_number_admin_for_remove - 1)
                condition_of_remove = True

        if condition_of_remove:
            print("Successful remove")

        else:
            print("Admin not found try again")

    # This function is a little difference and longer than previous functions
    # First highlighting an information that user want to modify
    # Then pop the last information then insert new information
    def modify_the_admin_information_by_super_admin(self):
        print("Enter one of this number to modify the information "
              "\n1 - Name admin\n2 - Last name admin\n3 - Admin code\n")
        input_number_information_admin = input(": ")

        # Make Type safe
        try:
            int_input_number_information_admin = int(input_number_information_admin)

        except ValueError:
            return print("ValueError: You should type just number")

        if int_input_number_information_admin > 3:
            return print("Error: Number not found")

        print("Enter number of admin that you want to remove")
        for admin in self.list_admin:
            print(self.list_admin.index(admin) + 1, " -- ", "(", admin[0], admin[1], ")", "code: ", admin[2])

        input_number_admin = input(": ")
        try:
            int_input_number_admin = int(input_number_admin)

        except ValueError:
            return print("ValueError: you should type just number")

        condition_of_change_last_name_admin = False
        condition_of_change_name_admin = False
        condition_of_change_admin_code = False

        if int_input_number_information_admin == 1:
            print("Enter new name")
            input_new_name_admin = input(": ")
            for admin_1 in self.list_admin:
                if self.list_admin.index(admin_1) + 1 == int_input_number_admin:
                    self.list_admin[int_input_number_admin - 1].pop(0)
                    self.list_admin[int_input_number_admin - 1].insert(0, input_new_name_admin)
                    condition_of_change_name_admin = True
                    break

        if int_input_number_information_admin == 2:
            print("Enter new last name")
            input_new_last_name_admin = input(": ")
            for admin_2 in self.list_admin:
                if self.list_admin.index(admin_2) + 1 == int_input_number_admin:
                    self.list_admin[int_input_number_admin - 1].pop(1)
                    self.list_admin[int_input_number_admin - 1].insert(1, input_new_last_name_admin)
                    condition_of_change_last_name_admin = True
                    break

        if int_input_number_information_admin == 3:
            print("Enter new admin code")
            input_new_admin_code = input(": ")
            try:
                int_input_new_admin_code = int(input_new_admin_code)

            except ValueError:
                return print("ValueError: You should type just number")

            for admin_3 in self.list_admin:
                if self.list_admin.index(admin_3) + 1 == int_input_number_admin:
                    self.list_admin[int_input_number_admin - 1].pop(2)
                    self.list_admin[int_input_number_admin - 1].insert(2, int_input_new_admin_code)
                    condition_of_change_admin_code = True
                    break

        if condition_of_change_name_admin or condition_of_change_last_name_admin or condition_of_change_admin_code:
            print("Change was successful")

        else:
            print("Changes not applied")

    # This function is for display each admin information to user choose intended admin
    def display_admins(self):
        for admin in self.list_admin:
            print(self.list_admin.index(admin) + 1, " -- ", "(", admin[0], admin[1], ")", "code: ", admin[2])

