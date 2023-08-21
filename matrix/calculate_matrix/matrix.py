def make_matrix():
    layout_lines = int(input(": "))
    lucky_list = []

    while len(lucky_list) != layout_lines:
        lucky_list.append([])

    for line in lucky_list:
        while len(line) != layout_lines:
            line.append(0)

    return lucky_list


def check_horizontal_line(lines):
    for repeat_line in lines:
        for line in lines:
            enum_lines = list(enumerate(lines))
            for number in enum_lines:

                five_numbers = line[enum_lines.index(number): enum_lines.index(number)+5]
                if five_numbers == [1, 1, 1, 1, 1] or five_numbers == [-1, -1, -1, -1, -1]:
                    print(five_numbers[0], "WINNER from horizontal")
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
                            print(number[1], "WINNER from vertical")
                            return True

                    else:
                        counter = 0

                counter_index = enum_line.index(number)
                for again_line_2 in list_lines[list_lines.index(line)+1:]:
                    counter_index += 1
                    if counter_index < len(again_line_2):
                        if again_line_2[counter_index] == number[1]:
                            counter += 1
                            if counter == 5:
                                print(number[1], "WINNER from slash")
                                return True

                        else:
                            counter = 0

    return False

