# fmt: off
import sys
from builtins import frozenset
from functools import lru_cache
from itertools import permutations
from typing import List, Set

from utils.vector import Vec3

sys.path.append("..")


# fmt: on

def transform(ss: Set[Vec3], dv: Vec3) -> Set[Vec3]:
    return {s + dv for s in ss}


def all_24(ss):
    return _all24(frozenset(ss))


@lru_cache(maxsize=None)
def _all24(ss):
    print("cache not hit")
    return [
        {Vec3(x, y, z) for x, y, z in ss},
        {Vec3(y, -x, z) for x, y, z in ss},
        {Vec3(-x, -y, z) for x, y, z in ss},
        {Vec3(-y, x, z) for x, y, z in ss},
        {Vec3(-x, y, -z) for x, y, z in ss},
        {Vec3(y, x, -z) for x, y, z in ss},
        {Vec3(x, -y, -z) for x, y, z in ss},
        {Vec3(-y, -x, -z) for x, y, z in ss},
        {Vec3(z, y, -x) for x, y, z in ss},
        {Vec3(z, x, y) for x, y, z in ss},
        {Vec3(z, -y, x) for x, y, z in ss},
        {Vec3(z, -x, -y) for x, y, z in ss},
        {Vec3(-z, y, x) for x, y, z in ss},
        {Vec3(-z, x, -y) for x, y, z in ss},
        {Vec3(-z, -y, -x) for x, y, z in ss},
        {Vec3(-z, -x, y) for x, y, z in ss},
        {Vec3(x, z, -y) for x, y, z in ss},
        {Vec3(-y, z, -x) for x, y, z in ss},
        {Vec3(-x, z, y) for x, y, z in ss},
        {Vec3(y, z, x) for x, y, z in ss},
        {Vec3(x, -z, y) for x, y, z in ss},
        {Vec3(-y, -z, x) for x, y, z in ss},
        {Vec3(-x, -z, -y) for x, y, z in ss},
        {Vec3(y, -z, -x) for x, y, z in ss},
    ]


def get_overlap(a: Set, b: Set):
    """Transform all points in b and check if they patch with a"""
    return a & b


def stitch(a: Set, b: Set, overlap=12):
    """Checks if images can be stitched and returns stitched scan relative to a's coordinate system"""

    for av in a:
        for bv in b:
            # calculate offset
            dv = av - bv

            # check if points in b match with points in a given the offset
            bt = transform(b, dv)
            if len(a & bt) >= overlap:
                print(f"found match {dv=}")
                return bt, dv
                # return a | bt

    return None


def part_1(data: List[Set[Vec3]], overlap=12):
    base = data.pop(0)

    while data:
        print(len(data))
        for tile in data[:]:
            for transition in all_24(tile):
                stitched = stitch(base, transition, overlap=overlap)
                if stitched:
                    new_points, _ = stitched
                    base = base | new_points
                    data.remove(tile)
                    break
            else:
                continue
            break

    return len(base)


def part_2(data: List[Set[Vec3]], overlap=12):
    base = data.pop(0)

    scanners = {Vec3(0, 0, 0)}

    while data:
        print(len(data))
        for tile in data[:]:
            for transition in all_24(tile):
                stitched = stitch(base, transition, overlap=overlap)
                if stitched:
                    new_points, scanner_loc = stitched
                    base = base | new_points
                    data.remove(tile)

                    scanners.add(scanner_loc)
                    break
            else:
                continue
            break

    max_man = 0
    for s1, s2 in permutations(scanners, 2):
        max_man = max(max_man, s1.manhattan(s2))

    return max_man


def parse(lines) -> List[Set[Vec3]]:
    scanners = []

    for line in lines:
        if len(line) == 0:
            continue

        if line.startswith("---"):
            scanners.append(set())
        else:
            coordinates = tuple(map(int, line.split(",")))
            if len(coordinates) == 2:
                coordinates += (0,)

            scanners[-1].add(Vec3(*coordinates))

    return scanners


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
