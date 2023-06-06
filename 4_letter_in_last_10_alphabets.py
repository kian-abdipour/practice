# This is the list of 10 last letters of alphabet
list_last_10_letters = ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# This function it's very clear first check we have 4 letters or not
# Then check that the fourth letter is in the list_last_10_letters or not
def check_letter_4():
    print("Please type something:")
    string_1 = input(": ")
    if len(string_1) >= 4 and string_1[3].lower() in list_last_10_letters:
        print(string_1[3])

    else:
        pass


if __name__ == "__main__":
    check_letter_4()

else:
    print("Im sorry but it's not a main file.")
