def make_number():
    while_manager = True
    while while_manager:
        print("If it's finish type q")
        print("Please enter number of row mosalas khaiam that you want.")
        input_number_row = input(": ")

        if input_number_row.isdigit():
            for item in range(0, int(input_number_row)):
                numbers_row_mosalas_khaiam = 11 ** item
                str_numbers_row_mosalas_khaiam = str(numbers_row_mosalas_khaiam)
                print(str_numbers_row_mosalas_khaiam)

        if input_number_row == "q":
            while_manager = False

        else:
            while_manager = True


if __name__ == "__main__":
    make_number()

else:
    print("You should run this program on main file")
