import sys
from util import get_lines

TEST = """987654321111111
811111111111119
234234234234278
818181911112111"""

def solve(lines):
    result = 0

    # we keep track of the max number and we find the highest after that
    # special handling for the last number in the line
    for line in lines:
        first_digit = 0
        second_digit = 0
        
        for i in range(len(line)):
            n = int(line[i])

            if n > first_digit and i != len(line)-1:
                first_digit = n
                second_digit = 0
            elif n > second_digit:
                second_digit = n

        result += int(str(first_digit) + str(second_digit))
    
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