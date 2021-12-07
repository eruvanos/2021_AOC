# fmt: off
import sys
from typing import Callable, List

import uniplot

sys.path.append("..")


# fmt: on


def find_minimal_fuel_cost(crabs: List[int], cost_func: Callable, debug=False):
    """
    :param debug: does not stop at minima, plots the whole curve
    """
    values = {}
    min_fuel = 9999999999999
    for x in range(min(crabs), max(crabs)):
        fuel = sum(cost_func(crab, x) for crab in crabs)
        if debug:
            values[x] = fuel

        if fuel < min_fuel:
            min_fuel = fuel
        elif not debug:
            break

    if debug:
        uniplot.plot(xs=list(values.keys()), ys=list(values.values()))

    return min_fuel


def part_1(data):
    crabs = list(map(int, data[0].split(",")))

    def fuel_cost(crab, pos):
        return abs(pos - crab)

    return find_minimal_fuel_cost(crabs, fuel_cost, debug=False)


def part_2(data):
    crabs = list(map(int, data[0].split(",")))

    def fuel_cost(crab, pos):
        return sum(range(abs(pos - crab) + 1))

    return find_minimal_fuel_cost(crabs, fuel_cost)


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
