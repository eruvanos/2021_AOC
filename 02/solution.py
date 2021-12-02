# fmt: off
import sys

sys.path.append("..")


# fmt: on

def part_1(data):
    x = y = 0

    for line in data:
        cmd, param = line.split()
        param = int(param)
        match cmd:
            case "forward":
                x += param
            case "down":
                y += param
            case "up":
                y -= param

    return x * y


def part_2(data):
    x = y = aim = 0

    for line in data:
        cmd, param = line.split()
        param = int(param)

        match cmd:
            case "forward":
                x += param
                y += aim * param
            case "down":
                aim += param
            case "up":
                aim -= param

    return x * y


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
