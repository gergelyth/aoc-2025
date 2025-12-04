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

    for r in range(matrix.row_count):
        for c in range(matrix.col_count):
            if matrix.get_item(r,c) != "@":
                continue
            
            surrounds = matrix.get_all_surrounding(r, c)
            if surrounds.count("@") < 4:
                result += 1
    
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