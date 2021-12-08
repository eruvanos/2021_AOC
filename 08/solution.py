# fmt: off
import sys
from collections import defaultdict
from typing import List

sys.path.append("..")


# fmt: on

# 0 - 6
# 1 - 2 X
# 2 - 5
# 3 - 5
# 4 - 4 X
# 5 - 5
# 6 - 6
# 7 - 3 X
# 8 - 7 X
# 9 - 6

def part_1(data):
    counter = 0
    for line in data:
        raw_in, raw_out = line.split(" | ")
        _out: List[str] = raw_out.split()

        for o in _out:
            if len(o) in (2, 4, 3, 7):
                counter += 1
    return counter


def solve(words: List[str]):
    # group by length
    len_words = defaultdict(set)
    for word in words:
        len_words[len(word)].add("".join(sorted(word)))

    options = {
        0: len_words[6],
        1: len_words[2],
        2: len_words[5],
        3: len_words[5],
        4: len_words[4],
        5: len_words[5],
        6: len_words[6],
        7: len_words[3],
        8: len_words[7],
        9: len_words[6]
    }

    # resolve obvious ones
    key = {k: words.pop() for k, words in options.items() if len(words) == 1}
    assert 8 in key

    # resolve 3
    for word in len_words[5]:
        if len(set(word) - set(key[1])) == 3:
            key[3] = word
            len_words[5].remove(word)
            break

    # resolve 5
    for word in len_words[5]:
        if len(set(word) - set(key[4])) == 2:
            key[5] = word
            len_words[5].remove(word)
            break

    # resolve 2
    assert len(len_words[5]) == 1
    key[2] = len_words[5].pop()

    # resolve 9
    for word in len_words[6]:
        if len(set(word) - set(key[4])) == 2:
            key[9] = word
            len_words[6].remove(word)
            break

    # resolve 6
    for word in len_words[6]:
        if len(set(word) - set(key[5])) == 1:
            key[6] = word
            len_words[6].remove(word)
            break

    # resolve 0
    assert len(len_words[6]) == 1
    key[0] = len_words[6].pop()

    # reverse key map
    return {"".join(sorted(v)): k for k, v in key.items()}


def part_2(data):
    result = 0
    for line in data:
        raw_in, raw_out = line.split(" | ")
        _in: List[str] = raw_in.split()
        _out: List[str] = raw_out.split()

        key = solve(_in + _out)
        # key: word -> number

        result += int("".join(str(key["".join(sorted(word))]) for word in _out))

    return result


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
