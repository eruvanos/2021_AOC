# fmt: off
import sys

sys.path.append("..")


# fmt: on


def part_1(data):
    bits = [0] * len(data[0])

    for row in data:
        for i, c in enumerate(row):
            if c == "1":
                bits[i] += 1

    gamma = ""
    epsilon = ""
    for b in bits:
        gamma += "1" if b > len(data) // 2 else "0"
        epsilon += "0" if b > len(data) // 2 else "1"

    return int(gamma, 2) * int(epsilon, 2)


def calc_most_common(data, bit):
    dx = "".join(bits[bit] for bits in data)
    return "1" if dx.count("1") >= len(dx) / 2 else "0"


def part_2(data):
    print()
    bits = [0] * len(data[0])

    for row in data:
        for i, c in enumerate(row):
            if c == "1":
                bits[i] += 1

    o2_data = data[:]
    for i in range(len(o2_data)):
        most_common = calc_most_common(o2_data, i)
        o2_data = list(filter(lambda d: d[i] == most_common, o2_data))
        # print(f"{o2_data=}, {most_common=}")
        if len(o2_data) == 1:
            o2_data = o2_data[0]
            break

    co2_data = data[:]
    for i, b in enumerate(bits):
        most_common = calc_most_common(co2_data, i)
        co2_data = list(filter(lambda d: d[i] != most_common, co2_data))
        # print(f"{co2_data=}, !{most_common=}")
        if len(co2_data) == 1:
            co2_data = co2_data[0]
            break

    return int(o2_data, 2) * int(co2_data, 2)


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
