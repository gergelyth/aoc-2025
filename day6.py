import sys
import math
from util import get_lines

TEST = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

def calc(columns_backwards):
    #get the operator
    operator = (columns_backwards[-1]).pop()
    numbers = [int("".join(c)) for c in columns_backwards]
    
    if operator == "+":
        return sum(numbers)
    elif operator == "*":
        return math.prod(numbers)

def solve(lines):
    result = 0

    columns_backwards = []
    for i in range(len(lines[0])-1, -1, -1):
        column = [line[i] for line in lines]
        if not all(x == " " for x in column):
            columns_backwards.append(column)
            continue
        
        result += calc(columns_backwards)
        columns_backwards = []

    result += calc(columns_backwards)
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