def calculator():
    print("please between any number and math operation add (space).")
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

                        result_dvision = int(number_before_math_operation) / int(number_after_math_operation)

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

                        result_multiplication = int(number_after_math_operation) * int(number_before_math_operation)

                        list_character.insert(list_character.index(item) - 1, result_multiplication)
                        list_character.remove(number_before_math_operation)
                        list_character.pop(list_character.index(item))
                        list_character.remove(number_after_math_operation)

                    else:
                        continue
        multiplication_and_dvision()

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

                        result_total = int(number_before_math_operation) + int(number_after_math_operation)

                        list_character.insert(list_character.index(item) - 1, result_total)
                        list_character.remove(number_before_math_operation)
                        list_character.pop(list_character.index(item))
                        list_character.remove(number_after_math_operation)

                    # this is the second part of function
                    # this part work like last part but the difference is our math operation
                    elif item == '-':
                        number_before_math_operation = list_character[list_character.index(item) - 1]
                        number_after_math_operation = list_character[list_character.index(item) + 1]

                        result_multiplication = int(number_before_math_operation) - int(number_after_math_operation)

                        list_character.insert(list_character.index(item) - 1, result_multiplication)
                        list_character.remove(number_before_math_operation)
                        list_character.pop(list_character.index(item))
                        list_character.remove(number_after_math_operation)

                    else:
                        continue
        total_subtraction()
        answer_math = list_character[0]
        print(answer_math)
        print("Please between any number and math operation add (space)\nIf there is problem type (q) to check it.")
        request = input(": ")
        list_character = request.split(" ")
    return answer_math

