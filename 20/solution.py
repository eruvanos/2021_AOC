# fmt: off
import sys
from collections import Counter
from typing import Dict

from utils.vector import Vec2, get_min_x, get_max_x, get_min_y, get_max_y, neigbors_tl_br

sys.path.append("..")


# fmt: on

def part_1(data):
    algorithm, image = data
    image: Dict

    default = "."

    for _ in range(2):
        new_image = {}
        min_x = get_min_x(image.keys())
        max_x = get_max_x(image.keys())
        min_y = get_min_y(image.keys())
        max_y = get_max_y(image.keys())
        for x in range(min_x - 2, max_x + 3):
            for y in range(min_y - 2, max_y + 3):
                index_string = "".join(image.get(n, default) for n in neigbors_tl_br(Vec2(x, y), True))
                index = int(index_string.replace(".", "0").replace("#", "1"), 2)
                new_image[Vec2(x, y)] = algorithm[index]
        image = new_image

        default = algorithm[0]

    return Counter(image.values())["#"]


def part_2(data):
    algorithm, image = data
    image: Dict

    default = "."

    for i in range(50):
        new_image = {}
        min_x = get_min_x(image.keys())
        max_x = get_max_x(image.keys())
        min_y = get_min_y(image.keys())
        max_y = get_max_y(image.keys())
        for x in range(min_x - 2, max_x + 3):
            for y in range(min_y - 2, max_y + 3):
                index_string = "".join(image.get(n, default) for n in neigbors_tl_br(Vec2(x, y), True))
                index = int(index_string.replace(".", "0").replace("#", "1"), 2)
                new_image[Vec2(x, y)] = algorithm[index]
        image = new_image

        # calc infinity default
        index_string = "".join(image.get(n, default) for n in neigbors_tl_br(Vec2(-100, -100), True))
        index = int(index_string.replace(".", "0").replace("#", "1"), 2)
        default = algorithm[index]
        print("new default:", default)

    return Counter(image.values())["#"]


def parse(lines):
    # lines = [int(l) for l in lines]

    algorithm = ""
    while line := lines.pop(0):
        algorithm += line

    image = []
    while lines and (line := lines.pop(0)):
        image.append(line)

    image_dict = {}
    for y, cs in enumerate(image):
        for x, c in enumerate(cs):
            image_dict[Vec2(x, y)] = c

    return algorithm, image_dict


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(parse(lines[:])))
    print("Falsch: 5179 (to high)")
    print("Part 2: ", part_2(parse(lines[:])))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
