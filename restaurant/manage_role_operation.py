from restaurant.modul import SuperAdmin, Admin, Category, Item, CategoryItem, Address

# In this program just super admin with username <<<kian_abdipour>>> can add or delete super admins and
# Other super admins can just add or delete admins


def manage_super_admin_operation():
    login = SuperAdmin.login()
    if login[0] and login[1].username == 'kian_abdipour':
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
            print('Enter a number \n1.Add category\n'
                  '2.Delete category\n3.Show category\n'
                  '4.Add item\n5.Show item\n6.Add item to category\n'
                  '7.delete item from category\n8.logout')

            try:
                operation = int(input(': '))

            except ValueError:
                print('ValueError: You should type just number!')
                operation = None

            if operation is not None:
                if operation == 1:
                    Category.add()

                elif operation == 2:
                    Category.delete()

                elif operation == 3:
                    print('Enter a number \n1.Show all\n2.Search')

                    try:
                        operation_show = int(input(': '))

                    except ValueError:
                        print('ValueError: You should type just number!')
                        operation_show = None

                    if operation_show == 1:
                        Category.show_all()

                    elif operation_show == 2:
                        category_id = Category.search()
                        if category_id is not False:
                            CategoryItem.show_item_side(category_id)

                    else:
                        print('Waring: Number not found')

                elif operation == 4:
                    if CategoryItem.match_row(Item.add()) is not True:
                        print('Your item it\'s not in any category')

                elif operation == 5:
                    print('Enter a number \n1.Show all\n2.Search\n3.Show item by category')
                    try:
                        operation_show = int(input(': '))

                    except ValueError:
                        print('ValueError: You should type just number!')
                        operation_show = None

                    if operation_show == 1:
                        Item.show_all()

                    elif operation_show == 2:
                        Item.search()

                    else:
                        print('Waring: Number not found')

                elif operation == 6:
                    item_id = Item.search().id
                    if item_id is not False:  # Ask question
                        CategoryItem.match_row(item_id)

                    else:
                        pass

                elif operation == 7:
                    category_id = Category.search()
                    if category_id is not False:
                        CategoryItem.show_item_side(category_id)
                        item_id = Item.search().id
                        if item_id is not False:
                            CategoryItem.delete(category_id, item_id)

                elif operation == 8:
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
                Address.show_all(customer_id)
                try:
                    address_id_user = int(input(': '))

                except ValueError:
                    print('ValueError: You should type just number')
                    address_id_user = None

                address_id_order = Address.search(address_id_user, customer_id)
                if address_id_order is not False:
                    list_item_to_order = []  # This is a list of all item that customer chose to order them
                    proceed_order = True
                    while proceed_order:
                        category_id = Category.search()
                        print('If it\'s finish type q')
                        if category_id is not False:
                            CategoryItem.show_item_side(category_id)
                            item = Item.search()
                            if item.stock > 0:
                                list_item_to_order.append(item)
                                print('Item successfully added')

                            else:
                                print(f'Sorry, but now we don\'t have {item.name}')

                        elif category_id == 'q':
                            proceed_order = False
                            if len(list_item_to_order) > 0:
                                Order.add()

            elif operation == 2:
                pass

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

