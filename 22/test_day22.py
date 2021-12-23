from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    # ("test_input_1.txt", 39, None),
    # ("test_input_2.txt", 590784, None),
    ("test_input_3.txt", 1, None),
]


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, expected, _ in files],
)
def test_part_1(file: Path, expected, capsys):
    lines = file.read_text().splitlines()

    with capsys.disabled():
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


def test_intersection():
    c1 = solution.Cube(10, 20, 10, 20, 10, 20)
    c2 = solution.Cube(15, 25, 15, 25, 15, 25)
    assert c1.intersection(c2) == solution.Cube(15, 20, 15, 20, 15, 20)


def test_intersection_non_overlap():
    c1 = solution.Cube(10, 20, 10, 20, 10, 20)
    c2 = solution.Cube(20, 25, 20, 25, 20, 25)
    assert c1.intersection(c2) is None
