from restaurant.modul import SuperAdmin

# In this program just super admin <<<kian_abdipour>>> can add or delete super admins and other super admins
# Can just add or delete admins


def manage_super_admin_operation():
    condition_login = SuperAdmin.login()
    if condition_login[0] and condition_login[1].username == 'kian_abdipour':
        proceed = True
        while proceed:
            print('Enter a number\n1.Add_admin\n2.Delete admin\n3.Add_super_admin\n4.Delete_super_admin\n5.back')

            try:
                operation = int(input(': '))

            except ValueError:
                return print('ValueError: You should type just number!')

            if operation == 3:
                if SuperAdmin.add():
                    print(f'Successfully added to super admins')

                else:
                    print('Adding operation was field')

            elif operation == 4:
                if SuperAdmin.delete():
                    print('Successfully deleted from super admins')

                else:
                    print('Deleting operation was field')

            elif operation == 5:
                proceed = False

            else:
                print('Number not found')

    elif condition_login[0]:
        print('Enter a number\n1.add_admin')
        try:
            operation = int(input(': '))

        except ValueError:
            return print('ValueError: You should type just number!')

        if operation == 1:
            pass

