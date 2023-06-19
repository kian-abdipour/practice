# In here we separate our number and math operation by space and insert to list integer.
def make_list_character():
    print("Please between any number and math operation add (space)\nIf it's finish type (q) to exist.")
    input_1 = input(": ")
    list_character = input_1.split(" ")
    return list_character


print("Tip: when you enter somthing for first time it doesn't work, "
      "after that you can us calculator without any problem. This will be ok in the next update.")
list_main_character = make_list_character()  # This is our main list because we can't import variable from function.
