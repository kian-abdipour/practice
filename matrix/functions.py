def check_horizontal_line(list_lines):
    for line in list_lines:
        count = 0
        selected_number = 0
        for number in line:
            if number != selected_number or number == 0:
                if number != 0:
                    selected_number = number
                count = 0
            if number == selected_number:
                count += 1

            if count == 5:
                return True
    return False


def check_horizontal_line_2(number_to_be_true, list_lines):
    if len(list_lines) >= 5:
        number_one = 1
        number_negative_one = 1
        for line in list_lines:
            enum_line = list(enumerate(line))
            for number in enum_line[:-1]:
                if number[1] != 0:
                    next_number = line[enum_line.index(number) + 1]
                    if number[1] == next_number:
                        if number[1] == 1:
                            number_one += 1
                        elif number[1] == -1:
                            number_negative_one += 1
                        if number_one == number_to_be_true or number_negative_one == number_to_be_true:
                            return True
                    else:
                        number_one = 1
                        number_negative_one = 1
    return False


def check_vertical_line_1(number_to_be_true, list_lines):
    for line in list_lines:
        enum_line = list(enumerate(line))
        for number in enum_line:
            number_one = 1
            number_negative_one = 1
            if number[1] == 1 or number[1] == -1:
                index_number = enum_line.index(number)

                for again_line in list_lines[list_lines.index(line) + 1: list_lines.index(line) + 5]:
                    if again_line[index_number] == 1:
                        number_one += 1

                    elif again_line[index_number] == -1:
                        number_negative_one += 1

                    if number_one == number_to_be_true or number_negative_one == number_to_be_true:
                        return True

    return False


def check_vertical_line(list_lines):
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


def check_vertical_and_slash_line(list_lines):
    for line in list_lines:
        enum_line = list(enumerate(line))

        for number in enum_line:
            counter = 0
            counter_index = 0
            if number[1] != 0:

                for again_line in list_lines:
                    if again_line[enum_line.index(number)] == number[1]:
                        counter += 1
                        if counter == 5:
                            print("From vertical")
                            return True

                    else:
                        counter = 0

                counter = 0
                for again_line_2 in list_lines:
                    if again_line_2[enum_line.index(number) + 1] == number[1]:
                        counter += 1
                        if counter == 5:
                            print("From vertical")
                            return True

                    else:
                        counter = 0

    return False


lines = [[1, -1, 1, 1, 0, 1, 0],
         [-1, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, -1, 0, 0, 0, 0, 0]]


print(check_vertical_and_slash_line(lines))

