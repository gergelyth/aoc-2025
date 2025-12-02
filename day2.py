import sys
from util import get_lines

TEST = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def solve(line):
    result = 0

    # count digits, only even digit numbers need to be considered
    # basically get the range of digits (i.e. "11"->2, "4444"->4, so our range is 2,3,4), then get the numbers by pasting the 1 or 2 digit numbers together
    # it's enough to start from the "first half of lower bound" and finish at "first half of upper bound"
    ranges = [r.split("-") for r in line.split(",")]
    for r in ranges:
        lower_digit_count, upper_digit_count = len(r[0]), len(r[1])
        lower, upper = int(r[0]), int(r[1])

        for i in range(lower_digit_count, upper_digit_count+1):
            if i % 2 == 1:
                continue

            if i == lower_digit_count:
                base_number = r[0][:lower_digit_count // 2]
            else:
                base_number = "1" + "0" * ((i-1) // 2)
            
            while True:
                candidate = int(base_number * 2)
                if len(str(candidate)) != i or candidate > upper:
                    break
                
                if lower <= candidate <= upper:
                    result += candidate

                base_number = str(int(base_number) + 1) 
    
    return result

def read_input():
    if not sys.stdin.isatty():
        input_data = sys.stdin.read()
    else:
        input_data = TEST

    return input_data

if __name__ == "__main__":
    input = read_input()
    print(solve(input))