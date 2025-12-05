import sys
from util import flatten_overlapping_ranges, get_lines

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

    # flatten the overlaps
    ranges_str = lines[:lines.index("")]
    ranges = [tuple(map(int, range_str.split("-"))) for range_str in ranges_str]

    #count the numbers now
    for lower, upper in flatten_overlapping_ranges(ranges):
        result += upper - lower + 1
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