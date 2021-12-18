from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input_1.txt", 3488, None),
    ("test_input_2.txt", 4140, None),
]


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, expected, _ in files],
)
def test_part_1(file: Path, expected):
    lines = file.read_text().splitlines()

    print()
    result = solution.part_1(solution.parse(lines))
    assert result == expected


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, _, expected in files],
)
def test_part_2(file: Path, expected):
    lines = file.read_text().splitlines()

    result = solution.part_2(solution.parse(lines))
    assert result == expected


@pytest.mark.parametrize("given,expected", [
    ([[[[[9, 8], 1], 2], 3], 4], "[[[[0,9],2],3],4]"),
    ([7, [6, [5, [4, [3, 2]]]]], "[7,[6,[5,[7,0]]]]"),
    ([[6, [5, [4, [3, 2]]]], 1], "[[6,[5,[7,0]]],3]"),
    ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
    ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
])
def test_explode(given, expected):
    node = solution.Node.read(given)
    assert repr(node.explode()) == expected


def test_reduce():
    data = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
    assert repr(solution.reduce(data)) == "[[[[5,0],[7,4]],[5,5]],[6,6]]"


@pytest.mark.parametrize("task,expected", [
    param(([9, 1]), 29, id="29"),
    param(([1, 9]), 21, id="21"),
    param(([[9, 1], [1, 9]]), 129, id="129"),
    param(([[1, 2], [[3, 4], 5]]), 143, id="143"),
    param(([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]), 1384, id="1384"),
    param(([[[[1, 1], [2, 2]], [3, 3]], [4, 4]]), 445, id="445"),
    param(([[[[3, 0], [5, 3]], [4, 4]], [5, 5]]), 791, id="791"),
    param(([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]), 1137, id="1137"),
    param(([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]), 3488, id="3488"),
])
def test_magnitude(task, expected):
    assert solution.magnitude(task) == expected


def test_addition():
    result = solution.Node.read([[[[4, 3], 4], 4], [7, [[8, 4], 9]]]) + solution.Node.read([1, 1])
    assert repr(result) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

def test_addition_complex():
    result = solution.Node.read([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]) + solution.Node.read([7,[[[3,7],[4,3]],[[6,3],[8,8]]]])
    assert repr(result) == "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"