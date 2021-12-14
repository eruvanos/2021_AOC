# fmt: off
import sys
from collections import Counter, defaultdict
from io import StringIO
from math import ceil

import tqdm

sys.path.append("..")


# fmt: on
def slice(text: str, chunk_size: int, overlap=0):
    while len(text) >= chunk_size:
        to_send, text = text[:chunk_size], text[chunk_size-overlap:]
        yield to_send

def part_1(data):
    poly, rules = data

    # steps
    for step in range(10):
        # poly = "".join(map(rules.__getitem__, slice(poly, 2, 1))) + poly[-1]
        new_poly = defaultdict(int)
        for pair, appearance in poly.items():
            for seq in rules[pair]:
                new_poly[seq] += appearance

        poly = new_poly
        print(f"Step {step + 1}: {poly}")

    # result
    counter = defaultdict(int)
    for (a,b), appearance in poly.items():
        counter[a] += appearance
        counter[b] += appearance

    return ceil(max(counter.values())/2) - ceil(min(counter.values())/2)


def part_2(data):
    poly, rules = data

    # steps
    for step in range(40):
        # poly = "".join(map(rules.__getitem__, slice(poly, 2, 1))) + poly[-1]
        new_poly = defaultdict(int)
        for pair, appearance in poly.items():
            for seq in rules[pair]:
                new_poly[seq] += appearance

        poly = new_poly
        print(f"Step {step + 1}: {poly}")

    # result
    counter = defaultdict(int)
    for (a, b), appearance in poly.items():
        counter[a] += appearance
        counter[b] += appearance

    return ceil(max(counter.values()) / 2) - ceil(min(counter.values()) / 2)


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
