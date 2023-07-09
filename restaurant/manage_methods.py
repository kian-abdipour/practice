from super_admin import SupperAdmin
from admin import Admin
from menu import Menu
from customer import Customer
from customer import list_information_signup_customer

super_admin_obj = SupperAdmin("Kian", "Abdipour")
admin_obj = Admin()

customer_obj = Customer()


# This function manage methods that are in SuperAdmin class
# Actually this function set that when each method will be run
def manage_super_admin():
    if super_admin_obj.super_admin_login():
        print("Type q to go back")
        while_response = True
        while while_response:
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

            if input_action_of_super_admin == "q":
                while_response = False


# This function exactly work like last function but the difference if that
# This function manage admin methods that are in Admin class
def manage_admin():
    if admin_obj.admin_login():
        print("Type q to bo back")
        while_response = True
        while while_response:
            print("Enter one of this number \n1 -- add food\n2 -- remove food\n3 -- menu"
                  "\n4 -- confirmation transactions")
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

            if input_action_of_admin == "q":
                while_response = False


def manage_customer():
    print("Choose one of this number \n1 -- login\n2 -- signup\n")
    input_number_login_or_signup = input(": ")

    if input_number_login_or_signup == "1":
        if Customer.login_customer():
            while_response = True
            print("Type q to go back")
            while while_response:
                print("Enter one of this number \n1 -- order food\n2 -- list orders")
                input_number_actions_customer = input(": ")
                if input_number_actions_customer == "1":
                    customer_obj.order_food()

                elif input_number_actions_customer == "2":
                    customer_obj.display_orders()

                else:
                    print("Number not found")

                if while_response == "q" or input_number_actions_customer == "q":
                    while_response = False

    elif input_number_login_or_signup == "2":
        customer_obj.signup_customer()
