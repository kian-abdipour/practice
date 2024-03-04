from restaurant.model import (SuperAdmin, Admin, Category, Item, CategoryItem, Address,
                              Order, OrderItem, Payment, Discount, DiscountHistory)

from dotenv import load_dotenv
from os import getenv

# In this program just super admin with username ----- can add or delete super admins and
# Other super admins can just add or delete admins
load_dotenv()

super_admin_username = getenv('SUPER_ADMIN_URL')  # This our super_admin username with higher access


def manage_super_admin_operation():
    login = SuperAdmin.login()
    if login[0] and login[1].username == super_admin_username:
        proceed = True
        while proceed:
            print('Enter a number\n1.Add admin\n2.Delete admin'
                  '\n3.Add super admin\n4.Delete super admin'
                  '\n5.Show super admin\n6.show admin\n7.logout')

            try:
                operation = int(input(': '))

            except ValueError:
                print('ValueError: You should type just number!')
                operation = None

            if operation is not None:

                if operation == 1:
                    if Admin.add(login[1].id):
                        print('Successfully added to admins')

                    else:
                        print('Adding operation was field')

                elif operation == 2:
                    if Admin.delete():
                        print('Successfully deleted from admins')

                    else:
                        print('Deleting operation was field')

                elif operation == 3:
                    if SuperAdmin.add():
                        print('Successfully added to super admins')

                    else:
                        print('Adding operation was field')

                elif operation == 4:
                    if SuperAdmin.delete():
                        print('Successfully deleted from super admins')

                    else:
                        print('Deleting operation was field')

                elif operation == 5:
                    SuperAdmin.show_super_admin()

                elif operation == 6:
                    Admin.show_admin()

                elif operation == 7:
                    return

                else:
                    print('Number not found')

    if login[0]:  # Check this line againe to undrestand what was the bug for
        proceed_for_other_super_admin = True  # Check this line againe to undrestand what was the bug for
        while proceed_for_other_super_admin:  # Check this line againe to undrestand what was the bug for
            print('Enter a number\n1.add admin\n2.delete admin\n3.show admin\n4.logout')
            try:
                operation = int(input(': '))

            except ValueError:
                print('ValueError: You should type just number!')
                operation = None

            if operation is not None:
                if operation == 1:
                    if Admin.add(login[1].id):
                        print('Successfully added to admins')

                    else:
                        print('Adding operation was field')

                elif operation == 2:
                    if Admin.delete():
                        print('Successfully deleted from admins')

                    else:
                        print('Deleting operation was field')

                elif operation == 3:
                    Admin.show_admin()

                elif operation == 4:
                    proceed_for_other_super_admin = False

                else:
                    print('Number not found')


def manage_admin_operation():
    login = Admin.login()
    if login[0]:
        proceed = True
        while proceed:
            print('Enter a number\n1.Manage category\n2.Manage item\n3.Manage order\n4.Manage discount\n5.Logout')

            try:
                operation = int(input(': '))

            except ValueError:
                print('ValueError: You should type just number!')
                operation = None

            if operation is not None:
                if operation == 1:
                    print('Enter a number \n1.Show all\n2.Search\n3.Add\n4.Delete')

                    try:
                        operation_manage_category = int(input(': '))

                    except ValueError:
                        print('ValueError: You should type just number!')
                        operation_manage_category = None

                    if operation_manage_category == 1:
                        Category.show_all()

                    elif operation_manage_category == 2:
                        category = Category.search()
                        if category[0] is not False:
                            CategoryItem.show_item_side(category[0].id)

                    elif operation_manage_category == 3:
                        Category.add()

                    elif operation == 4:
                        Category.delete()

                    else:
                        print('Waring: Number not found')

                elif operation == 2:
                    print('Enter a number \n1.Show all\n2.Search\n4.Add\n5.Delete'
                          '\n6.Add item to categroy\n7.Delete item from categroy')
                    try:
                        operation_manage_item = int(input(': '))

                    except ValueError:
                        print('ValueError: You should type just number!')
                        operation_manage_item = None

                    if operation_manage_item == 1:
                        Item.show_all()

                    elif operation_manage_item == 2:
                        Item.search()

                    elif operation_manage_item == 4:
                        CategoryItem.match_row(Item.add())

                    elif operation_manage_item == 6:
                        item_id = Item.search().id
                        if item_id is not False:  # Ask question
                            CategoryItem.match_row(item_id)

                        else:
                            pass

                    elif operation_manage_item == 7:
                        category = Category.search()
                        if category[0] is not False:
                            CategoryItem.show_item_side(category[0].id)
                            item_id = Item.search().id
                            if item_id is not False:
                                CategoryItem.delete(category[0].id, item_id)

                    else:
                        print('Waring: Number not found')

                elif operation == 3:
                    proceed_confirm_order = True
                    while proceed_confirm_order:
                        print('Enter a number \n1.Confirm order\n2.Show all order\n3.Back')
                        try:
                            operation_order = int(input(': '))

                        except ValueError:
                            print('Waring: You should type just number')
                            operation_order = None

                        if operation_order is not None:
                            if operation_order == 1:
                                Order.show_all_waiting_to_confirm()
                                Order.confirm()

                            elif operation_order == 2:
                                Order.show_all_waiting_to_confirm()

                            elif operation_order == 3:
                                proceed_confirm_order = False

                elif operation == 4:
                    print('Enter a number \n1.Add discount\n2.Delete discount\n3.Show all')
                    try:
                        operation_discount = int(input(': '))

                    except ValueError:
                        print('ValueError: You should type just number')
                        operation_discount = None

                    if operation_discount is not None:
                        if operation_discount == 1:
                            Discount.add(Discount.generate_code())

                        elif operation_discount == 2:
                            Discount.delete()

                        elif operation_discount == 3:
                            Discount.show_all()

                        else:
                            print('Number not found')

                elif operation == 5:
                    proceed = False

                else:
                    print('Waring: Operation not found!, try again')


def manage_customer_operation(customer_id):
    proceed = True
    while proceed:
        print('Enter a number \n1.Order\n2.Show order\n3.Manage address\n4.Logout')
        try:
            operation = int(input(': '))

        except ValueError:
            print('ValueError: You should type just number')
            operation = None

        if operation is not None:
            if operation == 1:
                print('Enter id of your address')
                if Address.show_all(customer_id):
                    try:
                        address_id_user = int(input(': '))

                    except ValueError:
                        print('ValueError: You should type just number')
                        address_id_user = None

                    address_id_order = Address.search(address_id_user, customer_id)
                    if address_id_order is not False:
                        list_item_to_order = []  # This is a list of all item that customer choose to order them
                        list_item_id = []  # This is a list of all item id that user choose to order
                        proceed_order = True
                        while proceed_order:

                            print('If it\'s finish type q to go to payment '
                                  'part if you selected item, else it will go back')
                            category = Category.search()
                            if category[0] is not False:
                                print('Items in this category:')

                                if CategoryItem.show_item_side(category[0].id):
                                    item = Item.search()
                                    if item is not False:
                                        if item.stock > 0:
                                            if list_item_id.count(item.id) < item.stock:
                                                list_item_to_order.append(item)
                                                list_item_id.append(item.id)
                                                print('Item successfully added')

                                            else:
                                                print(f'Waring: Stock of {item.name} is finished')

                                        else:
                                            print(f'Now we don\'t have {item.name}')

                            elif category[1] == 'q':
                                proceed_order = False
                                if len(list_item_to_order) > 0:
                                    order = Order.add(customer_id, address_id_order)
                                    OrderItem.add(order.id, list_item_to_order, list_item_id)

                                    proceed_payment = True
                                    while proceed_payment:
                                        if Payment.add(list_item_to_order, order.id, customer_id) is False:

                                            print('If you want to pay again type yes, else type no')
                                            operation_pay_again = input(': ')
                                            if operation_pay_again == 'Yes' or operation_pay_again == 'yes':
                                                Payment.add(list_item_to_order, order.id, customer_id)
                                                proceed_payment = False

                                            elif operation_pay_again == 'No' or operation_pay_again == 'No':
                                                proceed_payment = False

                                            else:
                                                print('Waring: You should just type yes for pay again,'
                                                      ' and no for go back')

                                        else:
                                            proceed_payment = False

                                else:
                                    print('You does not select any item to be order')

            elif operation == 2:
                proceed_show_order = True
                while proceed_show_order:
                    print('Enter a number \n1.Show your all order\n2.Back')
                    try:
                        operation_show_order = int(input(': '))

                    except ValueError:
                        print('ValueError: You should type just number')
                        operation_show_order = None

                    if operation_show_order is not None:
                        if operation_show_order == 1:
                            Order.show_all_for_customer(customer_id)

                        elif operation_show_order == 2:
                            proceed_show_order = False

                        else:
                            print('Waring: Number not found')

            elif operation == 3:
                print('Enter a number \n1.Show Your addresses\n2.Add address\n3.Delete address')
                try:
                    operation_address = int(input(': '))

                except ValueError:
                    print('ValueError: You should type just number')
                    operation_address = None

                if operation_address is not None:
                    if operation_address == 1:
                        Address.show_all(customer_id)

                    elif operation_address == 2:
                        Address.add(customer_id)

                    elif operation_address == 3:
                        print('Enter id of address that you want to delete')
                        Address.show_all(customer_id)
                        try:
                            address_id_user = int(input(': '))

                        except ValueError:
                            print('ValueError: You should type just number')
                            address_id_user = None

                        Address.delete(address_id_user, customer_id)

            elif operation == 4:
                proceed = False

            else:
                print('Waring: Number not found')

