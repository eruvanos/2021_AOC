# fmt: off
import re
import sys
from typing import NamedTuple, Literal, List

sys.path.append("..")


# fmt: on

# Required code comparison  to get mine working xD
# https://www.reddit.com/r/adventofcode/comments/rlxhmg/comment/hpke376/?utm_source=share&utm_medium=web2x&context=3
def part_1(cubes,skip_huge=True):
    processed: List[Cube] = []

    for i, cube in enumerate(cubes):
        if abs(cube.min_y) > 50 and skip_huge:
            continue

        next_processed = []
        for previous in processed:
            next_processed.append(previous)
            if overlap := previous.intersection(cube):
                next_processed.append(overlap)

        if cube.on:
            next_processed.append(cube)

        processed = next_processed

    return sum(cube.volume() if cube.on else -cube.volume() for cube in processed)

#
# def part_1_x(data, ):
#     volume = 0
#     instructions = []
#
#     for inst in data:
#         if abs(inst.cube.min_x) > 50 and skip_huge:
#             continue
#
#         if inst.state == "on":
#             volume_change = inst.cube.volume()
#             for state, cube in instructions:
#                 if int_cube := cube.intersection(inst.cube):
#                     if state == "on":
#                         volume_change -= int_cube.volume()
#                     else:
#                         volume_change += int_cube.volume()
#             instructions.append(inst)
#
#         else:
#             volume_change = 0
#             cuts = []
#             for state, cube in instructions:
#                 if int_cube := cube.intersection(inst.cube):
#                     if state == "on":
#                         volume_change -= int_cube.volume()
#                         cuts.append(Instruction(state, cube))
#                     else:
#                         volume_change += int_cube.volume()
#             instructions.extend(cuts)
#
#         volume += volume_change
#
#     return volume


def part_2(cubes):
    return part_1(cubes, False)


class Cube(NamedTuple):
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    min_z: int
    max_z: int
    on: bool

    def volume(self):
        min_x, max_x, min_y, max_y, min_z, max_z, _ = self
        return (max_x + 1 - min_x) * (max_y + 1 - min_y) * (max_z + 1 - min_z)

    def intersection(self, c2: "Cube"):
        """Intersection with a cube"""
        c1_min_x, c1_max_x, c1_min_y, c1_max_y, c1_min_z, c1_max_z, c1_on = self
        c2_min_x, c2_max_x, c2_min_y, c2_max_y, c2_min_z, c2_max_z, c2_on = c2

        if not (
                ((c1_min_x <= c2_min_x & c2_min_x <= c1_max_x) or (c2_min_x <= c1_min_x & c1_min_x <= c2_max_x)) &
                ((c1_min_y <= c2_min_y & c2_min_y <= c1_max_y) or (c2_min_y <= c1_min_y & c1_min_y <= c2_max_y)) &
                ((c1_min_z <= c2_min_z & c2_min_z <= c1_max_z) or (c2_min_z <= c1_min_z & c1_min_z <= c2_max_z))
        ):
            return None

        x1 = max(c1_min_x, c2_min_x)
        x2 = min(c1_max_x, c2_max_x)
        y1 = max(c1_min_y, c2_min_y)
        y2 = min(c1_max_y, c2_max_y)
        z1 = max(c1_min_z, c2_min_z)
        z2 = min(c1_max_z, c2_max_z)

        return Cube(x1, x2, y1, y2, z1, z2, c2.on if self.on != c2.on else not self.on)


class Instruction(NamedTuple):
    state: Literal["on", "off"]
    cube: Cube


def parse(lines):
    cubes = []
    # on x=-48..-4,y=-28..24,z=-9..40
    pattern = re.compile(r"(on|off) x=(-?\d*)..(-?\d*),y=(-?\d*)..(-?\d*),z=(-?\d*)..(-?\d*)")
    for line in lines:
        state, min_x, max_x, min_y, max_y, min_z, max_z = pattern.match(line).groups()
        cubes.append(
            Cube(int(min_x), int(max_x), int(min_y), int(max_y), int(min_z), int(max_z), state == "on")
        )
    return cubes


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
