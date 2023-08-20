def check_is_square_matrix(matrix):
    counter = 0
    for line in matrix:
        if len(line) == len(matrix):
            counter += 1

    if counter == len(matrix) and len(matrix) > 0:
        return True

    else:
        return False


def check_is_row_matrix(matrix):
    if len(matrix) == 1:
        return True

    else:
        return False


def check_is_columnar_matrix(matrix):
    counter = 0
    for line in matrix:
        if len(line) == 1:
            counter += 1

    if counter == len(matrix):
        return True

    else:
        return False


def check_is_zero_matrix(matrix):
    if len(matrix) > 0:
        for line in matrix:
            if not any(line) and len(line) > 0:
                pass

            else:
                return False

    else:
        return False

    return True


def check_is_diagonal_matrix(matrix):
    if check_is_square_matrix(matrix):
        counter = 0
        for line in matrix:
            if line[counter] != 0:
                line.pop(counter)
                counter += 1
                if not any(line):
                    pass

                else:
                    return False

            else:
                return False

        return True

    else:
        return False


my_matrix = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 23, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 10]]
print(check_is_diagonal_matrix(my_matrix))
print(my_matrix)

