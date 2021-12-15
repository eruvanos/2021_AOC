from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 40, 315),
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


def test_grid():
    graph = solution.MyGraph({(0, 0): 8}, scale=5)
    solution.print_grid(graph.data, set())
    assert graph.data[(4, 4)] == 7
