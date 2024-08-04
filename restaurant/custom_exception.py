class LengthError(Exception):
    def __init__(self, massage):
        self.massage = massage

    def show_massage(self):
        print(f'{self.massage}')


class OutOfStockError(Exception):
    def __init__(self, massage):
        self.massage = massage

    def show_massage(self):
        print(f'{self.massage}')


class DisposableDiscountError(Exception):
    def __init__(self, massage):
        self.massage = massage

    def show_massage(self):
        print(f'{self.massage}')


class StartDateDiscountError(Exception):
    def __init__(self, massage):
        self.massage = massage

    def show_massage(self):
        print(f'{self.massage}')


class ExpireDateDiscountError(Exception):
    def __init__(self, massage):
        self.massage = massage

    def show_massage(self):
        print(f'{self.massage}')


class UsageLimitationDiscountError(Exception):
    def __init__(self, massage):
        self.massage = massage

    def show_massage(self):
        print(f'{self.massage}')


class UsedDiscountError(Exception):
    def __init__(self, massage):
        self.massage = massage

    def show_massage(self):
        print(f'{self.massage}')

