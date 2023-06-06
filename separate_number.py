list_integers = []


# This function first check if item is digit then
# put the item in list_integers.
def make_list_integers():
    print("Please type somthing")
    my_string = input(": ")
    for item in my_string:
        if item.isdigit():
            number = list(my_string).pop(list(my_string).index(item))
            list_integers.append(int(number))
        else:
            continue
    list_integers.sort()


make_list_integers()


# This function first check we have 3 item or not then make it non-repetitive.
def make_list_non_repetitive():
    if len(list_integers) > 3:
        list_integer = set(list_integers)  # This is for make list non-repetitive
        list_integer = list(list_integer)  # Again make list because we need list
        print(list_integer)
    else:
        list_integers.clear()


make_list_non_repetitive()
