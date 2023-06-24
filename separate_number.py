list_integers = []
list_str = []


# This function first check if item is digit then
# put the item in list_integers.
def make_list_integers():
    input_string = input(": ")
    for item in input_string:
        if item.isdigit():
            number = list(input_string).pop(list(input_string).index(item))
            list_integers.append(int(number))

        else:
            list_str.append(item)
    list_integers.sort()


# This function first check we have 3 item or not then make it non-repetitive.
def make_list_non_repetitive():
    if len(list_integers) > 3:
        list_integer = set(list_integers)  # This is for make list non-repetitive
        list_integer = list(list_integer)  # Again make list because we need list
        print(list_integer)

    else:
        list_integers.clear()


def main():
    while_manager = True
    while while_manager:
        make_list_integers()
        make_list_non_repetitive()

        if list_str == ["q"]:
            while_manager = False

        else:
            while_manager = True

        list_str.clear()
        list_integers.clear()


if __name__ == "__main__":
    main()

else:
    print("You should run this program in main file.")
