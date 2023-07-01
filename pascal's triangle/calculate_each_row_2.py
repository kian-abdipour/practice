# This function is clear but if you can't understand you cana read comment that you will see
def calculate_each_row(input_number_row):
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

    while number_row != int(input_number_row):

        # In this part I use enumerate because get repetitious index of item
        enumerate_list_main_character = list(enumerate(list_main_character))

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

        list_main_character = list_new_characters
        print(list_new_characters)

