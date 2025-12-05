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

    # flatten the overlaps
    ranges_str = lines[:lines.index("")]
    ranges = [tuple(map(int, range_str.split("-"))) for range_str in ranges_str]

    flattened_ranges_temp = []
    for start, end in ranges:
        flattened_ranges_temp.append((start, "start"))
        flattened_ranges_temp.append((end, "end"))

    flattened_ranges_temp.sort(key= lambda x: (x[0], x[1] != "start"))

    flattened = []
    stack = []
    for number, bound_type in flattened_ranges_temp:
        if bound_type == "start":
            stack.append(number)
        else:
            if len(stack) == 1:
                flattened.append((stack[0], number))
            stack.pop()

    #count the numbers now
    for lower, upper in flattened:
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