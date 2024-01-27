from restaurant.modul import SuperAdmin, Admin, Category, Item, CategoryItem

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
                proceed = False
                return None

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
                return None

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
                  '7.delete item from category\n8.Back')

            try:
                operation = int(input(': '))

            except ValueError:
                print('ValueError: You should type just number!')
                operation = None

            if operation == 1:
                Category.add()

            elif operation == 2:
                Category.delete()

            elif operation == 3:
                Category.show_category()

            elif operation == 4:
                if CategoryItem.match_row(Item.add()) is not True:
                    print('Your item it\'s not in any category')

            elif operation == 5:
                print('Enter a number \n1.Show all\n2.Search')
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
                item_id = Item.search()
                if type(item_id) == int:  # Ask question
                    CategoryItem.match_row(item_id)

                else:
                    pass

            elif operation == 7:
                pass

            elif operation == 8:
                proceed = False

            else:
                print('Waring: Operation not found!, try again')


def manage_customer_operation():
    pass

