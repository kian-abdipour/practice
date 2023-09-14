from retailer import Retailer
from order import Order
from datetime import datetime
import random
import time


class CarRetailer(Retailer):
    def __init__(self, retailer_id=None, retailer_name=None,
                 car_retailer_address=None, car_retailer_business_hours=None):
        self.car_retailer_address = car_retailer_address
        self.car_retailer_business_hours = car_retailer_business_hours
        self.car_retailer_stock = []

        super().__init__(retailer_id, retailer_name)

    def load_current_stock(self, path):
        pass

    @staticmethod
    def is_operating(cur_hour):
        time_now = float(str(datetime.now().hour) + "." + str(datetime.now().minute))
        if cur_hour[0] < time_now < cur_hour[1]:
            return True

        else:
            return False

    def get_all_stock(self):
        return self.car_retailer_stock

    def get_post_code_distance(self, post_code):
        post_code_car_retailer = ''
        for character in self.car_retailer_address:
            if character.isdigit():
                post_code_car_retailer += character
        number_post_code = int(post_code_car_retailer)

        if post_code > number_post_code:
            return post_code - number_post_code

        else:
            return number_post_code - post_code

    def remove_from_stock(self, car_code):
        for car in self.car_retailer_stock:
            if car.car_code == car_code:
                self.car_retailer_stock[self.car_retailer_stock.index(car)] = "is not available"
                return True

        return False

    def add_to_stock(self, car):
        condition_duplicated = False
        for car_item in self.car_retailer_stock:
            if car_item.car_code == car.car_code:
                condition_duplicated = True

        if not condition_duplicated:
            self.car_retailer_stock.append(car)
            return True

        else:
            return False

    def car_recommendation(self):
        return random.choice(self.car_retailer_stock)

    def create_order(self, car_code):
        if self.is_operating(self.car_retailer_business_hours):
            car_retailer = CarRetailer(self.retailer_id, self.retailer_name,
                                       self.car_retailer_address, self.car_retailer_business_hours)

            for car in self.car_retailer_stock:
                if car.car_code == car_code:
                    if self.remove_from_stock(car_code):
                        order = Order(-1, car, car_retailer, time.time())
                        order.order_id = order.generate_order_id(car_code)
                        return order

    def get_stock_by_car_type(self, car_types):
        car_retailer_stock_by_type = []
        for car in self.car_retailer_stock:
            if car.car_type in car_types:
                car_retailer_stock_by_type.append(car)

        return car_retailer_stock_by_type

    def __str__(self):
        return (f"{self.retailer_id}, "
                f"{self.retailer_name}, "
                f"{self.car_retailer_address}, "
                f"{self.car_retailer_business_hours}, "
                f"{self.car_retailer_stock}")

