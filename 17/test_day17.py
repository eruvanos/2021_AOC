from pathlib import Path

import pytest
from pytest import param

import solution
from utils.vector import Vec2

files = [
    ("test_input.txt", 45, 112),
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


def test_simulation():
    assert solution.simulate(Vec2(6, 3), (20, 30, -10, -5))[0]
    assert solution.simulate(Vec2(9, 0), (20, 30, -10, -5))[0]
    assert not solution.simulate(Vec2(17, -4), (20, 30, -10, -5))[0]
