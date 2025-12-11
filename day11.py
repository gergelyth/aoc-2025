import sys
from util import get_lines
from collections import deque, defaultdict

TEST = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

def find_path(node, graph, cache):
    if node == "out":
        return 1
    if node in cache:
        return cache[node]
    
    result = 0
    for edge in graph[node]:
        result += find_path(edge, graph, cache)

    cache[node] = result
    return result

def solve(lines):
    graph = {(p := line.split(":"))[0]: p[1].split() for line in lines}
    cache = {}

    return find_path("you", graph, cache)

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