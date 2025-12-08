import sys
import math
from util import get_lines
from collections import Counter

TEST = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

def solve(lines):
    result = 0

    coordinates = [tuple(map(int, line.split(","))) for line in lines]
    distances = {}
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distances[(coordinates[i], coordinates[j])] = math.dist(coordinates[i], coordinates[j])

    sorted_dist = sorted(distances.items(), key=lambda x: x[1])

    point_to_circuit = {}
    new_circuit_id = 0
    connections_made = 0
    for (coord1, coord2), _ in sorted_dist:
        circuit1, circuit2 = point_to_circuit.get(coord1), point_to_circuit.get(coord2)
        if circuit1 is None and circuit2 is None:
            point_to_circuit[coord1] = point_to_circuit[coord2] = new_circuit_id
            new_circuit_id += 1
        elif circuit1 is None or circuit2 is None:
            point_to_circuit[coord1] = point_to_circuit[coord2] = circuit1 if circuit1 is not None else circuit2
        else:
            #both have circuits
            if circuit1 != circuit2:
                #we need to merge them (circuit2 to circuit1) - this is inefficient for now, we could improve this
                for point, circuit in point_to_circuit.items():
                    if circuit == circuit2:
                        point_to_circuit[point] = circuit1

        connections_made += 1
        if connections_made == 1000:
            break

    top_3 = Counter(point_to_circuit.values()).most_common(3)
    return math.prod([x[1] for x in top_3])

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