import sys
from util import get_lines
from collections import defaultdict

TEST = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

def solve(lines):
    col_count = len(lines[0])
    
    beams = defaultdict(int, { lines[0].index("S") : 1 })
    for line in lines[1:]:
        new_beams = defaultdict(int)
        for beam_index, beam_value in beams.items():
            if line[beam_index] == ".":
                new_beams[beam_index] += beam_value
            elif line[beam_index] == "^":
                if beam_index-1 >= 0:
                    new_beams[beam_index-1] += beam_value
                if beam_index+1 < col_count:
                    new_beams[beam_index+1] += beam_value
                
        beams = new_beams

    return sum(beams.values())

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