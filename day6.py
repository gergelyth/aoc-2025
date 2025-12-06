import sys
import math
from util import get_lines

TEST = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

def solve(lines):
    result = 0

    split_lines = [line.split() for line in lines]
    for i in range(len(split_lines[0])):
        problem = [split_line[i] for split_line in split_lines]
        numbers = [int(n) for n in problem[:-1]]
        if problem[-1] == "+":
            result += sum(numbers)
        elif problem[-1] == "*":
            result += math.prod(numbers)

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