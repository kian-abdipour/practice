from restaurant.modul import SuperAdmin

# In this program just super admin <<<kian_abdipour>>> can add or delete super admins and other super admins
# Can just add or delete admins


def manage_super_admin_operation():
    condition_login = SuperAdmin.login()
    if condition_login[0] and condition_login[1].username == 'kian_abdipour':
        print('Enter a number\n1.add_admin\n2.add_super_admin\n3.delete_super_admin')

        try:
            operation = int(input(': '))

        except ValueError:
            return print('ValueError: You should type just number!')

        if operation == 2:
            if SuperAdmin.add():
                print(f'Successfully added to super admins')

            else:
                print('Adding operation was field')

        elif operation == 3:
            if SuperAdmin.delete():
                print('Successfully deleted from super admins')

            else:
                print('Deleting operation was field')

    elif condition_login[0]:
        print('Enter a number\n1.add_admin')
        try:
            operation = int(input(': '))

        except ValueError:
            return print('ValueError: You should type just number!')

        if operation == 1:
            pass

