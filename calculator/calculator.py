from custom_exception import SpaseERROR


def calculator():
    print("Please between any number and math operation add (space)\nIf it's finish type (q) to exist.")
    request = input(": ")
    list_character = request.split(" ")
    while request != "q":
        # I in this function we calculate the multiplication and division then separate the answer of them instead of
        # last number.
        # Tip: in math before and after any math operation we have a number like this (2 * 6 - 1)
        def multiplication_and_dvision():
            while '*' in list_character or '/' in list_character:
                for item in list_character:
                    # This is the first part of this function.
                    # In here we define the numbers that are before and after dvision and this is for tip that i sayed
                    # then we divided the number before dvision and number after dvision then
                    # Remove this 3 character and separate answer in list_character.
                    if item == '/':
                        number_before_math_operation = list_character[list_character.index(item) - 1]
                        number_after_math_operation = list_character[list_character.index(item) + 1]

                        result_dvision = float(number_before_math_operation) / float(number_after_math_operation)

                        list_character.insert(list_character.index(item) - 1, result_dvision)
                        list_character.remove(number_before_math_operation)
                        list_character.pop(list_character.index(item))
                        list_character.remove(number_after_math_operation)

                    # This is the second part of this function.
                    # In here work like part 1 but the difference between this two it's the math operation
                    # first one is division the second part is multiplication.
                    elif item == '*':
                        number_before_math_operation = list_character[list_character.index(item) - 1]
                        number_after_math_operation = list_character[list_character.index(item) + 1]

                        result_multiplication = float(number_after_math_operation) * float(number_before_math_operation)

                        list_character.insert(list_character.index(item) - 1, result_multiplication)
                        list_character.remove(number_before_math_operation)
                        list_character.pop(list_character.index(item))
                        list_character.remove(number_after_math_operation)

                    else:
                        continue

        # This function exactly work like last function but in here we calculate total and subtraction
        # Tip: in math before and after any math operation we have a number like this (2 * 6 - 1)
        def total_subtraction():
            while '+' in list_character or '-' in list_character:

                for item in list_character:
                    # This function hase two part and this is first.
                    # First like function one we define after and before number of math operation
                    # Then calculate our phrase and separate answer by last character
                    if item == '+':
                        number_before_math_operation = list_character[list_character.index(item) - 1]
                        number_after_math_operation = list_character[list_character.index(item) + 1]

                        result_total = float(number_before_math_operation) + float(number_after_math_operation)

                        list_character.insert(list_character.index(item) - 1, result_total)
                        list_character.remove(number_before_math_operation)
                        list_character.pop(list_character.index(item))
                        list_character.remove(number_after_math_operation)

                    # this is the second part of function
                    # this part work like last part but the difference is our math operation
                    elif item == '-':
                        number_before_math_operation = list_character[list_character.index(item) - 1]
                        number_after_math_operation = list_character[list_character.index(item) + 1]

                        result_multiplication = float(number_before_math_operation) - float(number_after_math_operation)

                        list_character.insert(list_character.index(item) - 1, result_multiplication)
                        list_character.remove(number_before_math_operation)
                        list_character.pop(list_character.index(item))
                        list_character.remove(number_after_math_operation)

                    else:
                        continue

        # This function has 2 parts
        # This for check built in Error
        def check_Error():
            try:
                multiplication_and_dvision()
                total_subtraction()
            except ValueError:
                print("ValueError: please just type number")

            except IndexError:
                print("you type just {a} and it don't hase any number".format(a=request))

            answer_math = list_character[0]
            if type(answer_math) == int or type(answer_math) == float and len(list_character) == 1:
                print(answer_math)
            # This is for checking custom ERROR
            try:
                if type(answer_math) != int and type(answer_math) != float:
                    raise SpaseERROR("")
                else:
                    pass
            except SpaseERROR:
                print("SpaseERROR: please add correctly form of spase and just type math operation"
                      "\nExample: 2 + 3 * 1\n")

        check_Error()

        answer = list_character[0]
        request = input(": ")
        list_character = request.split(" ")
    return answer

