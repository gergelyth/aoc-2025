import sys
import math
from util import get_lines

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
    coordinates = [tuple(map(int, line.split(","))) for line in lines]
    distances = {}
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distances[(coordinates[i], coordinates[j])] = math.dist(coordinates[i], coordinates[j])

    sorted_dist = sorted(distances.items(), key=lambda x: x[1])

    circuits = {}
    point_to_circuit = {}
    new_circuit_id = 0
    for (coord1, coord2), _ in sorted_dist:
        circuit1, circuit2 = point_to_circuit.get(coord1), point_to_circuit.get(coord2)
        if circuit1 is None and circuit2 is None:
            point_to_circuit[coord1] = point_to_circuit[coord2] = new_circuit_id
            circuits[new_circuit_id] = set([coord1, coord2])
            new_circuit_id += 1
        elif circuit1 is None or circuit2 is None:
            new_circuit = circuit1 if circuit1 is not None else circuit2
            point_to_circuit[coord1] = point_to_circuit[coord2] = new_circuit
            circuits[new_circuit].update([coord1, coord2])
        else:
            #both have circuits
            if circuit1 != circuit2:
                for merging_point in circuits[circuit2]:
                    circuits[circuit1].add(merging_point)
                    point_to_circuit[merging_point] = circuit1
                del circuits[circuit2]

        if len(circuits) == 1 and len(point_to_circuit) == len(coordinates):
            break

    return coord1[0] * coord2[0]

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