# fmt: off
import sys
from itertools import cycle
from typing import NamedTuple

sys.path.append("..")


# fmt: on


def part_1(data):
    p1, p2 = data

    p1_score = 0
    p2_score = 0

    dice = cycle(range(1, 101))
    rolls = 0

    while True:
        # turn p1
        d1, d2, d3 = next(dice), next(dice), next(dice)
        p1 += d1 + d2 + d3
        print(f"Player 1 {d1}, {d2}, {d3} -> {p1} ({p1_score=}")

        rolls += 3
        while p1 > 10:
            p1 -= 10
        p1_score += p1

        if p1_score >= 1000:
            break

        # turn p2
        d1, d2, d3 = next(dice), next(dice), next(dice)
        p2 += d1 + d2 + d3
        print(f"Player 2 {d1}, {d2}, {d3} -> {p2} ({p1_score=}")
        rolls += 3
        while p2 > 10:
            p2 -= 10
        p2_score += p2
        if p2_score >= 1000:
            break

    print(f"End {rolls=}, {min(p1_score, p2_score)}")
    return min(p1_score, p2_score) * rolls


class State(NamedTuple):
    p1: int
    p2: int
    s1: int
    s2: int
    universes: int
    p1_turn: bool


def calc_step(state: State, step, splits):
    pos = state.p1 if state.p1_turn else state.p2
    pos += step
    pos = pos if pos <= 10 else pos - 10

    if state.p1_turn:
        return state._replace(p1=pos, s1=state.s1 + pos, p1_turn=not state.p1_turn,
                              universes=state.universes * splits)
    else:
        return state._replace(p2=pos, s2=state.s2 + pos, p1_turn=not state.p1_turn,
                              universes=state.universes * splits)


def generate_paths(state: State, depth=0):
    if state.s1 >= 21 or state.s2 >= 21:
        yield state
    else:
        yield from generate_paths(calc_step(state, 3, 1), depth=depth + 1)
        yield from generate_paths(calc_step(state, 4, 3), depth=depth + 1)
        yield from generate_paths(calc_step(state, 5, 6), depth=depth + 1)
        yield from generate_paths(calc_step(state, 6, 7), depth=depth + 1)
        yield from generate_paths(calc_step(state, 7, 6), depth=depth + 1)
        yield from generate_paths(calc_step(state, 8, 3), depth=depth + 1)
        yield from generate_paths(calc_step(state, 9, 1), depth=depth + 1)


def part_2(data):
    p1, p2 = data

    p1_wins = 0
    p2_wins = 0

    for i, state in enumerate(generate_paths(State(p1, p2, 0, 0, 1, True))):
        if i % 10000000 == 0:
            print(f"state {i}, {p1_wins=}, {p2_wins=}")

        if state.p1_turn:
            # p1 would be next, but p2 already won
            p2_wins += state.universes
        else:
            p1_wins += state.universes

    print(f"Total calculatet states: {i}")
    return max(p1_wins, p2_wins)


# expected: 444356092776315
# actual:    67597267014647

def parse(lines):
    lines = [int(l.split(": ")[1]) for l in lines if l]
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
