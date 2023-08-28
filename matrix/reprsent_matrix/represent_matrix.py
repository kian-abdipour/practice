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


def check_is_diagonal_matrix(matrix, condition_lower_and_upper_matrix):
    if condition_lower_and_upper_matrix:

        for line in matrix:
            if line[matrix.index(line)] != 0:
                pass

            else:
                return False

        return True

    else:
        return False


def check_is_unit_matrix(matrix, condition_lower_and_upper_matrix):
    if condition_lower_and_upper_matrix:

        for line in matrix:
            if line[matrix.index(line)] == 1:
                pass

            else:
                return False

        return True

    else:
        return False


def check_is_lower_triangular_matrix(matrix, condition_square_matrix):
    if condition_square_matrix and len(matrix[0]) > 1:
        for line in matrix[:-1]:
            if not any(line[matrix.index(line) + 1:]):
                pass

            else:
                return False

        return True

    else:
        return False


def check_is_upper_triangular_matrix(matrix, condition_square_matrix):
    if condition_square_matrix and len(matrix[0]) > 1:
        for line in matrix[1:]:
            if not any(line[:matrix.index(line)]):
                pass

            else:
                return False

        return True

    else:
        return False


def make_coherence_matrix(matrix, condition_square_matrix):
    if condition_square_matrix:
        coherence_matrix = []
        while len(coherence_matrix) != len(matrix):
            coherence_matrix.append([])

        for line in coherence_matrix:
            while len(line) != len(matrix):
                line.append([])

        counter_i = 0
        counter_j = 0
        for line in coherence_matrix:
            counter_j += 1
            for number in line:
                counter_i += 1
                number.append(counter_i)
                number.append(counter_j)

            counter_i = 0

        return coherence_matrix

    else:
        return "Your matrix must be square matrix"


def make_transpose_matrix(matrix, condition_square_matrix):
    if condition_square_matrix:
        transpose_matrix = []
        while len(transpose_matrix) != len(matrix):
            transpose_matrix.append([])

        counter = 0
        for line in matrix:
            for number in line:
                for line_transpose in transpose_matrix:
                    line_transpose.append(line[counter])

                    counter += 1
                break

            counter = 0

        return transpose_matrix

    else:
        return "You matrix must be square matrix"


