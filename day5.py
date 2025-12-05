import sys
from util import get_lines

TEST = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def solve(lines):
    result = 0

    ranges_str, numbers_str = lines[:lines.index("")], lines[lines.index("")+1:]
    ranges = [tuple(map(int, range_str.split("-"))) for range_str in ranges_str]

    for number_str in numbers_str:
        number = int(number_str)
        for lower, upper in ranges:
            if lower <= number <= upper:
                result += 1
                break

    return result

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