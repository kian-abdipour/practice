from car_retailer import CarRetailer
from car import Car
from retailer import Retailer
import random
import datetime


def generate_test_data():
    with open("stock.txt", "a+") as file:
        read_file = file.readlines()

    name_retailers = ["ULTnkYQ QN", "asTgslrLl", "eiTyElGZTv"]
    car_retailer_addresses = ["Clayton Rd Clayton, VIC3170", "Clayton Rd Clayton, VIC3170", "Clayton Rd Mount Waverley, VIC3168"]
    car_retailer_business_hours = [(10.9, 14.5), (8.4, 16.9), (11.9, 12.3)]
    for name_retailer in name_retailers:
        car_a = Car("PX101073", "jEJPRJ qNTOlvhmWpw", 17, 212, 2210, "FWD")
        car_b = Car("QZ278951", "KnifVWGlnEvsudbG", 11, 155, 1751, "AWD")
        car_c = Car("HP701271", "hqVm QRxZJMhhB", 19, 213, 1180, "AWD")
        car_d = Car("GN448578", "GiblDmqvZLrPmLQJAmsW", 5, 176, 2450, "RWD")
        car_e = Car("UX761456", "WSTzkGuigTuKgXzVNG", 14, 210, 2150, "FWD")
        car_f = Car("GD356859", "OGrenAEllf tJH", 6, 230, "FWD")
        cars = [car_a, car_b, car_c, car_d, car_e, car_f]

        retailer = Retailer(-1, name_retailer)
        retailer.generate_retailer_id(read_file)

        address = car_retailer_addresses[name_retailers.index(name_retailer)]
        business_hours = car_retailer_business_hours[name_retailers.index(name_retailer)]
        car_retailer = CarRetailer(retailer.retailer_id, retailer.retailer_name, address, business_hours)
        while len(car_retailer.car_retailer_stock) != 4:
            car = random.choice(cars)
            is_duplicated_car = False
            for item_car in car_retailer.car_retailer_stock:
                if car.car_code in item_car:
                    is_duplicated_car = True

            if not is_duplicated_car:
                car_retailer.car_retailer_stock.append(str(car))

        with open("stock.txt", "a") as file:
            file.write(str(car_retailer)+"\n")


def main():
    progress = True
    while progress:
        with open("stock.txt", "r") as stock_file:
            read_file = stock_file.readlines()

        retailer_lines = []
        for line in read_file:
            retailer_information = line[0: line.index("[")-2].split(",")
            car_lines = line[line.index("[")+2: -2].split("', '")
            for car_line in car_lines:
                car_lines[car_lines.index(car_line)] = car_line.split(", ")
            retailer_information.append(car_lines)
            retailer_lines.append(retailer_information)

        retailers = []
        for line in retailer_lines:
            str_business_hours = line[4] + line[5]
            business_hours = tuple(((str_business_hours.replace(" (", "")).replace(")", "")).split(" "))
            if "'" in business_hours[0] and "'" in business_hours[1]:
                list_business_hours = list(business_hours)
                list_business_hours[0] = business_hours[0].replace("'", "")
                list_business_hours[1] = business_hours[1].replace("'", "")
                business_hours = tuple(list_business_hours)

            car_retailer = CarRetailer(int(line[0]), line[1], line[2] + ", " + line[3], business_hours)
            for car_line in line[6]:
                if len(car_line) >= 5:
                    if "'" in car_line[5]:
                        car_line[5] = car_line[5].replace("'", "")
                    car = Car(car_line[0], car_line[1], int(car_line[2]), int(car_line[3]), int(car_line[4]), car_line[5])
                    car_retailer.car_retailer_stock.append(car)
            retailers.append(car_retailer)

