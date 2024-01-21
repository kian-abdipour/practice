from restaurant.modul import (SuperAdmin, Admin, Customer, Category, Item,
                              Order, OrderItem, Payment, Address, category_item)
from manage_role_operation import manage_super_admin_operation


def main():
    proceed = True
    while proceed:
        print('Choose your role \n1.customer\n2.admin\n3.super admin\n4.exit')
        # Make type safing
        try:
            operation = int(input(': '))

        except ValueError:
            print('Waring: You should type just number')
            operation = None

        if operation == 2:
            Admin.login()

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

