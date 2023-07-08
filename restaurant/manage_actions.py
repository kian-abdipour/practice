from super_admin import SupperAdmin
from admin import Admin
from menu import Menu

super_admin_obj = SupperAdmin("Kian", "Abdipour")
admin_obj = Admin()


# This function manage methods that are in SuperAdmin class
# Actually this function set that when each method will be run
def super_admin():
    if super_admin_obj.super_admin_login():
        print("Enter one of this number \n1 -- add admin\n2 -- remove admin\n3 -- modify information of admin"
              "\n4 -- display admins")
        input_action_of_super_admin = input(": ")

        if input_action_of_super_admin == "1":
            super_admin_obj.add_admin_by_super_admin()

        elif input_action_of_super_admin == "2":
            if len(super_admin_obj.list_admin) > 0:
                super_admin_obj.remove_admin_by_supper_admin()

            else:
                print("You don't have any admin, first you should add admin")

        elif input_action_of_super_admin == "3":
            if len(super_admin_obj.list_admin) > 0:
                super_admin_obj.modify_the_admin_information_by_super_admin()

            else:
                print("You don't have any admin, first you should add admin")

        elif input_action_of_super_admin == "4":
            super_admin_obj.display_admins()

        else:
            print("Number not found")


# This function exactly work like last function but the difference if that
# This function manage admin methods that are in Admin class
def admin():
    if admin_obj.admin_login():
        print("Enter one of this number \n1 -- add food\n2 -- remove food\n3 -- menu\n4 -- confirmation transactions")
        input_action_of_admin = input(": ")

        if input_action_of_admin == "1":
            admin_obj.add_food()

        elif input_action_of_admin == "2":
            if len(Menu.list_food) > 0:
                admin_obj.remove_food()

            else:
                print("You don't have any food, first you should add food to menu")

        elif input_action_of_admin == "3":
            if len(Menu.list_food) > 0:
                admin_obj.display_menu()

            else:
                print("You don't have any food, first you should add food to menu")

        elif input_action_of_admin == "4":
            pass

        else:
            print("number not found")
