list_information_login_customer = []  # All data that we have about customer is in this variable as list
list_categories = []  # All instance about categories and items are in this variable


class Customer:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.list_orders = []
    username_login_customer_for_now = None  # This is for set a username that is login now and do some method on it

    @staticmethod
    # This method get the user's username and password then append to list_information_login_customer
    def signup_customer():
        print("Enter your username")
        username = input(": ")

        print("Enter your password")
        password = input(": ")

        customer = Customer(username, password)
        list_information_login_customer.append(customer)

    @classmethod
    # This method check that we have this username pass or not if we don't have customer can't see the next
    # Page
    def login_customer(cls):
        print("Please enter username of your relax account")
        login_username = input(": ")

        print("Please enter password of your relax account")
        signup_password = input(": ")

        cls.username_login_customer_for_now = login_username
        condition_of_login = False
        for customer in list_information_login_customer:
            if customer.username == login_username and customer.password == signup_password:
                condition_of_login = True

        if condition_of_login:
            print("Welcome to relax account ", login_username)

        else:
            print("Username or password not found")

        return condition_of_login

    @staticmethod
    def display_categories():
        if len(list_categories) > 0:
            for category in list_categories:
                print(list_categories.index(category) + 1, " -- ", category.name)

        else:
            print("Now we don't have any category")

    # This method first display menu then get the number of food that customer want to order
    # Then add this food to list_customer that are in list_information_login_customer
    def order_item(self):
        Customer.display_categories()

        try:
            number_category = int(input(": ")) - 1
            # This variable is for handle index error
            last_item_list_food = list_categories[number_category - 1]

        except ValueError:
            return print("ValueError: You must type just number")

        except IndexError:
            return print("IndexError: You must type just number")
        
        for category in list_categories:
            if list_categories.index(category) == number_category:
                for item in category.list_items:
                    print(category.list_items.index(item) + 1, " -- ", item.name, "price: ", item.price)
        
        try:
            number_item = int(input(": ")) - 1
            
        except ValueError:
            return print("ValueError: Number not found")

        condition_of_select_item = False
        for category in list_categories:
            if list_categories.index(category) == number_category:
                for item in category.list_items:
                    if category.list_items.index(item) == number_item:
                        selected_item = item
                        condition_of_select_item = True

        if condition_of_select_item:
            for customer in list_information_login_customer:
                if self.username_login_customer_for_now == customer.username:
                    customer.list_orders.append(selected_item)
                    print("Record item was successful")

        else:
            print("Number not found")

    @classmethod
    # This method display order of account that user say and show the total of fee's order
    def display_orders_and_receipt(cls):
        total = 0
        for customer in list_information_login_customer:
            if customer.username == cls.username_login_customer_for_now:
                if len(customer.list_orders) > 0:
                    for order in customer.list_orders:
                        print(customer.list_orders.index(order) + 1, " -- ", order.name,
                              "price: ", order.price)
                        total += order.price

        print("total: ", total)

    @staticmethod
    def display_menu():
        print("Enter a number\n1 -- All menu\n2 -- All category\n3 -- Number of each category that use")
        number_type_of_display = input(": ")
        if number_type_of_display == "1":
            for category in list_categories:
                if len(category.list_items) > 0:
                    for item in category.list_items:
                        print(category.list_items.index(item) + 1, " -- ", "(", item.name,
                              "category:", category.name, ")",
                              "price:", item.price)

                else:
                    print("We don't have any food in", category.name)

        elif number_type_of_display == "2":
            Customer.display_categories()

        elif number_type_of_display == "3":
            for category in list_categories:
                print(list_categories.index(category) + 1, " -- ", category.name + ":", len(category.list_items))

        else:
            print("Number not found")

    def __repr__(self):
        return ("This model hase 2 attribute username and password, and you define instance by positional argument"
                "like this: customer: Customer(kian, 'bmw1386z4')")

    def __str__(self):
        return f"Customer: {self.username} password: {self.password}"
