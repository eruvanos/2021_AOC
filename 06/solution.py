# fmt: off
import sys
from collections import Counter, defaultdict

sys.path.append("..")


# fmt: on

def tick(sim):
    for i in range(80):
        next_sim_state = defaultdict(int)
        for days, fishes in sim.items():
            match days:
                case 0:
                    next_sim_state[6] += fishes
                    next_sim_state[8] += fishes
                case _:
                    next_sim_state[days - 1] += fishes
    return next_sim_state


def part_1(data):
    raw = map(int, data[0].split(","))

    sim = Counter(raw)
    for _ in range(80):
        sim = tick(sim)

    return sum(sim.values())


def part_2(data):
    raw = map(int, data[0].split(","))

    sim = Counter(raw)
    for _ in range(256):
        sim = tick(sim)

    return sum(sim.values())


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
