from super_admin import SupperAdmin

super_admin_obj = SupperAdmin("Kian", "Abdipour")


def super_admin():
    if super_admin_obj.super_admin_login():
        print("Enter one of this number \n1 -- add admin\n2 -- remove admin\n3 -- modify information of admin"
              "\n4 -- display admins")
        input_action_of_super_admin = input(": ")

        if input_action_of_super_admin == "1":
            super_admin_obj.add_admin_by_super_admin()

        if input_action_of_super_admin == "2":
            if len(super_admin_obj.list_admin) > 0:
                super_admin_obj.remove_admin_by_supper_admin()

            else:
                print("You don't have any admin, first you should add admin")

        if input_action_of_super_admin == "3":
            if len(super_admin_obj.list_admin) > 0:
                super_admin_obj.modify_the_admin_information_by_super_admin()

            else:
                print("You don't have any admin, first you should add admin")

        if input_action_of_super_admin == "4":
            super_admin_obj.display_admins()

        else:
            print("Number not found")
