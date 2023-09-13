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

    def __str__(self):
        return (f"{self.car_code}, {self.car_name}, "
                f"{self.car_capacity}, {self.car_horsepower}, "
                f"{self.car_weight}, {self.car_type}")


