def make_list():
    layout_lines = int(input(": "))
    lines = []

    while len(lines) != layout_lines:
        lines.append([])

    for line in lines:
        while len(line) != layout_lines:
            line.append(0)

    return lines


def check_slash_lines_from_wright(number_to_be_true, lines):
    count_of_one = 0
    count_of_negative_one = 0

    for line in lines:
        enumerate_line = list(enumerate(line))
        for number in enumerate_line:
            if number[1] == 1 or number[1] == -1:
                if number[1] == 1:
                    count_of_one += 1

                elif number[1] == -1:
                    count_of_negative_one += 1

                counter = enumerate_line.index(number)
                for again_line in lines[lines.index(line) + 1: lines.index(line)+5]:
                    counter += 1
                    if counter < len(line):
                        if again_line[counter] == 1:
                            count_of_one += 1

                        elif again_line[counter] == -1:
                            count_of_negative_one += 1

                        if count_of_one == number_to_be_true or count_of_negative_one == number_to_be_true:
                            return True

                    else:
                        break

                count_of_one = 0

    return False


print(check_slash_lines_from_wright(5, make_list()))