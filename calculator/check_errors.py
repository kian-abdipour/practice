from custom_exception import SpaseERROR
from four_main_math_operation import calculate_math_operation
from four_main_math_operation import new_list_main_character
from make_list_main_character import list_main_character


def run_math_operation_and_check_Error():

    # This part is for checking custom ERROR
    while_manager_calculator = True
    while while_manager_calculator:

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

        if list_answer_math[0] == "q":
            while_manager_calculator = False

        else:
            while_manager_calculator = True


def calculator():
    run_math_operation_and_check_Error()
