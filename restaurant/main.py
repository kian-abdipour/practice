from manage_methods import manage_super_admin
from manage_methods import manage_admin
from manage_methods import manage_customer


def manage_pages():
    while_response = True
    print("Welcome to relax food")
    print("Type q to exist")

    while while_response:
        print("Please choose your role \n1 -- customer\n2 -- admin\n3 -- super admin")
        input_number_role = input(": ")

        if input_number_role == "1":
            manage_customer()

        elif input_number_role == "2":
            manage_admin()

        elif input_number_role == "3":
            manage_super_admin()

        if input_number_role == "q":
            while_response = False


if __name__ == "__main__":
    manage_pages()

else:
    print("you should run this program in the main file")

