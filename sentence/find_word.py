from custom_exseption import NoSentence


# This function get sentence and make a list of word that are in sentence.
def make_list_word():
    print("Please type a sentence.")
    input_sentence = input(": ")
    list_word = input_sentence.split(" ")
    return list_word


# This function get the word and check it is in sentence or not.
def get_and_find_word(list_word):
    print("\nOk, type word that you want.")
    input_word = input(": ")

    if (input_word.lower() in list_word) or (input_word.upper() in list_word):
        print("\nYes! i found this word.\n")

    else:
        print("\nOh! i couldn't found this word.\n")

    return list_word


# This function run the program and check the error
def run_and_check_error():
    list_word = []
    print("If it's finish type (q).")
    while_manager = True
    while while_manager:
        if len(list_word) == 1:
            raise NoSentence("\nNoSentence_Error: You should type sentence not word.\n")

        list_word = get_and_find_word(make_list_word())

        # This part is our while manager checker
        if list_word == ["q"]:
            while_manager = False

        else:
            while_manager = True


if __name__ == "__main__":
    run_and_check_error()

else:
    print("You should run this function in main file")
