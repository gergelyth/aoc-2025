import sys
import math
from util import get_lines

TEST = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

def solve(lines):
    coordinates = [tuple(map(int, line.split(","))) for line in lines]
    
    max_area = 0
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            area = (abs(coordinates[i][0] - coordinates[j][0]) + 1) * (abs(coordinates[i][1] - coordinates[j][1]) + 1)
            max_area = max(max_area, area)
    
    return max_area

def read_input():
    if not sys.stdin.isatty():
        input_data = sys.stdin.read()
    else:
        input_data = TEST

    lines = get_lines(input_data)
    return lines

if __name__ == "__main__":
    input = read_input()
    print(solve(input))