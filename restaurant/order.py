from menu import Menu
from customer import list_information_signup_customer
from customer import Customer

list_orders = []
#customer = Customer()


class Order:
    def __init__(self, customer_that_is_order=None):
        self.customer_that_is_order = customer_that_is_order
        self.list_items = []

    @staticmethod
    # This method first display menu then get the number of food that customer want to order
    # Then add this food to list_customer that are in list_information_login_customer
    def order_item():
        Menu.display_categories()

        try:
            number_category = int(input(": ")) - 1
            # This variable is for handle index error
            last_item_list_food = Menu.list_categories[number_category - 1]

        except ValueError:
            return print("ValueError: You must type just number")

        except IndexError:
            return print("IndexError: Number not found")

        for category in Menu.list_categories:
            if Menu.list_categories.index(category) == number_category:
                for item in category.list_items:
                    print(category.list_items.index(item) + 1, " -- ", item.name, "price: ", item.price)

        try:
            number_item = int(input(": ")) - 1

        except ValueError:
            return print("ValueError: Number not found")

        condition_of_select_item = False
        for category in Menu.list_categories:
            if Menu.list_categories.index(category) == number_category:
                for item in category.list_items:
                    if category.list_items.index(item) == number_item:
                        selected_item = item
                        condition_of_select_item = True

        if condition_of_select_item:
            for customer in list_information_signup_customer:
                if Customer.username_login_customer_for_now == customer.username:
                    order = Order(customer)
                    order.list_items.append(selected_item)

            condition_of_order = False
            for order in list_orders:
                if order.customer_that_is_order.username == Customer.username_login_customer_for_now:
                    order.list_items.append(selected_item)
                    print("Record item was successful")
                    condition_of_order = True

            if condition_of_order:
                print("True")
                print(list_orders)
                pass

            else:
                list_orders.append(order)
                print("False")
                print(list_orders)

        else:
            print("Number not found")

    @staticmethod
    # This method display order of account that user say and show the total of fee's order
    def display_orders_and_receipt():
        total = 0
        for order in list_orders:
            if order.customer_that_is_order.username == Customer.username_login_customer_for_now:
                print("found")
                for item in order.list_items:
                    print("found_2")
                    print(order.customer_that_is_order.username, " -- ", item.name, "Price: ", item.price)
                    total += item.price

        print("Total: ", total)

