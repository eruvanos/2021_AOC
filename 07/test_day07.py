from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 37, 168),
]


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, expected, _ in files],
)
def test_part_1(file: Path, expected):
    lines = file.read_text().splitlines()

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


@pytest.mark.parametrize(
    "crab,pos,result",
    [
        (16, 5, 66),
        (1, 5, 10),
        (2, 5, 6),
        (0, 5, 15),
        (4, 5, 1),
        (2, 5, 6),
        (7, 5, 3),
        (14, 5, 45),
    ]
)
def test_example_input_terminates(crab, pos, result):
    assert solution.fuel_cost(crab, pos) == result
