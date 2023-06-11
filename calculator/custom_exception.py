from calculator import calculator


class SpaseERROR(Exception):
    def __init__(self, answer):
        self.answer = answer


def make_spase_error():
    try:
        answer = calculator()
        if type(answer) != int and type(answer) != float:
            raise SpaseERROR("")
        else:
            print("There is no problem !")
    except SpaseERROR:
        print("SpaseERROR: please add correctly form of spase and just type math operation\nExample: 2 + 3 * 1")

    except ValueError:
        print("ValueError: please just type number")

