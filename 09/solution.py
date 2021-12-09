# fmt: off
import math
import sys

from utils.path import ArrayGraph

sys.path.append("..")


# fmt: on

def find_minima(graph: ArrayGraph):

    return [
        (x, y, c)
        for x, y, c in graph
        if c < min(graph.get(n) for n in graph.neighbors((x, y)))
    ]


def part_1(data):
    minima = find_minima(ArrayGraph(data))
    # print(graph.neighbors(Vec2(0, 0)))
    return sum(c + 1 for x, y, c in minima)


def part_2(data):
    graph = ArrayGraph(data)
    minima = find_minima(graph)

    basin_sizes = []
    for x, y, _ in minima:
        basin = set()
        neighbors = [(x, y)]
        while neighbors:
            current = neighbors.pop()
            basin.add(current)
            for n in graph.neighbors(current):
                if n not in basin and graph.get(n) != 9:
                    neighbors.append(n)

        basin_sizes.append(len(basin))

    return math.prod(list(sorted(basin_sizes, reverse=True))[:3])


def parse(lines):
    lines = [[int(c) for c in l] for l in lines]
    return lines


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(parse(lines[:])))
    print("Part 2: ", part_2(parse(lines[:])))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
