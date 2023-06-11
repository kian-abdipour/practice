class SpaseERROR(Exception):
    def __init__(self, answer):
        self.answer = answer
