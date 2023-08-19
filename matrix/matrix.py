import random


def make_list():
    layout_lines = int(input(": "))
    lucky_list = []

    while len(lucky_list) != layout_lines:
        lucky_list.append([])

    for line in lucky_list:
        while len(line) != layout_lines:
            line.append(random.choice([0]))

    return lucky_list


def check_horizontal_line(lines):
    for line in lines:
        enum_lines = list(enumerate(lines))
        for number in enum_lines:

            five_numbers = line[enum_lines.index(number): enum_lines.index(number)+5]
            if five_numbers == [1, 1, 1, 1, 1] or five_numbers == [-1, -1, -1, -1, -1]:
                return True

        return False


def check_vertical_and_slash_line(list_lines):
    for line in list_lines:
        enum_line = list(enumerate(line))

        for number in enum_line:
            counter = 0
            if number[1] != 0:

                for again_line in list_lines:
                    if again_line[enum_line.index(number)] == number[1]:
                        counter += 1
                        if counter == 5:
                            return True

                    else:
                        counter = 0

    return False


def check_slash_lines_from_wright(number_to_be_true, list_lines):
    for line in list_lines:
        enumerate_line = list(enumerate(line))

        for number in enumerate_line:
            count_of_one = 1
            count_of_negative_one = 1

            if number[1] == 1 or number[1] == -1:
                counter = enumerate_line.index(number)
                for again_line in list_lines[list_lines.index(line) + 1: list_lines.index(line) + 5]:
                    counter += 1
                    if counter < len(line):
                        if again_line[counter] == 1:
                            count_of_one += 1

                        elif again_line[counter] == -1:
                            count_of_negative_one += 1

                        if count_of_one == number_to_be_true or count_of_negative_one == number_to_be_true:
                            print(again_line)
                            return True

                    else:
                        break

    return False


def main():
    number_to_be_true = 5
    lines = [[0, 0, 1, 1, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]

    # if check_vertical_line(number_to_be_true, lines):
    #    print("Vertical")
    #    return True

    print(check_horizontal_line(lines))


#    elif check_slash_lines_from_wright(number_to_be_true, lines):
#        print("Slash from wright")
#        return True
#
#    lines.reverse()
#    if check_slash_lines_from_wright(number_to_be_true, lines):
#        print("Slash from left")
#        return True
#
#    else:
#        return False
#

if __name__ == "__main__":
    main()
