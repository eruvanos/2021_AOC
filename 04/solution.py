# fmt: off
import sys
from io import StringIO

from termcolor import colored

sys.path.append("..")


# fmt: on

class Card:
    def __init__(self, card_name=""):
        self.numbers = []
        self.marked_index = set()
        self.card_name = card_name

    def add(self, row):
        self.numbers.extend(row)

    def pick(self, number):
        if number in set(self.numbers):
            index = self.numbers.index(number)
            self.marked_index.add(index)

    @property
    def won(self):
        # check rows
        for r in range(5):
            r = r * 5
            indexes = {r, r + 1, r + 2, r + 3, r + 4}
            if self.marked_index.issuperset(indexes):
                return indexes

        # check columns
        for r in range(5):
            indexes = {r, r + 5, r + 10, r + 15, r + 20}
            if self.marked_index.issuperset(indexes):
                return indexes

        return False

    def score(self, last_num):
        unmarked = set(self.numbers) - {self.numbers[index] for index in self.marked_index}
        return last_num * sum(unmarked)

    def print(self):
        print("Card:", self.card_name)
        print("Win index:", self.won)
        print(self)

    def __str__(self):
        buffer = StringIO()
        for i, n in enumerate(self.numbers):
            if i and i % 5 == 0:
                print(file=buffer)

            print(colored(f"{n:02}", "red") if i in self.marked_index else f"{n:02}", end=" ", file=buffer)
        return buffer.getvalue()


def part_1(data: list):
    numbers = map(int, data.pop(0).split(","))

    cards = []
    last_card = None
    for line in data:
        if not line:
            last_card = Card(card_name=str(len(cards)))
            cards.append(last_card)
            continue

        last_card.add(list(map(int, line.split())))

    # search winning board
    for number in numbers:
        print(f"pick number: {number}")
        for card in cards:
            card.pick(number)
            if card.won:
                winner_card = card
                break
        else:
            continue

        break

    # debug
    # for card in cards:
    #     print("----------------")
    #     card.print()
    # card.print()

    # return cald score
    return winner_card.score(number)


def part_2(data):
    numbers = map(int, data.pop(0).split(","))

    cards = []
    last_card = None
    for line in data:
        if not line:
            last_card = Card(card_name=str(len(cards)))
            cards.append(last_card)
            continue

        last_card.add(list(map(int, line.split())))

    # search winning board
    for number in numbers:
        print(f"pick number: {number}")
        for card in cards[:]:
            card.pick(number)
            if card.won:
                cards.remove(card)

                if len(cards) == 0:
                    winner_card = card
                    break
        else:
            continue

        break

    # debug
    # for card in cards:
    #     print("----------------")
    #     card.print()
    # card.print()

    # return cald score
    return winner_card.score(number)


def parse(lines):
    # lines = [int(l) for l in lines]
    return lines


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    # wrong: 57375
    print("Part 1: ", part_1(parse(lines[:])))
    print("Part 2: ", part_2(parse(lines[:])))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
