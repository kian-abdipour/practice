from calculate_each_row_2 import calculate_each_row


def pascal_triangle():
    # First in here I get the number of row that user want
    print("Please type number of row that you want to see.")
    print("If it's finish type q")
    input_number_row = input(": ")
    print("Before show you the pascal triangle choose and type messi or ronaldo")
    input_messi_or_ronaldo = input(": ")
    while_response = True
    while while_response:
        try:

            if input_number_row != "q":
                int_input_number_row = int(input_number_row)

            else:
                break

        except ValueError:
            return print("You should type just natural number not", "(" + input_number_row + ")")

        try:
            if input_messi_or_ronaldo != "messi" and input_messi_or_ronaldo != "ronaldo":
                int_input_messi_or_ronaldo = int(input_messi_or_ronaldo)
                str_inpt_messi_or_ronaldo = str(input_messi_or_ronaldo)

        except ValueError:
            return print("ValueError: You should choose and type messi or ronaldo")

        calculate_each_row(input_number_row)

        input_number_row = input(": ")
        if input_number_row == "q":
            while_response = False


if __name__ == "__main__":
    pascal_triangle()

else:
    print("You must run this program in main file")

