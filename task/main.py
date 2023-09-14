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
        car_f = Car("GD356859", "OGrenAEllf tJH", 6, 230, 1899, "FWD")
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
    with open("stock.txt", "r") as stock_file:
        read_file = stock_file.readlines()

    retailers_information = []
    for line in read_file:
        retailer_information = line.split(", [")
        retailer_information[0] = retailer_information[0].split(", ")
        retailer_information[1] = retailer_information[1].replace("']\n", "")
        retailer_information[1] = retailer_information[1].split("'")
        retailer_information[1].remove('')
        while ', ' in retailer_information[1]:
            retailer_information[1].remove(', ')
        for car_line in retailer_information[1]:
            retailer_information[1][retailer_information[1].index(car_line)] = car_line.split(", ")
        retailers_information.append(retailer_information)

    retailers = []
    for line in retailers_information:
        str_business_hours = line[0][4].replace("(", "") + " " + line[0][5].replace(")", "")
        business_hours = tuple(str_business_hours.split(" "))
        business_hours = (float(business_hours[0]), float(business_hours[1]))

        car_retailer = CarRetailer(int(line[0][0]), line[0][1], line[0][2] + ", " + line[0][3], business_hours)
        for car_line in line[1]:
            car = Car(car_line[0], car_line[1], int(car_line[2]), int(car_line[3]), int(car_line[4]), car_line[5])
            car_retailer.car_retailer_stock.append(car)
        retailers.append(car_retailer)

    return retailers


generate_test_data()
main()

