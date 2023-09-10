from decorators import representing


class SupperAdmin:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    super_admin_code = 1386

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

