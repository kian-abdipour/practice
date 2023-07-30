class SupperAdmin:
    def __new__(cls, *args, **kwargs):
        print("Instance of SupperAdmin hase created")
        instance = super().__new__(cls)
        return instance

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    super_admin_code = "1386"
    list_admin = []

    # This function is for login super admin, and we have just one super admin in this program
    # If condition of login will be true user can continue ass super admin
    def super_admin_login(self):
        print("Enter super admin code login")
        super_admin_code = input(": ")

        condition_of_login_super_admin = False
        if super_admin_code == self.super_admin_code:
            condition_of_login_super_admin = True

        else:
            print("super admin code not found")

        return condition_of_login_super_admin

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

    # This function is for display each admin information to user choose intended admin
    def display_admins(self):
        for admin in self.list_admin:
            print(self.list_admin.index(admin) + 1, " -- ", "(", admin.first_name, admin.last_name, ")",
                  "code: ", admin.admin_code)

#    def __getattr__(self, attribute):
#        return print("{attribute} Attribute not found".format(attribute=attribute))

    def __repr__(self):
        return ("This model has first_name and last_name attribute and you should define it by positional "
                "argument like this super_admin = SuperAdmin('kian', 'abdipour')")

    def __str__(self):
        return f"Super admin: {self.first_name} {self.last_name}"

