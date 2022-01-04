# fmt: off
import sys
from functools import cache
from typing import List, Dict, Iterable

from tqdm import tqdm

sys.path.append("..")

# fmt: on

REGISTERS = "wxyz"
w, x, y, z = REGISTERS


class FailedValidation(BaseException):
    def __init__(self, regs: Dict):
        self.regs = regs


class Interpreter:

    def __init__(self, code: List[str]):
        self.code = list(code)

    # def step(self, pc=0, regs: Optional[Dict] = None) -> Tuple[Dict, int]:
    #     """Executes code until next input"""
    #     if regs:
    #         regs = regs.copy()
    #     else:
    #         regs = {
    #             w: 0,
    #             x: 0,
    #             y: 0,
    #             z: 0,
    #         }
    #
    #     while pc < len(self.code):
    #         line = self.code[pc]
    #         pc += 14

    def run(self, inputs: Iterable[int]) -> Dict:
        inputs = list(int(i) for i in inputs)
        registers = {
            w: 0,
            x: 0,
            y: 0,
            z: 0,
        }

        def param(p: str) -> str:
            return registers[p] if p in REGISTERS else int(p)

        for i, line in enumerate(self.code[:]):
            match line.split():
                case "":
                    # skip empty line
                    continue
                case "#", *_:
                    continue
                case "inp", a:
                    # print(f"Next input z: {registers[z]}")
                    # if registers[z] != 0:
                    #     raise FailedValidation(registers)
                    # elif len(inputs) == 0:
                    #     return registers

                    registers[a] = inputs.pop(0)

                case cmd, a, b:
                    a_var = a
                    a = int(param(a))
                    b = int(param(b))

                    match cmd, a, b:
                        case "add", a, b:
                            registers[a_var] = a + b

                        case "mul", a, b:
                            registers[a_var] = a * b

                        case "div", a, b:
                            registers[a_var] = a // b

                        case "mod", a, b:
                            registers[a_var] = a % b

                        case "eql", a, b:
                            registers[a_var] = int(a == b)

                        case _:
                            raise Exception(f"Unknown opp {cmd}")
        # print(f"Finish with z: {registers[z]}")
        return registers


def generate_model_numbers():
    for d in reversed(range(10)):
        for e in reversed(range(10)):
            for g in reversed(range(10)):
                for h in reversed(range(10)):
                    for i in reversed(range(10)):
                        for j in reversed(range(10)):
                            for k in reversed(range(10)):
                                for l in reversed(range(10)):
                                    for m in reversed(range(10)):
                                        for n in reversed(range(10)):
                                            yield 9, 9, 9, d, e, 9, g, h, i, j, k, l, m, n


@cache
def cr5(a, b, c, d, e):
    r1 = (a + 7)
    r2 = ((r1 * 26) + (b + 8))
    r3 = ((r2 * 26) + (c + 2))
    r4 = ((r3 * 26) + (d + 11))
    return (((r4 // 26) * ((25 * int(int(((r4 % 26) - 3) == e) == 0)) + 1)) + (
            (e + 6) * int(int(((r4 % 26) - 3) == e) == 0)))


@cache
def cr8(a, b, c, d, e, f, g, h):
    r5 = cr5(a, b, c, d, e)

    r6 = ((r5 * 26) + (f + 12))
    r7 = ((r6 * 26) + (g + 14))
    return (((r7 // 26) * ((25 * int(int(((r7 % 26) - 16) == h) == 0)) + 1)) + (
            (h + 13) * int(int(((r7 % 26) - 16) == h) == 0)))


def optimized(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    # r1 = (a + 7)
    # r2 = ((r1 * 26) + (b + 8))
    # r3 = ((r2 * 26) + (c + 2))
    # r4 = ((r3 * 26) + (d + 11))
    # r5 = (((r4 // 26) * ((25 * int(int(((r4 % 26) - 3) == e) == 0)) + 1)) + (
    #         (e + 6) * int(int(((r4 % 26) - 3) == e) == 0)))
    # r5 = cr5(a, b, c, d, e)
    #
    # r6 = ((r5 * 26) + (f + 12))
    # r7 = ((r6 * 26) + (g + 14))
    # r8 = (((r7 // 26) * ((25 * int(int(((r7 % 26) - 16) == h) == 0)) + 1)) + (
    #         (h + 13) * int(int(((r7 % 26) - 16) == h) == 0)))

    r8 = cr8(a, b, c, d, e, f, g, h)
    r9 = ((r8 * 26) + (i + 15))
    r10 = (((r9 // 26) * ((25 * int(int(((r9 % 26) - 8) == j) == 0)) + 1)) + (
            (j + 10) * int(int(((r9 % 26) - 8) == j) == 0)))
    r11 = (((r10 // 26) * ((25 * int(int(((r10 % 26) - 12) == k) == 0)) + 1)) + (
            (k + 6) * int(int(((r10 % 26) - 12) == k) == 0)))
    r12 = (((r11 // 26) * ((25 * int(int(((r11 % 26) - 7) == l) == 0)) + 1)) + (
            (l + 10) * int(int(((r11 % 26) - 7) == l) == 0)))
    r13 = (((r12 // 26) * ((25 * int(int(((r12 % 26) - 6) == m) == 0)) + 1)) + (
            (m + 8) * int(int(((r12 % 26) - 6) == m) == 0)))
    return (((r13 // 26) * ((25 * int(int(((r13 % 26) - 11) == n) == 0)) + 1)) + (
            (n + 5) * int(int(((r13 % 26) - 11) == n) == 0)))


def part_1(code: List[str]):
    inter = Interpreter(code)
    for model_number in tqdm(generate_model_numbers(), total=10 ** 10):
        # regs = inter.run(model_number)[z]
        value = optimized(*model_number)
        if value == 0:
            return model_number


def part_2(data):
    pass


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
