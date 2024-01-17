from super_admin import SuperAdmin


def manage_super_admin_operation():
    condition_login = SuperAdmin.login()
    if condition_login[0] and condition_login[1].username == 'Kian_abdipour':
        print('Enter a number\n1.add_admin\n2.add_super_admin\n3.delete_super_admin')
        operation = int(input(': '))
