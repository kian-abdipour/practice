from retailer import Retailer


class CarRetailer(Retailer):
    def __init__(self, retailer_id=None, retailer_name=None,
                 car_retailer_address=None, car_retailer_business_hours=None):
        self.car_retailer_address = car_retailer_address
        self.car_retailer_business_hours = car_retailer_business_hours
        self.car_retailer_stock = []

        super().__init__(retailer_id, retailer_name)

    def load_current_stock(self, path):
        pass

    def is_operating(self, cur_hour):
        pass

    def __str__(self):
        return (f"{self.retailer_id}, "
                f"{self.retailer_name}, "
                f"{self.car_retailer_address}, "
                f"{self.car_retailer_business_hours}, "
                f"{self.car_retailer_stock}")
