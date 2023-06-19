from custom_exception import SpaseERROR
from four_main_math_operation import calculate_math_operation


def run_math_operation_and_check_Error():
    # This part is for checking custom ERROR

    answer_math = calculate_math_operation()  # This answer_math it's not that one you saw in
    # (file = four_main_math_operation) actually we move that one to here by return.
    while answer_math != "q":
        try:

            if type(answer_math) != int and type(answer_math) != float and answer_math != "q":
                raise SpaseERROR("")

            else:
                print(answer_math)

        except SpaseERROR:
            print("SpaseERROR: please add correctly form of spase and just type math operation."
                  "\nExample: 2 + 3 * 1\n")

        except ValueError:
            print("ValueError: please just type number")

        except IndexError:
            print("IndexError: You type just one character and it don't hase any number.")

        answer_math = calculate_math_operation()


def calculator():
    run_math_operation_and_check_Error()
