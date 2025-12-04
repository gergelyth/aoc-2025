import sys
from util import Matrix, get_lines

TEST = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def solve(matrix):
    result = 0

    while (removed_items := [
        (r,c)
        for r in range(matrix.row_count)
        for c in range(matrix.col_count)
        if matrix.get_item(r,c) == "@" and matrix.get_all_surrounding(r,c).count("@") < 4
    ]):
        result += len(removed_items)
        for removed_item in removed_items:
            matrix.set_item_pos(removed_item, ".")
    
    return result

def read_input():
    if not sys.stdin.isatty():
        input_data = sys.stdin.read()
    else:
        input_data = TEST

    matrix = Matrix(input_data)
    return matrix

if __name__ == "__main__":
    matrix = read_input()
    print(solve(matrix))