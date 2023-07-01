from calculate_each_row_2 import calculate_each_row


def pascal_triangle():
    # First in here I get the number of row that user want
    print("Please type number of row that you want to see.")
    print("If it's finish type q")
    input_number_row = input(": ")
    while_response = True  # This is my while manager and I manage it in the end of function
    while while_response:
        calculate_each_row(input_number_row)

        input_number_row = input(": ")
        if input_number_row == "q":
            while_response = False


if __name__ == "__main__":
    pascal_triangle()

else:
    print("You must run this program in main file")

