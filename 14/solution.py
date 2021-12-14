# fmt: off
import sys
from collections import Counter, defaultdict
from math import ceil

from utils.data import slice

sys.path.append("..")


# fmt: on
def step(poly, rules):
    new_poly = defaultdict(int)
    for pair, appearance in poly.items():
        for seq in rules[pair]:
            new_poly[seq] += appearance
    return new_poly


def calc_score(poly):
    counter = defaultdict(int)
    for (a, b), appearance in poly.items():
        counter[a] += appearance
        counter[b] += appearance

    return ceil(max(counter.values()) / 2) - ceil(min(counter.values()) / 2)


def part_1(data, rounds=10):
    poly, rules = data

    # steps
    for i in range(rounds):
        poly = step(poly, rules)
        print(f"Step {i + 1}: {poly}")

    # result
    return calc_score(poly)


def part_2(data):
    return part_1(data, 40)


def parse(lines):
    poly_str = lines.pop(0)
    poly = Counter(slice(poly_str, 2, 1))

    lines.pop(0)  # skip empty line

    rules = {}
    while lines and (line := lines.pop(0)):
        pair, addition = line.split(" -> ")
        rules[pair] = (pair[0] + addition, addition + pair[1])

    return poly, rules


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
