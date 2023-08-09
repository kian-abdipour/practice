from manage_methods import manage_super_admin_methods
from manage_methods import manage_admin_methods
from manage_methods import manage_customer_methods


# Again in here we have tab manager that set each tab of role when will be show
# In here the user choose his role
def manage_tabs():
    print("Welcome to relax food")
    print("Type q to exist")

    progress = True
    while progress:
        print("Please choose your role \n1 -- customer\n2 -- admin\n3 -- super admin")
        input_number_role = input(": ")

        if input_number_role == "1":
            manage_customer_methods()

        elif input_number_role == "2":
            manage_admin_methods()

        elif input_number_role == "3":
            manage_super_admin_methods()

        if input_number_role == "q":
            progress = False


if __name__ == "__main__":
    manage_tabs()

else:
    print("you should run this program in the main file")

