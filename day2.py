import sys
from util import get_lines

TEST = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def solve(line):
    result = 0

    results = set()

    # count digits, only even digit numbers need to be considered
    # basically get the range of digits (i.e. "11"->2, "4444"->4, so our range is 2,3,4), then get the numbers by pasting the 1 or 2 digit numbers together
    # it's enough to start from the "first half of lower bound" and finish at "first half of upper bound"
    ranges = [r.split("-") for r in line.split(",")]
    for r in ranges:
        lower_digit_count, upper_digit_count = len(r[0]), len(r[1])
        lower, upper = int(r[0]), int(r[1])

        # i = base_number (repeating number) digit count
        for i in range(0, upper_digit_count // 2 + 1):
            base_number = "1" + "0" * i
            
            while True:
                base_multiplier = 2
                while True:
                    candidate = int(base_number * base_multiplier)
                    if candidate > upper:
                        break
                    
                    if lower <= candidate <= upper:
                        results.add(candidate)

                    base_multiplier += 1

                base_number = str(int(base_number) + 1) 
                if len(str(base_number)) > i+1:
                    break
    
    return sum(results)

def read_input():
    if not sys.stdin.isatty():
        input_data = sys.stdin.read()
    else:
        input_data = TEST

    return input_data

if __name__ == "__main__":
    input = read_input()
    print(solve(input))