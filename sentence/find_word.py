from custom_exseption import NoSentence


# This function get sentence and make a list of word that are in sentence.
def get_sentence():
    global list_word
    print("Please type a sentence.")
    input_sentence = input(": ")
    list_word = input_sentence.split(" ")
    return list_word


# This function get the word and check it is in sentence or not.
def get_and_find_word():
    global list_word
    print("If it's finish type (q).")
    list_word = get_sentence()
    while list_word != ["q"]:
        print("\nOk, type word that you want.")
        input_word = input(": ")

        if input_word == "q":
            break

        if input_word in list_word:
            print("\nYes! i found this word.\n")

        else:
            print("\nOh! i couldn't found this word.\n")

        list_word = get_sentence()


# This function run the program and check the error
def check_error():
    global list_word
    list_word = "True"
    while list_word != ["q"]:
        try:

            get_and_find_word()
            if len(list_word) == 1 and list_word != ["q"]:
                raise NoSentence("")

            else:
                pass

        except NoSentence:
            print("\nNoSentence_Error: You should type sentence not word.\n")


if __name__ == "__main__":
    get_and_find_word()

else:
    print("You should run this function in main file")
