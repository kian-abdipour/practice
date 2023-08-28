from category import Category
from customer import Customer
from decorators import representing
import copy


class Order:
    orders = []

    def __init__(self, username_that_is_order=None, item=None):
        self.username_that_is_order = username_that_is_order
        self.item = item

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

        for category in Category.categories:
            if Category.categories.index(category) == number_category:
                for item in category.items:
                    if category.items.index(item) == number_item:
                        order = Order(Customer.username_that_is_login, item)
                        cls.orders.append(order)
                        print("Order was successful")

    @classmethod
    # This method display order of account that is login and show the total fee of order
    def display_orders_and_receipt_for_customer(cls):
        total = 0
        for order in cls.orders:
            if order.username_that_is_order == Customer.username_that_is_login:
                print(order.username_that_is_order, " -- ", order.item.name, "Price: ", order.item.price)
                total += order.item.price

        print("Total: ", total)

    @classmethod
    # This method is like last one but the difference is that
    # Last one display just one orders that is for customer is login now but this method
    # Display all orders that we have in list_orders for admin
    def display_orders_and_receipt_for_admin(cls):
        if len(cls.orders) > 0:
            for order in cls.orders:
                print(order.username_that_is_order, " -- ", order.item.name, "Price:",  order.item.price)

        else:
            print("Now we don't have any order")

    @classmethod
    @representing
    # This first display the orders that are in list_orders
    # Then set the order that admin want and remove if from list_orders
    def confirmation_the_orders(cls):
        deepcopy_orders = copy.deepcopy(cls.orders)
        progress = True
        print("Please enter username of user that you want to confirm his orders")
        while progress:
            Order.display_orders_and_receipt_for_admin()
            username_for_confirmation = input(": ")
            condition_of_confirmation = False
            for repeat in deepcopy_orders:
                for order in cls.orders:
                    if order.username_that_is_order == username_for_confirmation:
                        cls.orders.remove(order)

            if condition_of_confirmation:
                print("Confirmation was successful")

            else:
                print("Username not found")

            if username_for_confirmation == "q":
                progress = False

