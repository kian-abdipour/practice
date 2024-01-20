from restaurant.modul import (SuperAdmin, Admin, Customer, Category, Item,
                              Order, OrderItem, Payment, Address, category_item)
from manage_role_operation import manage_super_admin_operation


def main():
    manage_super_admin_operation()


if __name__ == '__main__':
    main()

else:
    print('Waring: This program should run from main file')

