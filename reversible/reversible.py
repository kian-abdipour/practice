def get_string():
    print("Enter something")
    string = input(": ")
    return string


def check_reversible(string):
    list_strings = list(string)
    list_strings.reverse()
    string_2 = ""
    for character in list_strings:
        string_2 += character

    print(string == string_2)


if __name__ == "__main__":
    check_reversible(get_string())

else:
    print("You must run this program in main file")

