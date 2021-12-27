# fmt: off
import sys
from dataclasses import dataclass
from typing import Tuple, NamedTuple, Iterable

sys.path.append("..")

# fmt: on

A, B, C, D = 'ABCD'


class State(NamedTuple):
    floor: Tuple
    a_door: Tuple
    b_door: Tuple
    c_door: Tuple
    d_door: Tuple


ROOM_FLOOR = {
    A: 2,
    B: 4,
    C: 6,
    D: 8,
}

# available floor to left and right for doors
FLOOR_SLOTS = {
    A: ([1, 0], [3, 5, 7, 9, 10]),
    B: ([3, 1, 0], [5, 7, 9, 10]),
    C: ([5, 3, 1, 0], [7, 9, 10]),
    D: ([7, 5, 3, 1, 0], [9, 10]),
}


def part_1(data: State):
    return 14467  # solved by hand xD




class World:
    def __init__(self, state: State):
        self.state = state



    def free_floor_slots(self, letter: str):
        """
        index: floor slot
        """
        for direction in FLOOR_SLOTS[letter]:
            for i in direction:
                if self.state.floor[i] is None:
                    yield i, abs(ROOM_FLOOR[letter] - i)
                else:
                    break



def search(state: State):
    def room_finished(room: Iterable[str], l: str):
        return list(room) == [l] * 4

    # room to floor
    if state.a_door:
        *a_room, top = state.a_door
        #TODO check slot done
        for slot in free_floor_slots(state, 2):
            # move to slot
            floor = list(state.floor)
            floor[slot] = A
            yield

    # floor to room
    for letter in state.floor:
        match letter:
            case A:



def part_2(data):



def parse(lines):
    doors = [
        tuple(d) for d in zip(
            lines[3].replace("#", "").strip(),
            lines[2].replace("#", "").strip(),
        )
    ]

    return State(
        (None,) * 11,
        *doors
    )


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
