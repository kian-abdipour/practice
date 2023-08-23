import json
from item import Item
from customer import Customer


class Order:
    def __init__(self, username_that_is_order=None, item=None):
        self.username_that_is_order = username_that_is_order
        self.item = item

    @staticmethod
    # This method first display menu then get the number of food that customer want to order
    # Then add this food to list_customer that are in list_information_login_customer
    def order_item():
        with open("order_datas.json", "r") as order_file:
            load_data_order = json.load(order_file)

        with open("category_datas.json", "r") as category_file:
            load_data_category = json.load(category_file)

        number_category = Item.display_items()
        try:
            number_item = int(input(": "))

        except ValueError:
            return print("ValueError: you should type just number")

        selected_item = load_data_category["categories"][number_category-1]["list_items"][number_item-1]
        data = {
            "username_that_is_order": Customer.username_that_is_login,
            "item": selected_item
        }
        load_data_order["orders"].append(data)

        with open("order_datas.json", "w") as order_file:
            json.dump(load_data_order, order_file)

        return print("Order was successful")

    @staticmethod
    # This method display order of account that is login and show the total fee of order
    def display_orders_and_receipt_for_customer():
        with open("order_datas.json", "r") as order_file:
            load_data = json.load(order_file)

        total = 0
        counter = 0
        for order in load_data["orders"]:
            if order["username_that_is_order"] == Customer.username_that_is_login:
                counter += 1
                total += order["item"]["price"]
                print(counter, " -- ", order["item"]["name"], "price:", order["item"]["price"])

        print("total:", total)

    @staticmethod
    # This method is like last one but the difference is that
    # Last one display just one orders that is for customer is login now but this method
    # Display all orders that we have in list_orders for admin
    def display_orders_and_receipt_for_admin():
        with open("order_datas.json", "r") as order_file:
            load_data = json.load(order_file)

        if len(load_data["orders"]) == 0:
            return print("Now we don't have any order")

        for order in load_data["orders"]:
            print(order["username_that_is_order"], " -- ", order["item"]["name"], "price: ", order["item"]["price"])

    @staticmethod
    # This first display the orders that are in list_orders
    # Then set the order that admin want and remove if from list_orders
    def confirmation_the_orders():
        progress = True
        while progress:
            with open("order_datas.json") as order_file:
                data_load = json.load(order_file)

            Order.display_orders_and_receipt_for_admin()
            print("Enter a username to confirm his orders")
            username_to_confirmation = input(": ")

            condition_confirm = False
            for order in list(data_load["orders"]):
                if order["username_that_is_order"] == username_to_confirmation:
                    data_load["orders"].remove(order)
                    condition_confirm = True

            if condition_confirm:
                print("Confirmation was successful")

            else:
                print("Username not found")

            with open("order_datas.json", "w") as order_file:
                json.dump(data_load, order_file)

            if username_to_confirmation == "q":
                progress = False

