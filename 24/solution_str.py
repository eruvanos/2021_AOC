# fmt: off
import sys
from itertools import count
from typing import List, Dict, Iterable

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

    def run(self, inputs: Iterable[int]) -> Dict:
        inputs = iter(str(i) for i in inputs)
        registers = {
            w: "0",
            x: "0",
            y: "0",
            z: "0",
        }

        def param(p: str) -> str:
            return registers[p] if p in REGISTERS else p

        r_counter = count()
        for i, line in enumerate(self.code):
            match line.split():
                case "":
                    # skip empty line
                    continue
                case "#", *_:
                    continue
                case "inp", a:
                    registers[a] = next(inputs)
                    ref = f"r{next(r_counter)}"
                    registers[ref] = registers[z]
                    registers[z] = ref

                case cmd, a, b:
                    a_var = a
                    a = param(a)
                    b = param(b)

                    match cmd, a, b:
                        case "add", "0", b:
                            registers[a_var] = b

                        case "add", a, "0":
                            registers[a_var] = a

                        case "add", a, b:
                            registers[a_var] = f"({a} + {b})"

                        case "mul", a, "0":
                            registers[a_var] = f"0"

                        case "mul", "0", b:
                            registers[a_var] = f"0"

                        case "mul", a, b:
                            registers[a_var] = f"({a} * {b})"

                        case "div", a, "1":
                            registers[a_var] = a

                        case "div", "0", b:
                            registers[a_var] = f"0"

                        case "div", a, b:
                            registers[a_var] = f"({a} // {b})"

                        case "mod", "0", b:
                            registers[a_var] = "0"

                        case "mod", a, b:
                            registers[a_var] = f"({a} % {b})"

                        case "eql", a, b:
                            registers[a_var] = f"int({a} == {b})"

                        case _:
                            raise Exception(f"Unknown opp {cmd}")
        return registers


def part_1(code: List[str]):
    inter = Interpreter(code)
    regs = inter.run("abcdefghijklmn")
    print(regs)
    print()




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
