# fmt: off
import sys
from dataclasses import dataclass
from io import StringIO
from math import prod
from typing import List

sys.path.append("..")

# fmt: on

HEX_BYTE = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


@dataclass
class Package:
    version: int
    type: int

    def eval(self):
        return eval(repr(self), globals(), dict(prod=prod))


@dataclass
class GroupPackage(Package):
    subs: List[Package]

    def __repr__(self):
        match self.type:
            case 0:
                return f"sum({self.subs})"
            case 1:
                return f"prod({self.subs})"
            case 2:
                return f"min({self.subs})"
            case 3:
                return f"max({self.subs})"
            case 5:
                a, b = self.subs
                return f"int({a}>{b})"
            case 6:
                a, b = self.subs
                return f"int({a}<{b})"
            case 7:
                a, b = self.subs
                return f"int({a}=={b})"


@dataclass
class DecimalPackage(Package):
    value: int

    def __repr__(self):
        return str(self.value)


def decode_decimal(code: StringIO) -> int:
    data = ""
    while True:
        cnt_bit = code.read(1)
        data += code.read(4)
        if cnt_bit == "0":
            break
    return int(data, 2)


def decode(code: StringIO) -> Package:
    pkg_version = int(code.read(3), 2)
    pkg_type = int(code.read(3), 2)

    match pkg_type:
        case 4:
            return DecimalPackage(pkg_version, pkg_type, decode_decimal(code))
        case _:
            mode_bit = code.read(1)
            if mode_bit == "0":
                data_length = int(code.read(15), 2)
                subs = []
                start = code.tell()
                while code.tell() - start < data_length:
                    subs.append(decode(code))

                return GroupPackage(pkg_version, pkg_type, subs)
            else:
                pkgs_to_read = int(code.read(11), 2)
                subs = []
                for _ in range(pkgs_to_read):
                    subs.append(decode(code))

                return GroupPackage(pkg_version, pkg_type, subs)


def part_1(code):
    def walk(pkg: Package):
        yield pkg
        if isinstance(pkg, GroupPackage):
            for sub in pkg.subs:
                yield from walk(sub)

    pkg = decode(code)
    return sum(map(lambda p: p.version, walk(pkg)))


def part_2(code):
    return decode(code).eval()


def parse(lines):
    # lines = [int(l) for l in lines]
    return StringIO("".join(HEX_BYTE[l] for l in lines[0]))


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
