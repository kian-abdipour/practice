def get_number_fibonacci():
    print("Enter number of fibonacci number that you want see")
    try:
        number_fibonacci = int(input(": "))

    except ValueError:
        return print("ValueError: You should type number")

    if number_fibonacci <= 0:
        return print("You should type positive number")

    return number_fibonacci


# Recursion
def calculate_fibonacci_Numbers(number_fibonacci, numbers):
    if number_fibonacci == 1 or number_fibonacci == 2:
        return

    else:
        first_number = numbers[-1]
        second_number = numbers[-2]
        new_number = first_number + second_number
        numbers.append(new_number)
        calculate_fibonacci_Numbers(number_fibonacci - 1, numbers)
        print(new_number)
        return new_number


def main():
    progress = True
    while progress:
        number_fibonacci = get_number_fibonacci()
        print(calculate_fibonacci_Numbers(number_fibonacci, [0, 1]))
        print(0)

        if number_fibonacci == "q":
            progress = False


if __name__ == "__main__":
    main()

else:
    print("You must run this program in main file")

