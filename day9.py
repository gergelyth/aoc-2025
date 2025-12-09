import sys
from util import get_lines

TEST = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

# raytrace
def is_inside(point, coordinates):
    j = len(coordinates) - 1
    inside = False
    for i in range(len(coordinates)):
        xi, yi = coordinates[i]
        xj, yj = coordinates[j]

        if ((yi > point[1]) != (yj > point[1])) and (point[0] < (xj - xi) * (point[1] - yi) / (yj - yi) + xi):
            inside = not inside
        j = i

    return inside

def get_boundary(vertices):
    boundary = set()
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]

        # Get all points on line from (x1,y1) to (x2,y2)
        dx = 0 if x2 == x1 else (1 if x2 > x1 else -1)
        dy = 0 if y2 == y1 else (1 if y2 > y1 else -1)

        x, y = x1, y1
        while (x, y) != (x2, y2):
            boundary.add((x, y))
            x += dx
            y += dy
        boundary.add((x2, y2))

    return boundary

# an edge is fine if it goes along the boundary
# if we arrive at a point not on the boundary, we can raytrace it
# if that's fine, we can jump to the next boundary point because all points until then are guaranteed to be inside
def is_rect_edge_fine(coordinates, boundary, raytrace_cache, ranges, func):
    fine_until_boundary = False
    for x in range(ranges[0], ranges[1]):
        point = func(x)
        if point in boundary:
            fine_until_boundary = False
            continue
        if fine_until_boundary:
            continue

        if point not in raytrace_cache:
            raytrace_cache[point] = is_inside(point, coordinates)
        if not raytrace_cache[point]:
            return False

        fine_until_boundary = True

    return True

def is_good_rectangle(coordinates, boundary, raytrace_cache, first, second):
    horizontal_range = (min(first[1],second[1]), max(first[1],second[1])+1)
    vertical_range = (min(first[0],second[0]), max(first[0],second[0])+1)
    return (is_rect_edge_fine(coordinates, boundary, raytrace_cache, horizontal_range, lambda y: (first[0], y)) 
        and is_rect_edge_fine(coordinates, boundary, raytrace_cache, horizontal_range, lambda x: (second[0], x))
        and is_rect_edge_fine(coordinates, boundary, raytrace_cache, vertical_range, lambda x: (x, first[1]))
        and is_rect_edge_fine(coordinates, boundary, raytrace_cache, vertical_range, lambda x: (x, second[1])))

def solve(lines):
    coordinates = [tuple(map(int, line.split(","))) for line in lines]
    boundary = get_boundary(coordinates)
    raytrace_cache = {}
    
    max_area = 0
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            if is_good_rectangle(coordinates, boundary, raytrace_cache, coordinates[i], coordinates[j]):
                area = (abs(coordinates[i][0] - coordinates[j][0]) + 1) * (abs(coordinates[i][1] - coordinates[j][1]) + 1)
                max_area = max(max_area, area)
    
    return max_area

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