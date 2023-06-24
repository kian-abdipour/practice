# This is the list of 10 last letters of alphabet
list_last_10_letters = ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# This function it's very clear first check we have 4 letters or not
# Then check that the fourth letter is in the list_last_10_letters or not
def check_letter_4():
    print("If it's finish type -1")
    while_manager = True
    while while_manager:
        print("Please type something:")
        input_str = input(": ")
        if len(input_str) >= 4 and input_str[3].lower() in list_last_10_letters:
            print(input_str[3])

        else:
            pass

        # This part is our while manager checker
        if input_str == "-1":
            while_manager = False

        else:
            while_manager = True


if __name__ == "__main__":
    check_letter_4()

else:
    print("Im sorry but it's not a main file.")
