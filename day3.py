import sys
from util import get_lines

TEST = """987654321111111
811111111111119
234234234234278
818181911112111"""

def solve(lines):
    digit_count = 12
    result = 0

    # we keep track of the max number and we find the highest after that
    # special handling for the last number in the line
    # we keep the same if/elif structure with an array
    for line in lines:
        digits = [0] * digit_count
        
        for i in range(len(line)):
            n = int(line[i])

            for d in range(len(digits)):
                # line is 7 long (0-6), digit count is 3 (4,5,6), d is 1, i must be <= 5
                if n > digits[d] and i <= len(line) - digit_count + d:
                    digits[d] = n
                    #anull everything after it
                    digits[d+1:] = [0] * len(digits[d+1:])
                    break
    
        result += int("".join([str(d) for d in digits]))
    
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