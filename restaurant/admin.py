import json


class Admin:
    def __init__(self, first_name=None, last_name=None, admin_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.admin_code = admin_code

    @staticmethod
    # This method is for login admin with a code that super admin set and load a data
    # That is in admin_datas.json then check admin codes that we have in load_data
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
    # This method load a data that is in admin_datas.json
    # Then get the information of admin for adding and append it to load_date and dump a new version of load_data to
    # admin_datas.json
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
    # This method load a data that is in admin_datas.json and print each element of it that is dictionary
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
    # This method first display Admins with display_admins method that is in Admin then
    # From loaded data remove specified admin and dump a new version of load_data to admin_datas.json
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

