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
def calculate_fibonacci_Numbers(number_fibonacci, numbers, counter):
    if number_fibonacci == 0 or number_fibonacci == 1 or number_fibonacci == 2:
        return "finish"

    else:
        first_number = numbers[-1]
        second_number = numbers[-2]
        new_number = first_number + second_number
        numbers.append(new_number)
        counter += 1
        print(counter, " _ ",  new_number)
        return calculate_fibonacci_Numbers(number_fibonacci - 1, numbers, counter)


def main():
    progress = True
    while progress:
        number_fibonacci = get_number_fibonacci()
        print(1, " _ ", 0)
        print(2, " _ ", 1)
        print(calculate_fibonacci_Numbers(number_fibonacci, [0, 1], 2))

        if number_fibonacci == "q":
            progress = False


if __name__ == "__main__":
    main()

else:
    print("You must run this program in main file")

