# This function is clear but if you can't understand you cana read comment that you will see
def pascal_triangle():
    # First in here I get the number of row that user want
    print("Please type number of row that you want to see.")
    print("If it's finish type q")
    input_number_row = input(": ")
    while_response = True  # This is my while manager and I manage it in the end of function
    while while_response:
        # In this part I set the 2 first row as default because it's clear
        if int(input_number_row) == 1:
            print([1])
            return [1]

        elif int(input_number_row) == 2:
            print([1])
            print([1, 1])
            return [1]

        else:
            print([1])
            print([1, 1])

        number_row = 2  # Actually this is my row manager and start from 2 because I set 2 row as default
        list_main_character = [1, 1]

        # In this part I use enumerate because get repetitious index of item
        enumerate_list_main_character = list(enumerate(list_main_character))
        while number_row != int(input_number_row):

            list_new_characters = []

            # In here I pour each row of mosalas khaiam to list and show it to user
            list_new_characters.append(1)
            for item in enumerate_list_main_character[0: len(enumerate_list_main_character) - 1]:
                first_number = item[1]
                second_number = enumerate_list_main_character[enumerate_list_main_character.index(item) + 1][1]
                total_first_and_second_number = first_number + second_number
                list_new_characters.append(total_first_and_second_number)

            list_new_characters.append(1)
            number_row += 1
            print(list_new_characters)

            enumerate_list_main_character = list(enumerate(list_new_characters))

        input_number_row = input(": ")
        if input_number_row == "q":
            while_response = False


if __name__ == "__main__":
    try:
        pascal_triangle()

    except ValueError:
        print("ValueError: You shod just type number not letters or any think else")
else:
    print("Im sorry you should run this program in main file.")

