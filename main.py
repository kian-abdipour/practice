class Person:
    def __new__(cls, *args, **kwargs):
        print("Instance is creation")
        instance = super().__new__(cls)
        return instance

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"first name = {self.first_name} \nlast name = {self.last_name}"

    def __repr__(self):
        return "Class: Person"

    def __eq__(self, other):
        if self.first_name == other.first_name and self.last_name == other.last_name:
            return True

        else:
            return False

    def __lt__(self, other):
        return self.age < other

    def __gt__(self, other):
        return self.age > other

    def __ge__(self, other):
        return self.age >= other

    def __le__(self, other):
        return self.age <= other

    def __add__(self, other):
        return Person("kian", "Abdipour", self.age + other.age)

    def __sub__(self, other):
        return Person("Kian", "Abdipour", self.age - other.age)

    def __bool__(self):
        if self.age > 18:
            return True

        else:
            return False

    def __int__(self):
        return int(self.age)

    def __float__(self):
        return float(self.age)

    def __getattr__(self, item):
        return print(item)

    def __del__(self):
        return print("Person destroyed")


hossein = Person("hossein", "Hassani", 15)
ali = Person("Ali", "Hassani", 26)
print(ali.kk)
#jj = hossein - ali
#print(jj)

