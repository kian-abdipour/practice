from super_admin import SupperAdmin
from admin import Admin
from customer import Customer
from item import Item
from category import Category
from customer import list_categories

super_admin = SupperAdmin("Kian", "Abdipour")  # This set default because it's name of owner's program
admin = Admin()
customer = Customer()
item = Item()
category = Category()


# This function manage methods that are in SuperAdmin class
# Actually this function set that when each method will be run
def manage_super_admin_methods():
    if super_admin.super_admin_login():
        print("Type q to go back")
        progress = True
        while progress:
            print("Enter one of this number \n1 -- add admin\n2 -- remove admin\n3 -- modify information of admin"
                  "\n4 -- display admins")
            input_action_of_super_admin = input(": ")

            if input_action_of_super_admin == "1":
                admin.add_admin()

            elif input_action_of_super_admin == "2":
                if len(super_admin.list_admin) > 0:
                    super_admin.remove_admin_by_supper_admin()

                else:
                    print("You don't have any admin, first you should add admin")

            elif input_action_of_super_admin == "3":
                if len(super_admin.list_admin) > 0:
                    super_admin.modify_the_admin_information_by_super_admin()

                else:
                    print("You don't have any admin, first you should add admin")

            elif input_action_of_super_admin == "4":
                super_admin.display_admins()

            else:
                print("Number not found")

            if input_action_of_super_admin == "q":
                progress = False


# This function exactly work like last function but the difference if that
# This function manage admin methods that are in Admin class
def manage_admin_methods():
    if admin.admin_login():
        print("Type q to bo back")
        progress = True
        while progress:
            print("Enter one of this number \n1 -- add food\n2 -- remove food\n3 -- menu"
                  "\n4 -- confirmation transactions\n5 -- display account that have orders\n6 -- add category")
            input_action_of_admin = input(": ")

            if input_action_of_admin == "1":
                if len(list_categories) > 0:
                    Item.add_item()

                else:
                    print("You don't have any food, first you should add food to menu")

            elif input_action_of_admin == "2":
                if len(list_categories) > 0:
                    item.remove_item()

                else:
                    print("You don't have any food, first you should add food to menu")

            elif input_action_of_admin == "3":
                if len(list_categories) > 0:
                    customer.display_menu()

                else:
                    print("You don't have any category, first you should add category to menu")

            elif input_action_of_admin == "4":
                admin.confirmation_the_orders()

            elif input_action_of_admin == "5":
                admin.display_orders_of_customer()

            elif input_action_of_admin == "6":
                category.add_category()

            else:
                print("number not found")

            if input_action_of_admin == "q":
                progress = False


# This function work like past's functions and set that when each function will be run
def manage_customer_methods():
    print("Choose one of this number \n1 -- login\n2 -- signup\n")
    input_number_login_or_signup = input(": ")

    if input_number_login_or_signup == "1":
        if Customer.login_customer():
            progress = True
            print("Type q to go back")
            while progress:
                print("Enter one of this number \n1 -- order food\n2 -- list orders and receipt")
                input_number_actions_customer = input(": ")
                if input_number_actions_customer == "1":
                    customer.order_item()

                elif input_number_actions_customer == "2":
                    customer.display_orders_and_receipt()

                else:
                    if input_number_actions_customer != "q":
                        print("Number not found")

                if progress == "q" or input_number_actions_customer == "q":
                    progress = False

    elif input_number_login_or_signup == "2":
        customer.signup_customer()

