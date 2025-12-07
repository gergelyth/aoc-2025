import sys
from util import get_lines

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
    result = 0

    col_count = len(lines[0])
    
    beams = set([lines[0].index("S")])
    for line in lines[1:]:
        new_beams = set()
        for beam in beams:
            if line[beam] == ".":
                new_beams.add(beam)
            elif line[beam] == "^":
                if beam-1 >= 0:
                    new_beams.add(beam-1)
                if beam+1 < col_count:
                    new_beams.add(beam+1)
                
                result += 1

        beams = new_beams

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