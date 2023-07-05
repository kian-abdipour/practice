list_integer = []
list_consecutive = []


# In here first we separate our integer and append it to list_integer then append the consecutive number to
# list_consecutive and if we have 4 or more number in consecutive print our list none-repetitive.
def make_list_integer():
    print("If it's finish type q")
    while_manager = True
    while while_manager:
        print('Please type something.')
        input_character = input(": ")
        my_string = input_character + "A"
        for item in my_string:
            if item.isdigit():
                list_integer.append(int(item))

        for item_2 in my_string:
            if item_2.isdigit():

                if my_string[my_string.index(item_2) + 1].isdigit():
                    list_consecutive.append(item_2)

                else:
                    list_consecutive.append(item_2)
                    break

        if len(list_consecutive) > 3:
            set_integers = set(list_integer)  # This is for make our list none-repetitive
            list_main_integers = list(set_integers)  # Again we make list because we need list
            print(list_main_integers)

        # This part is our while manager checker
        if input_character == "q":
            while_manager = False

        else:
            while_manager = True


if __name__ == "__main__":
    make_list_integer()

else:
    print("I'm sorry but it's not a main file")
