# fmt: off
import sys
from itertools import count

from utils.vector import Vec2

sys.path.append("..")


# fmt: on

def step(right_cucumbers, down_cucumbers, size=(10, 10)):
    moved = False

    new_right = set()
    dir = Vec2(1, 0)
    blocked = right_cucumbers | down_cucumbers
    for r in right_cucumbers:
        new_pos = r + dir
        new_pos %= size
        if new_pos not in blocked:
            new_right.add(new_pos)
            moved = True
        else:
            new_right.add(r)

    new_down = set()
    dir = Vec2(0, 1)
    blocked = new_right | down_cucumbers
    for r in down_cucumbers:
        new_pos = r + dir
        new_pos %= size
        if new_pos not in blocked:
            new_down.add(new_pos)
            moved = True
        else:
            new_down.add(r)

    return new_right, new_down, moved


def part_1(data):
    rc, dc, size = data

    def print_turn():
        print(f"=== {c}")
        for y in range(size[1]):
            for x in range(size[0]):
                if (x, y) in rc:
                    print(">", end="")
                elif (x, y) in dc:
                    print("v", end="")
                else:
                    print(".", end="")
            print()

    for c in count():
        # print_turn()
        rc, dc, moved = step(rc, dc, size=size)
        if not moved:
            break
    return c + 1


def part_2(data):
    pass


def parse(lines):
    right_cucumbers = set()
    down_cucumbers = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ">":
                right_cucumbers.add(Vec2(x, y))
            elif c == "v":
                down_cucumbers.add(Vec2(x, y))
    size = (x+1, y+1)
    return right_cucumbers, down_cucumbers, size


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
