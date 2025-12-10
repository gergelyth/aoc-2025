import sys
from util import get_lines
import z3

TEST = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

#take the biggest number, press it as many times as we can while still under target end state
#remove presses from joltages, recursively call with those buttons removed and target end state adjusted
#if it doesn't work, return back, try 1 press of the second biggest button
def solve(lines):
    result = 0

    for line in lines:
        parts = line.split()
        #TODO can we just simply parse a tuple in python?
        buttons_raw, joltages = [list(map(int, button[1:-1].split(","))) for button in parts[1:-1]], [int(n) for n in parts[-1][1:-1].split(",")]

        free_variables = [z3.Int(f"res_{i}") for i in range(len(buttons_raw))]
        optimizer = z3.Optimize()
        max_jolt = max(joltages)
        optimizer.add(z3.And([var >= 0 for var in free_variables]))
        optimizer.add(z3.And([var <= max_jolt for var in free_variables]))
        for jolt_index, joltage in enumerate(joltages):
            optimizer.add(z3.And(sum([free_variables[button_idx] for button_idx, button in enumerate(buttons_raw) if jolt_index in button]) == joltage))

        optimizer.minimize(sum(free_variables))
        if optimizer.check() == z3.unsat:
            raise Exception(f"Line has no valid solution: {line}")

        model = optimizer.model()
        result += sum([model[var].as_long() for var in free_variables])

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