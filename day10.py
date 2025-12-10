import sys
from util import get_lines

TEST = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

def distribute(total, slots):
    if slots == 1:
        yield [total]
        return
    for first in range(total, -1, -1):
        for rest in distribute(total - first, slots - 1):
            yield [first] + rest

def calc(end_state, button_configs, joltages, i):
    if joltages[i] == 0:
        return calc(end_state, button_configs, joltages, i+1)

    needed_presses = joltages[i]
    relevant_buttons = {key: value for key, value in button_configs.items() if i in value}
    if len(relevant_buttons) == 0:
        return -1
    
    remaining_buttons = {key: value for key, value in button_configs.items() if key not in relevant_buttons}
    for distribution in distribute(needed_presses, len(relevant_buttons)):
        new_target = end_state - sum(distribution[index] * key for index, key in enumerate(relevant_buttons))
        if new_target < 0:
            continue

        new_joltage = list(joltages)
        for index, key in enumerate(relevant_buttons):
            # new_joltage -= button_press_count * button_config
            for x in relevant_buttons[key]:
                new_joltage[x] -= distribution[index]

        if any([x < 0 for x in new_joltage]):
            continue

        if all([x == 0 for x in new_joltage]):
            return needed_presses

        rec = calc(new_target, remaining_buttons, new_joltage, i+1)
        if rec == -1:
            continue
        return needed_presses + rec

    return -1

#take the biggest number, press it as many times as we can while still under target end state
#remove presses from joltages, recursively call with those buttons removed and target end state adjusted
#if it doesn't work, return back, try 1 press of the second biggest button
def solve(lines):
    result = 0

    for line in lines:
        parts = line.split()
        #TODO can we just simply parse a tuple in python?
        buttons_raw, joltages = [list(map(int, button[1:-1].split(","))) for button in parts[1:-1]], [int(n) for n in parts[-1][1:-1].split(",")]

        end_state = 0
        for i, joltage in enumerate(reversed(joltages)):
            end_state += 2 ** i * joltage
        
        buttons_arr = [["1" if i in button_raw else "0" for i in range(len(joltages))] for button_raw in buttons_raw]
        buttons = [int("".join(b), 2) for b in buttons_arr]
        button_configs = dict(reversed(sorted(zip(buttons, buttons_raw))))

        print(joltages)
        button_configs = dict(sorted(button_configs.items(), key=lambda item: sum(joltages[i] for i in item[1]), reverse=True))
        print(button_configs)
        # print(buttons[0] * 1 + buttons[1] * 3 + buttons[3] * 3 + buttons[4] * 1 + buttons[5] * 2)
        # print(end_state)

        result += calc(end_state, button_configs, joltages, 0)
        print("Line done")

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