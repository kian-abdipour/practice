from menu import Menu
from customer import list_information_signup_customer
from customer import Customer
from decorators import representing

list_orders = []


class Order:
    def __init__(self, customer_that_is_order=None):
        self.customer_that_is_order = customer_that_is_order
        self.list_items = []

    @staticmethod
    @representing
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
            for order_2 in list_orders:
                if order_2.customer_that_is_order.username == Customer.username_login_customer_for_now:
                    order_2.list_items.append(selected_item)
                    print("Record item was successful")
                    condition_of_order = True

            if not condition_of_order:
                list_orders.append(order)

        else:
            print("Number not found")

    @staticmethod
    # This method display order of account that is login and show the total fee of order
    def display_orders_and_receipt_for_customer():
        total = 0
        for order in list_orders:
            if order.customer_that_is_order.username == Customer.username_login_customer_for_now:
                for item in order.list_items:
                    print(order.customer_that_is_order.username, " -- ", item.name, "Price: ", item.price)
                    total += item.price

        print("Total: ", total)

    @staticmethod
    # This method is like last one but the difference is that
    # Last one display just one orders that is for customer is login now but this method
    # Display all orders that we have in list_orders for admin
    def display_orders_and_receipt_for_admin():
        total = 0
        if len(list_orders) > 0:
            for order in list_orders:
                for item in order.list_items:
                    print(order.customer_that_is_order.username, " -- ", item.name, "Price:",  item.price)
                    total += item.price

                print(order.customer_that_is_order.username, " -- total: ", total)

        else:
            print("Now we don't have any order")

    @staticmethod
    @representing
    # This first display the orders that are in list_orders
    # Then set the order that admin want and remove if from list_orders
    def confirmation_the_orders():
        progress = True
        while progress:
            Order.display_orders_and_receipt_for_admin()
            username_for_confirmation = input(": ")
            condition_of_confirmation = False
            for order in list_orders:
                if order.customer_that_is_order.username == username_for_confirmation:
                    list_orders.remove(order)
                    condition_of_confirmation = True

            else:
                print("Please enter username of user that you want to confirm his orders")

            if condition_of_confirmation:
                print("Confirmation was successful")

            else:
                print("Username not found")

            if username_for_confirmation == "q":
                progress = False

