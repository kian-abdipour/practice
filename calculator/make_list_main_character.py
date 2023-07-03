from custom_exception import SpaseERROR
from custom_exception import OnSupportedMathOperation


# In here we separate our number and math operation by space and insert to list integer.
def make_list_character():
    print("Please between any number and math operation add (space)\nIf it's finish type (q) to exist.")
    input_1 = input(": ")
    list_character = input_1.split(" ")
    try:
        if len(list_character) <= 1 and list_character[0] != "q":
            raise SpaseERROR("")

    except SpaseERROR:
        return print("\nSpaseError: You type something with out any space you should type a math operation with apace"
                     " like this:"" 2 + 4\n")

    try:
        for item in list_character:
            if item == "+" or item == "-" or item == "*" or item == "/" or item == "**" or item == "%" or item == "q":
                continue

            else:
                float_item = float(item)

    except ValueError:
        return print("\nValueError: you must type just number not letters or something else\n")

    try:
        if ("**" in list_character) or ("%" in list_character):
            raise OnSupportedMathOperation("")

    except OnSupportedMathOperation:
        return print("OnSupportedMathOperation: Im sorry but this program just have 4 math operation and doesn't "
                     "support ** and %")

    return list_character


print("Tip: when you enter somthing for first time it doesn't work, "
      "after that you can us calculator without any problem. This will be ok in the next update.")
list_main_character = make_list_character()  # This is our main list because we can't import variable from function.
