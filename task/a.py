progress = True
while progress:
    with open("stock.txt", "r") as stock_file:
        read_file = stock_file.readlines()

    retailer_lines = []
    for line in read_file:
        retailer_information = line[0: line.index("[") - 2].split(",")
        car_lines = line[line.index("[") + 2: -2].split("', '")
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

