import json


class Admin:
    def __init__(self, first_name=None, last_name=None, admin_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.admin_code = admin_code

    @staticmethod
    # This method is for login admin with a code that super admin set
    def admin_login():
        # Make type safe
        try:
            print("Enter your admin code")
            input_admin_code = int(input(": "))

        except ValueError:
            return print("ValueError: You should just type number")

        with open("admin_datas.json", "r") as admins_file:
            load_data = json.load(admins_file)

        for admin in load_data["admins"]:
            if admin["admin_code"] == input_admin_code:
                print(admin["first_name"], admin["last_name"], "welcome to your admin panel")
                return True

        return False

    @staticmethod
    # This method is one of actions that super admin can do
    # This method is clear and append a new admin to list_admin
    def add_admin():
        with open("admin_datas.json", "r") as admins_file:
            load_data = json.load(admins_file)

        print(f"Enter first name of admin {len(load_data['admins']) + 1}")
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
        data = {
            "first_name": admin.first_name,
            "last_name": admin.last_name,
            "admin_code": admin.admin_code
        }

        with open("admin_datas.json", "w") as admins_file:
            load_data["admins"].append(data)
            json.dump(load_data, admins_file)

        print("Add admin was successful")

    @staticmethod
    # This function is for display each admin information to user choose intended admin
    def display_admins():
        with open("admin_datas.json", "r") as admins_file:
            load_data = json.load(admins_file)

        if len(load_data["admins"]) > 0:
            for admin in load_data["admins"]:
                print(load_data["admins"].index(admin)+1, " _ ",
                      admin["first_name"],
                      admin["last_name"],
                      admin["admin_code"])
            return True

        else:
            return False

    @staticmethod
    # This method remove an admin from list_admin in SuperAdmin model that super admin want
    def remove_admin():
        with open("admin_datas.json", "r") as admins_file:
            load_data = json.load(admins_file)

        if Admin.display_admins():
            pass

        else:
            return print("Now we dont have admin")

        # This try except is our type safe part of this function
        try:
            print("Enter number of admin that you want to remove")
            number_admin = int(input(": "))

        except ValueError:
            return print("ValueError: You should type number not letters or something else.")

        condition_remove = False
        for admin in load_data["admins"]:
            if load_data["admins"].index(admin)+1 == number_admin:
                load_data["admins"].remove(admin)
                condition_remove = True

        with open("admin_datas.json", "w") as admins_file:
            json.dump(load_data, admins_file)

        if condition_remove:
            print("Remove admin was successful")

        else:
            print("Admin not found")

