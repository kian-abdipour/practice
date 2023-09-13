import random


class Retailer:
    def __init__(self, retailer_id=None, retailer_name=None):
        self.retailer_id = retailer_id
        self.retailer_name = retailer_name

    # This method generate a number with 8 characters
    # First append random numbers to characters then make it back to a string and change its type to int because we need
    # integer
    def generate_retailer_id(self, list_retailer):
        characters = []
        while len(characters) != 8:
            characters.append(str(random.randint(0, 9)))

        str_retailer_id = ""
        for character in characters:
            str_retailer_id += character

        is_duplicated = False
        for retailer in list_retailer:
            if retailer.retailer_id == int(str_retailer_id):
                is_duplicated = True

        if not is_duplicated:
            self.retailer_id = int(str_retailer_id)

    # This magic method it's for save data in a file
    def __str__(self):
        return f"{self.retailer_id}, {self.retailer_name}"


a = Retailer()
a.generate_retailer_id("")
print(a.retailer_id)

