from car_retailer import CarRetailer
from car import Car
from retailer import Retailer
import random
import datetime


def generate_test_data():
    with open("stock.txt", "a+") as file:
        read_file = file.readlines()

    with open("stock.txt", "r") as check_file:
        number_line = len(check_file.readlines())

    if number_line == 0:
        name_retailers = ["Exclusive Cars", "King Motor", "Racy Motors"]
        car_retailer_addresses = ["Clayton Rd Clayton, VIC3100", "Clayton Rd Clayton, VIC3170", "Clayton Rd Mount Waverley, VIC3168"]
        car_retailer_business_hours = [(10, 18), (6.5, 12), (14, 17.5)]
        for name_retailer in name_retailers:
            car_a = Car("PX101073", "BMW z4", 2, 205, 2470, "FWD")
            car_b = Car("QZ278951", "BMW X8", 5, 190, 1930, "RWD")
            car_c = Car("HP701271", "Mercedes-Benz G-Class", 5, 410, 2113, "AWD")
            car_d = Car("GN448578", "toyota supra mk5", 2, 335, 1420, "RWD")
            car_e = Car("UX761456", "Rolls-Royce Phantom", 5, 536, 2745, "AWD")
            car_f = Car("GD356859", "Honda Civic", 4, 180, 1268, "FWD")
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

            with open("stock.txt", "a+") as file:
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
            if car_line != ["is not available"]:
                car = Car(car_line[0], car_line[1], int(car_line[2]), int(car_line[3]), int(car_line[4]), car_line[5])
                car_retailer.car_retailer_stock.append(car)
        retailers.append(car_retailer)

    return retailers


def main_menu():
    generate_test_data()
    print("! Welcome to our car purchase advis system !")
    proceed = True
    while proceed:
        list_retailers = main()
        print("a) Look for the nearest car retailer\nb) Get car purchase advice\nc) Place a car order\nd) Exit")
        user_operation = input(": ")

        if user_operation == "a":
            condition_form_code_post = True
            try:
                print("Enter your code post")
                user_code_post = int(input(": "))

            except ValueError:
                condition_form_code_post = False
                print("postcode should be a number without space")

            if condition_form_code_post:
                list_distance = []
                for car_retailer in list_retailers:
                    list_distance.append(car_retailer.get_post_code_distance(user_code_post))

                print("Name:", list_retailers[list_distance.index(min(list_distance))].retailer_name,
                      "Address:", list_retailers[list_distance.index(min(list_distance))].car_retailer_address)

        elif user_operation == "b":
            print("i) Recommend a car\nii) Get all cars in stock\n"
                  "iii) Get cars in stock by car types\niv) Get probationary licence permitted cars in stock")
            operation_user_part_b = input(": ")

            if operation_user_part_b == "i":
                for retailer in list_retailers:
                    recommended_car = retailer.car_recommendation()
                    print("Retailer_name:", retailer.retailer_name, "retailer_id:", retailer.retailer_id,
                          " >>> car_name:", recommended_car.car_name, "car_id:", recommended_car.car_code)

            elif operation_user_part_b == "ii":
                for retailer in list_retailers:
                    for car in retailer.get_all_stock():
                        print("retailer id:", retailer.retailer_id, ", name retailer:", retailer.retailer_name,
                              " >>> ", "car_name:", car.car_name, ", code:", car.car_code, ", type:", car.car_type)

            elif operation_user_part_b == "iii":
                for retailer in list_retailers:
                    car_retailer_stock_by_type = retailer.get_stock_by_car_type(["AWD", "RWD"])
                    for car in car_retailer_stock_by_type:
                        print("retailer id:", retailer.retailer_id, ", name retailer:", retailer.retailer_name,
                              " >>> ", car.car_name, ", code:", car.car_code, ", type:", car.car_type)

            elif operation_user_part_b == "iv":
                for retailer in list_retailers:
                    for car in retailer.car_retailer_stock:
                        if car.probationary_licence_prohibited_vehicle():
                            print(f"Retailer name: {retailer.retailer_name}, retailer id: {retailer.retailer_id}"
                                  f" >>> car name: {car.car_name}, car code: {car.car_code}")

            else:
                print("Operation not found")

        elif user_operation == "c":
            print("Please enter a car_id and retailer_id like:BM123456 12345678")
            information_car = input(": ").split(" ")

            condition_form_ides = True
            if len(information_car) == 2:
                try:
                    number_retailer_id = int(information_car[1])

                except ValueError:
                    condition_form_ides = False
                    print("Please enter information ides like this:BM123456 12345678")

            else:
                condition_form_ides = False
                print("Please enter information ides like this:BM123456 12345678")

            if condition_form_ides:
                condition_order = False
                for retailer in list_retailers:
                    if retailer.retailer_id == number_retailer_id:
                        if retailer.is_operating(retailer.car_retailer_business_hours):
                            order = retailer.create_order(information_car[0])

                            with open("order.txt", "a+") as file_order:
                                file_order.write(str(order) + "\n")

                            for retailer_item in list_retailers:
                                str_cars = []
                                for car in retailer_item.car_retailer_stock:
                                    str_cars.append(str(car))

                                retailer_item.car_retailer_stock = str_cars

                            with open("stock.txt", "w") as file_stock:
                                for new_retailer in list_retailers:
                                    file_stock.write(str(new_retailer) + "\n")

                            condition_order = True

                        else:
                            print(f"{retailer.retailer_name}: you should place a order in cur time " 
                                  f"{retailer.car_retailer_business_hours[0]}AM to "
                                  f"{retailer.car_retailer_business_hours[1]}PM")

                if condition_order:
                    print(f"Your order was successful \n"
                          f"time: {datetime.datetime.fromtimestamp(order.order_creation_time)} \n"
                          f"order_id: {order.order_id}")

                else:
                    print("Order was fail: retailer or car not found")

        elif user_operation == "d":
            proceed = False

        else:
            print("Operation not found")


if __name__ == "__main__":
    main_menu()

else:
    print("This function should run in main file")

