from custom_exception import SpaseERROR
from four_main_math_operation import calculate_math_operation


def run_math_operation_and_check_Error():
    # This is for checking custom ERROR
    try:

        list_character = calculate_math_operation()
        answer_math = list_character[0]

        if type(answer_math) != int and type(answer_math) != float:
            raise SpaseERROR("")

        else:
            print(list_character[0])

    except SpaseERROR:
        print("SpaseERROR: please add correctly form of spase and just type math operation."
              "\nExample: 2 + 3 * 1\n")

    except ValueError:
        print("ValueError: please just type number")

    except IndexError:
        print("IndexError: You type just one character and it don't hase any number.")


def calculator():
    run_math_operation_and_check_Error()


calculator()
