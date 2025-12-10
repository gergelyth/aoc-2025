import sys
import math
from util import get_lines

TEST = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

def calc(end_state, buttons):
    steps = 1

    states = set([0])
    while True:
        new_states = set()
        for button in buttons:
            for state in states:
                new_value = state + button
                if new_value == end_state:
                    return steps
                
                new_states.add(new_value)
        
        steps += 1
        states = new_states

def solve(lines):
    result = 0

    for line in lines[:1]:
        parts = line.split()
        #TODO can we just simply parse a tuple in python?
        buttons_raw, joltages = [list(map(int, button[1:-1].split(","))) for button in parts[1:-1]], [int(n) for n in parts[-1][1:-1].split(",")]

        end_state = 0
        for i, joltage in enumerate(reversed(joltages)):
            end_state += 2 ** i * joltage

        buttons_arr = [["1" if i in button_raw else "0" for i in range(len(joltages))] for button_raw in buttons_raw]
        buttons = [int("".join(b), 2) for b in buttons_arr]
        print(buttons)
        # print(buttons[0] * 1 + buttons[1] * 3 + buttons[3] * 3 + buttons[4] * 1 + buttons[5] * 2)
        # print(end_state)

        result += calc(end_state, buttons)
        print(result)

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