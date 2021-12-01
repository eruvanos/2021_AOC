def part_1(data):
    last = data[0]
    counter = 0
    for x in data:
        if last < x:
            counter += 1

        last = x

    return counter


def part_2(data):
    last = 99999999999
    counter = 0
    for x in range(len(data) - 2):
        new_window = sum(data[x:x + 3])

        if new_window > last:
            counter += 1

        last = new_window

    return counter


def main(puzzle_input_f):
    lines = [int(l.strip()) for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(lines))
    print("Part 2: ", part_2(lines))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
