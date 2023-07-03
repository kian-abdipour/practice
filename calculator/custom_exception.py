class SpaseERROR(Exception):
    def __init__(self, result):
        self.result = result


class OnSupportedMathOperation(Exception):
    def __init__(self, result):
        self.result = result
