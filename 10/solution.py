# fmt: off
import sys

sys.path.append("..")

# fmt: on

ERR_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

COMP_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def validate_line(line: str):
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(c)
        elif c in ")]}>":
            last = stack.pop()
            if last + c not in ("[]", "{}", "()", "<>"):
                return ERR_SCORE[c]
        else:
            raise Exception("Unknown char")
    return 0


def part_1(data):
    return sum(validate_line(line) for line in data)


def complete_line(line: str):
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(c)
        elif c in ")]}>":
            last = stack.pop()
            if last + c not in ("[]", "{}", "()", "<>"):
                raise Exception("Corrupted line")
        else:
            raise Exception("Unknown char")

    return "".join(reversed(stack)).replace("(", ")").replace("[", "]").replace("{", "}").replace("<", ">")


def score_completion(completion):
    score = 0
    for c in completion:
        score *= 5
        score += COMP_SCORE[c]
    return score


def part_2(data):
    scores = []
    for line in data:
        if validate_line(line) > 0:
            # skip corrupted lines
            continue

        complete_string = complete_line(line)
        scores.append(score_completion(complete_string))

    return sorted(scores)[len(scores) // 2]


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
