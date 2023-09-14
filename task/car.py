class Car:
    def __init__(self, car_code=None, car_name=None,
                 car_capacity=None, car_horsepower=None,
                 car_weight=None, car_type=None):

        self.car_code = car_code
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = car_type

    def probationary_licence_prohibited_vehicle(self):
        power_car = self.car_horsepower / 1.341
        kilowatt_car = (power_car / self.car_weight) * 1000
        if kilowatt_car > 130:
            return False

        else:
            return True

    def get_car_type(self):
        return self.car_type

    def found_matching_car(self, car_code):
        if car_code == self.car_code:
            return True

        else:
            return False

    def __str__(self):
        return (f"{self.car_code}, {self.car_name}, "
                f"{self.car_capacity}, {self.car_horsepower}, "
                f"{self.car_weight}, {self.car_type}")


