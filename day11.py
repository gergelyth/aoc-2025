import sys
from util import get_lines
from collections import deque, defaultdict
from dataclasses import dataclass

TEST = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

@dataclass
class Paths:
    all_paths: int
    with_dac: int
    with_fft: int
    final_paths: int

def find_path(node, graph, cache):
    if node == "out":
        return Paths(1,0,0,0)
    if node in cache:
        return cache[node]
    
    result = Paths(0,0,0,0)
    for edge in graph[node]:
        new_path = find_path(edge, graph, cache)
        result.all_paths += new_path.all_paths
        if node == "fft":
            result.final_paths += new_path.with_dac
            #all of these are converted to final paths
            result.with_dac += 0
            result.with_fft += new_path.all_paths - new_path.with_fft
        elif node == "dac":
            result.final_paths += new_path.with_fft
            result.with_fft += 0
            result.with_dac += new_path.all_paths - new_path.with_dac
        else:
            result.final_paths += new_path.final_paths
            result.with_dac += new_path.with_dac
            result.with_fft += new_path.with_fft

    cache[node] = result
    return result

def solve(lines):
    graph = {(p := line.split(":"))[0]: p[1].split() for line in lines}
    cache = {}

    return find_path("svr", graph, cache)

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