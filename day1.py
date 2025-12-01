import sys
from util import get_lines

# or just use 
# curl -s --cookie "session=COOKIE" https://adventofcode.com/2025/day/1/input | python day1.py

TEST = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

def solve(lines):
    result = 0
    
    dial = 50
    for line in lines:
        turn = int(line[1:])
        if line[0] == 'L':
            dial -= turn
        else:
            dial += turn

        dial = dial % 100
        if dial == 0:
            result += 1

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