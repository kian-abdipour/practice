import random


class Order:
    def __init__(self, order_id=None, order_car=None, order_retailer=None, order_creation_time=None):
        self.order_id = order_id
        self.order_car = order_car
        self.order_retailer = order_retailer
        self.order_creation_time = order_creation_time

    def generate_order_id(self, car_code):
        characters = "abcdefghijklmnopqrstuvwxyz"

        order_id = random.choice(characters)
        while len(order_id) != 6:
            if (len(order_id)+1) % 2 == 0:
                order_id += (random.choice(characters)).upper()

            else:
                order_id += (random.choice(characters)).lower()

        characters_index = []
        str_1 = "~!@#$%^&*"
        for character in order_id:
            characters_index.append((ord(character) ** 2) % len(str_1))

        for index_character in characters_index:
            for repeat in range(0, characters_index.index(index_character)):
                order_id += str_1[index_character]

        order_id += car_code + str(self.order_creation_time)

        return order_id

    def __str__(self):
        return (f"{self.order_id},"
                f" {self.order_car.car_code},"
                f" {self.order_retailer.retailer_id},"
                f" {self.order_creation_time}")

