from calculate_each_row_2 import calculate_each_row


def pascal_triangle():
    # First in here I get the number of row that user want
    print("Please type number of row that you want to see.")
    print("If it's finish type q")
    input_number_row = input(": ")

    print("Before show you the pascal triangle choose and type messi or ronaldo")
    input_messi_or_ronaldo = input(": ")

    print("If you're sour about {messi_or_ronaldo} type ok else type no".format(messi_or_ronaldo=input_messi_or_ronaldo)
          )
    input_ok_or_no = input(": ")

    while_response = True
    while while_response:
        if input_number_row != "q":

            try:
                int_input_number_row = int(input_number_row)

            except ValueError:
                return print("You should type just natural number not", "(" + input_number_row + ")")

        else:
            break

        try:
            if input_messi_or_ronaldo != "messi" and input_messi_or_ronaldo != "ronaldo":
                raise ValueError

        except ValueError:
            return print("ValueError: You should choose and type messi or ronaldo not ({messi_ronaldo})".
                         format(messi_ronaldo=input_messi_or_ronaldo))

        try:
            if input_ok_or_no != "ok" and input_ok_or_no != "no":
                raise ValueError

        except ValueError:
            return print("ValueError: you should type ok or no not ({ok_or_no})".format(ok_or_no=input_ok_or_no))

        calculate_each_row(input_number_row)

        input_number_row = input(": ")
        if input_number_row == "q":
            while_response = False


if __name__ == "__main__":
    pascal_triangle()

else:
    print("You must run this program in main file")

