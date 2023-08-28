from super_admin import SupperAdmin
from admin import Admin
from customer import Customer
from item import Item
from category import Category
from order import Order

super_admin = SupperAdmin("Kian", "Abdipour")  # This set default because it's name of owner's program


# This function manage methods that are in SuperAdmin class
# Actually this function set that when each method will be call
def manage_super_admin_methods():
    if super_admin.super_admin_login():
        print("Type q to go back")
        progress = True
        while progress:
            print("Enter one of this number \n1 -- add admin\n2 -- remove admin\n3 -- display admins")
            action_of_super_admin = input(": ")

            if action_of_super_admin == "1":
                Admin.add_admin()

            elif action_of_super_admin == "2":
                if len(Admin.admins) > 0:
                    Admin.remove_admin()

                else:
                    print("You don't have any admin, first you should add admin")

            elif action_of_super_admin == "3":
                if len(Admin.admins) > 0:
                    Admin.display_admins()

                else:
                    print("You don't have any admin, first you should add admin")

            else:
                print("Number not found")

            if action_of_super_admin == "q":
                progress = False


# This function exactly work like last function but the difference if that
# This function manage admin methods that are in Admin class
def manage_admin_methods():
    if Admin.admin_login():
        print("Type q to bo back")
        progress = True
        while progress:
            print("Enter one of this number \n1 -- add item\n2 -- remove item\n3 -- menu"
                  "\n4 -- confirmation orders\n5 -- display account that have orders\n6 -- add category")
            action_of_admin = input(": ")

            if action_of_admin == "1":
                if len(Category.categories) > 0:
                    Item.add_item()

                else:
                    print("You don't have any food, first you should add food to menu")

            elif action_of_admin == "2":
                if len(Category.categories) > 0:
                    Item.remove_item()

                else:
                    print("You don't have any food, first you should add food to menu")

            elif action_of_admin == "3":
                if len(Category.categories) > 0:
                    Category.display_menu()

                else:
                    print("You don't have any category, first you should add category to menu")

            elif action_of_admin == "4":
                if len(Order.orders) > 0:
                    Order.confirmation_the_orders()

                else:
                    print("Now we don't have any orders")

            elif action_of_admin == "5":
                Order.display_orders_and_receipt_for_admin()

            elif action_of_admin == "6":
                Category.add_category()

            else:
                print("number not found")

            if action_of_admin == "q":
                progress = False


# This function work like pasts functions and set that when each function will be run
def manage_customer_methods():
    print("Choose one of this number \n1 -- login\n2 -- signup\n")
    action_of_customer = input(": ")

    if action_of_customer == "1":
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

    elif action_of_customer == "2":
        Customer.signup_customer()

