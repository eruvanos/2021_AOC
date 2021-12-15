# fmt: off
import sys
from collections import defaultdict
from typing import Set, List, Dict, Iterable

from termcolor import colored

from utils.path import Graph, a_star_search, manhattan
from utils.vector import Vec2, manhattan_neighbors, get_max_x, get_max_y

sys.path.append("..")


# fmt: on

class MyGraph(Graph):
    def __init__(self, data: Dict, scale=1):
        self.data = data
        self.scale = scale

        if scale > 1:
            len_x = max(x for x, _ in data.keys()) + 1
            len_y = max(y for _, y in data.keys()) + 1
            for x in range(0, len_x * scale):
                for y in range(0, len_y * scale):

                    base_cost = self.data[(x % len_x, y % len_y)]
                    tile_cost = manhattan((0, 0), (x // len_x, y // len_y))
                    cost = (base_cost + tile_cost)

                    while cost > 9:
                        cost -= 9

                    self.data[(x, y)] = cost

    def neighbors(self, current: Vec2) -> List:
        return [n for n in manhattan_neighbors(current) if n in self.data]

    def cost(self, current: Vec2, next: Vec2) -> int:
        return self.data[next]

    def print(self, visited: Iterable[Vec2]):
        visited = set(visited)
        max_x = max(x for x, _ in self.data.keys()) + 1
        max_y = max(y for _, y in self.data.keys()) + 1

        if visited is None:
            visited = set()

        for y in range(max_y):
            for x in range(max_x):
                if (x, y) in visited:
                    print(colored(self.data[(x, y)], color="yellow"), end="")
                else:
                    print(self.data[(x, y)], end="")
            print()


def part_1(grid):
    start = Vec2(0, 0)
    target = Vec2(get_max_x(grid.keys()), get_max_y(grid.keys()))

    graph = MyGraph(grid)
    path = a_star_search(graph, start, target) or []

    print()
    graph.print(path)
    print(f"{path=}")

    return sum(grid[pos] for pos in path)


def part_2(grid):
    start = Vec2(0, 0)

    len_x = get_max_x(grid.keys()) + 1
    len_y = get_max_y(grid.keys()) + 1
    target = Vec2(len_x * 5 - 1, len_y * 5 - 1)

    graph = MyGraph(grid, scale=5)
    path = a_star_search(graph, start, target) or []

    print()
    print(f"{path=}")

    return sum(grid[pos] for pos in path)


def parse(lines):
    data = [[int(i) for i in l] for l in lines]
    grid = defaultdict(int)
    for y, cells in enumerate(data):
        for x, level in enumerate(cells):
            grid[(x, y)] = int(level)
    return grid


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
