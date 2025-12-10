import sys
import time
from util import get_lines

TEST = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

def calc(target, buttons, i):
    button = buttons[i]    
    if i == len(buttons)-1:
        if target % button == 0:
            return target // button
        return -1

    max_presses = target // button
    if max_presses == 0:
        return calc(target, buttons, i+1)
    
    for j in range(max_presses, -1, -1):
        rec = calc(target - j * button, buttons, i+1)
        if rec == -1:
            continue
        return j + rec

    return -1

#take the biggest number, press it as many times as we can while still under target end state
#remove presses from joltages, recursively call with those buttons removed and target end state adjusted
#if it doesn't work, return back, try 1 press of the second biggest button
def solve(lines):
    result = 0

    start = time.time()
    for l_idx, line in enumerate(lines):
        parts = line.split()
        #TODO can we just simply parse a tuple in python?
        buttons_raw, joltages = [list(map(int, button[1:-1].split(","))) for button in parts[1:-1]], [int(n) for n in parts[-1][1:-1].split(",")]

        target = 0
        carry = 0
        for i, joltage in enumerate(reversed(joltages)):
            if i == 0:
                target += ((joltage+carry) % 10)
            else:
                target += ((joltage+carry) % 10) * 10 ** i
            carry = (joltage+carry) // 10

        if carry > 0:
            target += carry * 10 ** (i+1)

        buttons_arr = [["1" if i in button_raw else "0" for i in range(len(joltages))] for button_raw in buttons_raw]
        buttons = [int("".join(b)) for b in buttons_arr]

        buttons.sort(reverse=True)
        calc_result = calc(target, buttons, 0)
        if calc_result == -1:
            raise Exception(f"No result for {line}")
        result += calc_result

        print(f"Line done {l_idx+1}/{len(lines)}")

    elapsed = time.time() - start
    print(f"Elapsed: {elapsed:.2f} seconds")
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