from restaurant.modul import (SuperAdmin, Admin, Customer, Category, Item,
                              Order, OrderItem, Payment, Address, category_item)
from manage_role_operation import manage_super_admin_operation, manage_admin_operation, manage_customer_operation


def main():
    proceed = True
    while proceed:
        print('Choose your role \n1.Customer\n2.Admin\n3.Super admin\n4.Exit')
        # Make type safing
        try:
            operation = int(input(': '))

        except ValueError:
            print('Waring: You should type just number')
            operation = None

        if operation is not None:

            if operation == 1:
                proceed_admin = True
                while proceed_admin:

                    print('Enter a number \n1.Login\n2.Signup\n3.Back')
                    try:
                        operation_admin = int(input(': '))

                    except ValueError:
                        print('ValueError: You should type just number')
                        operation_admin = None

                    if operation_admin is not None:
                        if operation_admin == 1:
                            if Customer.login():
                                manage_customer_operation()

                        elif operation_admin == 2:
                            if Customer.signup():
                                manage_customer_operation()

                        elif operation_admin == 3:
                            proceed_admin = False

                        else:
                            print('Number not found')

            elif operation == 2:
                manage_admin_operation()

            elif operation == 3:
                manage_super_admin_operation()

            elif operation == 4:
                proceed = False

            else:
                print('Number not found')


if __name__ == '__main__':
    main()

else:
    print('Waring: This program should run from main file')

