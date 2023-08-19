# This is a decorator that before call a function that calculate fibonacci number print 0 and 1
def print_zero_and_one(func):
    def inner(num):
        print(0)
        print(1)
        value = func(num)

        return value

    return inner


@print_zero_and_one
def my_generator(num):
    first_number = 0
    second_number = 1

    while num != 2:
        new_number = first_number + second_number
        yield new_number
        first_number = second_number
        second_number = new_number
        num -= 1


for fibonacci_number in my_generator(10):
    print(fibonacci_number)

