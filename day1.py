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
        new_dial = dial
        turn = int(line[1:])
        if line[0] == 'L':
            new_dial -= turn
        else:
            new_dial += turn

        # full rotations + dial at exactly zero + sign change if needed
        result += (abs(new_dial) // 100) + (1 if new_dial == 0 else 0) + (1 if new_dial != 0 and dial != 0 and new_dial * dial < 0 else 0)
        # print("line", line)
        # print("dial", dial)
        # print("new_dial", new_dial)

        dial = new_dial % 100
        # print("result", result)

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