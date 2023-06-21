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
    print("If it's finish type (q).")
    list_word = get_sentence()
    print("\nOk, type word that you want.")
    input_word = input(": ")

    # This function made whit lambda and check that we have word in sentence or not.
    find_word = (lambda a:
                 print("\nYes!, i found it") if (a.lower() in list_word) or (input_word.upper() in list_word)
                 else print("\nNo, i couldn't found it"))

    print(find_word(input_word))


def run_and_check_error():
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
    run_and_check_error()

else:
    print("You should")
