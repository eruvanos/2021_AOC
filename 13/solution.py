# fmt: off
import sys

from utils.vector import Vec2

sys.path.append("..")


# fmt: on

def print_grid(dots, empty_char="."):
    max_x = max(x for x, _ in dots) + 1
    max_y = max(y for _, y in dots) + 1

    for y in range(max_y):
        for x in range(max_x):
            print("#" if (x, y) in dots else empty_char, end="")
        print("")


def fold(dots, axis, place):
    def fold_y(dot):
        x, y = dot
        y = 2 * place - y if y > place else y
        return x, y

    def fold_x(dot):
        x, y = dot
        x = 2 * place - x if x > place else x
        return x, y

    fold_func = fold_x if axis == "x" else fold_y

    return set(map(fold_func, dots))


def part_1(data):
    dots, folds = data

    # fold
    for axis, place in folds[:1]:
        dots = fold(dots, axis, place)

        # print(f"{axis=}, {place=}")
        # print_grid(dots)

    return len(dots)


def part_2(data):
    dots, folds = data

    # fold
    for axis, place in folds:
        dots = fold(dots, axis, place)

    print("="*20)
    print("Code part 2")
    print_grid(dots, empty_char=" ")
    print("="*20)

    return len(dots)


def parse(lines):
    dots = set()
    while line := lines.pop(0):
        x, y = line.split(",")
        dots.add(Vec2(int(x), int(y)))

    folds = []
    while lines and (line := lines.pop(0)):
        axis, value = line.replace("fold along ", "").split("=")
        folds.append((axis, int(value)))
    return dots, folds


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
