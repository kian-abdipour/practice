from matrix.calculate_matrix.matrix import make_matrix
from matrix.calculate_matrix.matrix import check_horizontal_line
from matrix.calculate_matrix.matrix import check_vertical_and_slash_line


def main():
    lines = make_matrix()
    print(lines)

    if check_horizontal_line(lines):
        return True

    elif check_vertical_and_slash_line(lines):
        return True

    lines.reverse()
    if check_vertical_and_slash_line(lines):
        return True

    return False


if __name__ == "__main__":
    print(main())

