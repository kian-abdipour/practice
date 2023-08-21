from represent_matrix import check_is_square_matrix
from represent_matrix import check_is_row_matrix
from represent_matrix import check_is_columnar_matrix
from represent_matrix import check_is_zero_matrix
from represent_matrix import check_is_diagonal_matrix
from represent_matrix import check_is_unit_matrix
from represent_matrix import check_is_lower_triangular_matrix
from represent_matrix import check_is_upper_triangular_matrix
from represent_matrix import make_transpose_matrix
from represent_matrix import make_coherence_matrix


def main():
    matrix = []

    is_square_matrix = check_is_square_matrix(matrix)
    print("1 _ Square matrix:", is_square_matrix)
    print("2 _ Row matrix:", check_is_row_matrix(matrix))
    print("3 _ Columnar matrix:", check_is_columnar_matrix(matrix))
    print("4 _ Zero matrix:", check_is_zero_matrix(matrix))
    print("5 _ Diagonal matrix:", check_is_diagonal_matrix(matrix, is_square_matrix))
    print("6 _ Lower triangular matrix:", check_is_lower_triangular_matrix(matrix, is_square_matrix))
    print("7 _ Upper triangular matrix:", check_is_upper_triangular_matrix(matrix, is_square_matrix))

    is_lower_and_upper_triangle_matrix = (check_is_lower_triangular_matrix(matrix, is_square_matrix)
                                          and check_is_upper_triangular_matrix(matrix, is_square_matrix))
    print("8 _ Unit matrix:", check_is_unit_matrix(matrix, is_lower_and_upper_triangle_matrix))
    print("9 _ transpose matrix:", make_transpose_matrix(matrix, is_square_matrix))
    print("10 _ coherence matrix:", make_coherence_matrix(matrix, is_square_matrix))


if __name__ == "__main__":
    main()

else:
    print("You must run this function in main file")

