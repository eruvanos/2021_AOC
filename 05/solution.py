# fmt: off
import sys
from collections import Counter

from utils.vector import Vec2

sys.path.append("..")


# fmt: on

def part_1(data):
    dangerous_cells = []

    for row in data:
        start, end = row.split(" -> ")
        start_x, start_y = map(int, start.split(","))
        end_x, end_y = map(int, end.split(","))

        if start_x == end_x or start_y == end_y:
            for pos in generate_line_coordinates(start_x, start_y, end_x, end_y):
                dangerous_cells.append(pos)

    counter = Counter(dangerous_cells)
    # for pos, count in counter.items():
    #     print(f"{pos=}, {count=}")

    # draw field
    # for y in range(10):
    #     print()
    #     for x in range(10):
    #         print(counter.get((x, y), "."), end="")

    return len(list(filter(lambda v: v > 1, counter.values())))


def generate_line_coordinates(x1, y1, x2, y2) -> list:
    angle_vector = Vec2(x2 - x1, y2 - y1)
    angle = angle_vector.degree()

    slope = {
        0.0: Vec2(1, 0),
        45.0: Vec2(1, 1),
        90.0: Vec2(0, 1),
        135.0: Vec2(-1, 1),
        180.0: Vec2(-1, 0),
        225.0: Vec2(-1, -1),
        270.0: Vec2(0, -1),
        315.0: Vec2(1, -1),
    }[angle]

    cur = Vec2(x1, y1)
    points = [cur]
    while cur != Vec2(x2, y2):
        cur += slope
        points.append(cur)

    return sorted(points)


def part_2(data):
    dangerous_cells = []

    for row in data:
        start, end = row.split(" -> ")
        start_x, start_y = map(int, start.split(","))
        end_x, end_y = map(int, end.split(","))

        for pos in generate_line_coordinates(start_x, start_y, end_x, end_y):
            dangerous_cells.append(pos)

    counter = Counter(dangerous_cells)
    return len(list(filter(lambda v: v > 1, counter.values())))


def parse(lines):
    # lines = [int(l) for l in lines]
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
