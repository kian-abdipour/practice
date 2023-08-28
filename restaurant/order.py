from category import Category
from customer import Customer
from decorators import representing


class Order:
    orders = []

    def __init__(self, customer_that_is_order=None):
        self.customer_that_is_order = customer_that_is_order
        self.items = []

    @classmethod
    @representing
    # This method first display menu then get the number of food that customer want to order
    # Then add this food to list_customer that are in list_information_login_customer
    def order_item(cls):
        Category.display_categories()

        try:
            number_category = int(input(": ")) - 1
            # This variable is for handle index error
            last_item_list_food = Category.categories[number_category - 1]

        except ValueError:
            return print("ValueError: You must type just number")

        except IndexError:
            return print("IndexError: Number not found")

        for category in Category.categories:
            if Category.categories.index(category) == number_category:
                for item in category.items:
                    print(category.items.index(item) + 1, " -- ", item.name, "price: ", item.price)

        try:
            number_item = int(input(": ")) - 1

        except ValueError:
            return print("ValueError: Number not found")

        condition_of_select_item = False
        for category in Category.categories:
            if Category.categories.index(category) == number_category:
                for item in category.items:
                    if category.items.index(item) == number_item:
                        selected_item = item
                        condition_of_select_item = True

        if condition_of_select_item:
            for customer_element in Customer.information_customers:
                if Customer.username_login_customer_for_now == customer_element.username:
                    order = Order(customer_element)
                    order.items.append(selected_item)

            condition_of_order = False
            for order_2 in cls.orders:
                if order_2.customer_that_is_order.username == Customer.username_login_customer_for_now:
                    order_2.items.append(selected_item)
                    print("Record item was successful")
                    condition_of_order = True

            if not condition_of_order:
                cls.orders.append(order)

        else:
            print("Number not found")

    @classmethod
    # This method display order of account that is login and show the total fee of order
    def display_orders_and_receipt_for_customer(cls):
        total = 0
        for order in cls.orders:
            if order.customer_that_is_order.username == Customer.username_login_customer_for_now:
                for item in order.items:
                    print(order.customer_that_is_order.username, " -- ", item.name, "Price: ", item.price)
                    total += item.price

        print("Total: ", total)

    @classmethod
    # This method is like last one but the difference is that
    # Last one display just one orders that is for customer is login now but this method
    # Display all orders that we have in list_orders for admin
    def display_orders_and_receipt_for_admin(cls):
        total = 0
        if len(cls.orders) > 0:
            for order in cls.orders:
                for item in order.items:
                    print(order.customer_that_is_order.username, " -- ", item.name, "Price:",  item.price)
                    total += item.price

                print(order.customer_that_is_order.username, " -- total: ", total)
                total = 0

        else:
            print("Now we don't have any order")

    @classmethod
    @representing
    # This first display the orders that are in list_orders
    # Then set the order that admin want and remove if from list_orders
    def confirmation_the_orders(cls):
        progress = True
        while progress:
            Order.display_orders_and_receipt_for_admin()
            username_for_confirmation = input(": ")
            condition_of_confirmation = False
            for order in cls.orders:
                if order.customer_that_is_order.username == username_for_confirmation:
                    cls.orders.remove(order)
                    condition_of_confirmation = True

            else:
                print("Please enter username of user that you want to confirm his orders")

            if condition_of_confirmation:
                print("Confirmation was successful")

            else:
                print("Username not found")

            if username_for_confirmation == "q":
                progress = False

