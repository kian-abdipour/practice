class LengthError(Exception):
    def __init__(self, massage):
        self.massage = massage

    def show_massage(self):
        print(f'{self.massage}')



