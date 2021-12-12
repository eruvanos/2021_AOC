# fmt: off
import sys
from collections import defaultdict
from typing import List, Set

sys.path.append("..")


# fmt: on

def next_paths(data, path: List[str], visited: Set[str], double_visit=False):
    cur_loc = path[-1]
    if cur_loc == "end":
        yield path, visited

    else:
        for n in data[cur_loc]:
            dbl_vst = double_visit
            if n.islower() and n in visited:
                if double_visit and n != "start":
                    dbl_vst = False
                else:
                    continue

            yield from list(next_paths(data, path + [n], visited | {n}, dbl_vst))


def part_1(data):
    print()
    all_path = list(next_paths(data, ["start"], {"start"}))
    for path, visited in all_path:
        print(",".join(path))

    return len(all_path)


def part_2(data):
    print()
    all_path = list(sorted(next_paths(data, ["start"], {"start"}, double_visit=True)))
    for path, visited in all_path:
        print(",".join(path))

    return len(all_path)


def parse(lines):
    lines = [l.split("-") for l in lines]
    grid = defaultdict(set)
    for a, b in lines:
        grid[a].add(b)
        grid[b].add(a)
    return grid


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
