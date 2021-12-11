# fmt: off
import sys
from collections import defaultdict
from itertools import count

from termcolor import colored

from utils.vector import Vec2, neigbors

sys.path.append("..")


# fmt: on

def print_levels(octos_by_level, flashed=None):
    if flashed is None:
        flashed = set()

    octos_by_coords = {octo: level for level, octos in octos_by_level.items() for octo in octos}
    for y in range(10):
        for x in range(10):
            if (x, y) in flashed:
                print(colored(octos_by_coords[(x, y)], color="yellow"), end="")
            else:
                print(octos_by_coords[(x, y)], end="")
        print()


def step(octos_by_level):
    # increase all by one
    new_levels = defaultdict(set)
    for level in reversed(range(10)):
        new_levels[level + 1] = octos_by_level[level]

    # extract flashing (octo level over 9)
    flashing = new_levels[10]

    # prepare pos->octo map
    octos_by_coords = {octo: level for level, octos in new_levels.items() for octo in octos}

    # execute flashing
    flashed = set()
    while flashing:
        octo = flashing.pop()
        flashed.add(octo)

        for n in neigbors(octo):
            # skip if octo flashed or will flash already
            if n in flashed or n in flashing:
                continue

            # increse neighbor levels
            if n in octos_by_coords:
                octos_by_coords[n] += 1

                if octos_by_coords[n] > 9:
                    flashing.add(n)

    # reset flashed octos
    for octo in flashed:
        octos_by_coords[octo] = 0

    # return state as level->octo map
    res = defaultdict(set)
    for octo, level in sorted(octos_by_coords.items()):
        res[level].add(octo)
    return res, flashed


def part_1(octos_by_level, debug=False):
    total_flashed = 0
    print_levels(octos_by_level)
    for r in range(100):
        octos_by_level, flashed = step(octos_by_level)
        total_flashed += len(flashed)
        if debug:
            print()
            print(f"=== {r + 1} ===")
            print_levels(octos_by_level, flashed)

    return total_flashed


def part_2(octos_by_level):
    total_flashed = 0
    print_levels(octos_by_level)

    r = 0
    for r in count(1):
        octos_by_level, flashed = step(octos_by_level)
        total_flashed += len(flashed)
        if len(flashed) == 100:
            break

    return r


def parse(lines):
    data = [[int(i) for i in l] for l in lines]
    octos_by_level = defaultdict(set)
    for y, cells in enumerate(data):
        for x, level in enumerate(cells):
            octos_by_level[level].add(Vec2(x, y))
    return octos_by_level


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
