from custom_exception import SpaseERROR
from four_main_math_operation import calculate_math_operation
from four_main_math_operation import new_list_main_character


def run_math_operation_and_check_Error():

    # This part is for checking custom ERROR
    list_answer_math = ["True"]
    while list_answer_math[0] != "q":

        try:

            new_list_main_character()
            list_answer_math = calculate_math_operation()

            if type(list_answer_math[0]) != int and type(list_answer_math[0]) != float and list_answer_math[0] != "q":
                raise SpaseERROR("")

            else:
                print(list_answer_math[0])

        except SpaseERROR:
            print("\nSpaseERROR: please add correctly form of spase and just type math operation.\n"
                  "Example: 2 + 3 * 1\n")

        # This part is for checking built in ERROR
        except ValueError:
            print("\nValueError: please just type number.\n")

        except IndexError:
            print("\nIndexError: You type just one character and it don't hase any number.\n")


def calculator():
    run_math_operation_and_check_Error()
