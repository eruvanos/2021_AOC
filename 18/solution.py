# fmt: off
import sys
from ast import literal_eval
from itertools import permutations
from math import ceil
from typing import List, Optional, Iterable, Tuple

sys.path.append("..")


# fmt: on

class BaseNode:
    parent: Optional["BaseNode"]

    def walk(self, depth=0) -> Iterable[Tuple["Leaf", int]]:
        raise NotImplementedError

    def magnitude(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    def __add__(self, other):
        node = Node(self, other)
        self.parent = node
        other.parent = node
        return node.reduce()


class Leaf(BaseNode):
    def __init__(self, value: int, parent=None):
        self.parent = parent
        self.value = value

    def walk(self, depth=0):
        yield self, depth

    def reduce(self):
        return self

    def magnitude(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Node(BaseNode):
    def __init__(self, x: BaseNode, y: BaseNode, parent=None):
        self.parent = parent
        self.x = x
        self.y = y

        # update parent relation
        self.x.parent = self
        self.y.parent = self

    def find_exploding(self) -> Optional["Node"]:
        for node, depth in self.walk():
            if depth == 4:
                assert isinstance(node, Node)
                return node

        return None

    def explode(self):
        exploding = self.find_exploding()
        if exploding is None:
            return None

        leaves = list(self.walk())
        # TODO fix comparison (causes infinit recursion due to parent.child comparison)
        explode_index = leaves.index(exploding.x)
        # for i, l in enumerate(leaves):
        #     if id(l) == id(exploding.x):
        #         break
        # else:
        #     raise "Unexpected"
        # explode_index = i

        if explode_index > 0:
            leaves[explode_index - 1].value += exploding.x.value
        if explode_index + 2 < len(leaves):
            leaves[explode_index + 2].value += exploding.y.value

        parent = exploding.parent
        new_leaf = Leaf(0, parent=parent)
        if parent.x == exploding:
            parent.x = new_leaf
        else:
            parent.y = new_leaf

        return self

    def find_splitting(self):
        leaves = list(self.walk())
        for leaf in leaves:
            if leaf.value >= 10:
                return leaf

        return None

    def split(self):
        leaf = self.find_splitting()
        if leaf is None:
            return None

        parent = leaf.parent
        split_node = Node(
            Leaf(leaf.value // 2),
            Leaf(ceil(leaf.value / 2)),
            parent=parent
        )

        if parent.x == leaf:
            parent.x = split_node
        else:
            parent.y = split_node

        return self

    def reduce(self):
        node = self.explode()
        if node:
            return node.reduce()

        node = self.split()
        if node:
            return node.reduce()

        return self

    def __repr__(self):
        return f"[{self.x},{self.y}]"

    def walk(self, depth=0):
        yield from self.x.walk(depth + 1)
        yield from self.y.walk(depth + 1)

    def magnitude(self):
        return 3 * self.x.magnitude() + 2 * self.y.magnitude()

    @staticmethod
    def read(l: List):
        match l:
            case x, y:
                x_node = Node.read(x)
                y_node = Node.read(y)
                node = Node(x_node, y_node)

                x_node.parent = node
                y_node.parent = node

                return node
            case i:
                return Leaf(i)


def magnitude(num: List | int):
    if isinstance(num, int):
        return num

    a, b = num
    return 3 * magnitude(a) + 2 * magnitude(b)


def reduce(data: List):
    result = Node.read(data[0])
    print(result)
    for d in data[1:]:
        result = result + Node.read(d)
        print(result)
    return result


def part_1(data):
    return reduce(data).magnitude()


def part_2(data):
    max_mag = 0
    for a, b in permutations(data, 2):
        max_mag = max((Node.read(a) + Node.read(b)).magnitude(), max_mag)

    return max_mag


def parse(lines):
    lines = [literal_eval(l) for l in lines]
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
