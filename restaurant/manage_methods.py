from super_admin import SupperAdmin
from admin import Admin
from customer import Customer
from item import Item
from category import Category
from order import Order

super_admin = SupperAdmin("Kian", "Abdipour")  # This set default because it's name of owner's program


# This function manage super admin actions.
# In this program each action is a method and this function set that when to call each action
def manage_super_admin_methods():
    if super_admin.super_admin_login():
        print("Type q to go back")
        progress = True
        while progress:
            print("Enter one of this number \n1 -- add admin\n2 -- remove admin\n3 -- display admins")
            input_action_of_super_admin = input(": ")

            if input_action_of_super_admin == "1":
                Admin.add_admin()

            elif input_action_of_super_admin == "2":
                Admin.remove_admin()

            elif input_action_of_super_admin == "3":
                Admin.display_admins()

            else:
                print("Number not found")

            if input_action_of_super_admin == "q":
                progress = False


# This function exactly work like last one but the difference is that:
# This function manage admin methods
def manage_admin_methods():
    if Admin.admin_login():
        print("Type q to go back")
        progress = True
        while progress:
            print("Enter one of this number \n1 -- add item\n2 -- remove item\n3 -- menu"
                  "\n4 -- confirmation orders\n5 -- display account that have orders\n"
                  "6 -- add category\n7 -- remove category")
            input_action_of_admin = input(": ")

            if input_action_of_admin == "1":
                Item.add_item()

            elif input_action_of_admin == "2":
                Item.remove_item()

            elif input_action_of_admin == "3":
                Item.display_items()

            elif input_action_of_admin == "4":
                Order.confirmation_orders()

            elif input_action_of_admin == "5":
                Order.display_orders_and_receipt_for_admin()

            elif input_action_of_admin == "6":
                Category.add_category()

            elif input_action_of_admin == "7":
                Category.remove_categories()

            else:
                print("number not found")

            if input_action_of_admin == "q":
                progress = False


# This function work like pasts functions and set that when actions of customer will be call
def manage_customer_methods():
    print("Choose one of this number \n1 -- login\n2 -- signup\n")
    input_number_login_or_signup = input(": ")

    if input_number_login_or_signup == "1":
        if Customer.login_customer():
            progress = True
            print("Type q to go back")
            while progress:
                print("Enter one of this number \n1 -- order item\n2 -- list orders and receipt")
                input_number_actions_customer = input(": ")
                if input_number_actions_customer == "1":
                    Order.order_item()

                elif input_number_actions_customer == "2":
                    Order.display_orders_and_receipt_for_customer()

                else:
                    if input_number_actions_customer != "q":
                        print("Number not found")

                if progress == "q" or input_number_actions_customer == "q":
                    progress = False

    elif input_number_login_or_signup == "2":
        Customer.signup_customer()

