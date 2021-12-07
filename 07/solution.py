# fmt: off
import sys
from functools import lru_cache

sys.path.append("..")


# fmt: on

def calc_fuel_usage_part_1(crabs, pos):
    return sum(abs(pos - crab) for crab in crabs)


def part_1(data):
    raw = list(map(int, data[0].split(",")))

    min_fuel = max(raw) * len(raw)
    # pos = max(raw)
    for x in range(min(raw), max(raw)):
        fuel = calc_fuel_usage_part_1(raw, x)
        if fuel < min_fuel:
            min_fuel = fuel
            # pos = x

    return min_fuel


@lru_cache
def fuel_cost(crab, pos):
    return sum(range(abs(pos - crab) + 1))


def calc_fuel_usage_part_2(crabs, pos):
    return sum(fuel_cost(crab, pos) for crab in crabs)


def part_2(data):
    raw = list(map(int, data[0].split(",")))

    min_fuel = 9999999999999
    for x in range(min(raw), max(raw)):
        fuel = calc_fuel_usage_part_2(raw, x)
        if fuel < min_fuel:
            min_fuel = fuel

    # falsch: 1955000
    return min_fuel


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
