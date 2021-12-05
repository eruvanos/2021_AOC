from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 5, 12),
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


def test_line_coordinates_upright_degree():
    result = solution.generate_line_coordinates(1, 1, 3, 3)
    assert result == [(1, 1), (2, 2), (3, 3), ]


def test_line_coordinates_up():
    result = solution.generate_line_coordinates(1, 1, 1, 3)
    assert result == [(1, 1), (1, 2), (1, 3), ]


def test_line_coordinates_upright():
    result = solution.generate_line_coordinates(1, 1, 3, 3)
    assert result == [(1, 1), (2, 2), (3, 3), ]


def test_line_coordinates_right():
    result = solution.generate_line_coordinates(1, 1, 3, 1)
    assert result == [(1, 1), (2, 1), (3, 1), ]


def test_line_coordinates_downright():
    result = solution.generate_line_coordinates(1, 0, 0, 1)
    assert result == [(0, 1), (1, 0), ]


def test_line_coordinates_right_reverse():
    result = solution.generate_line_coordinates(3, 1, 1, 1)
    assert result == [(1, 1), (2, 1), (3, 1), ]


def test_line_coordinates_down_right_1():
    result = solution.generate_line_coordinates(5, 5, 8, 2)
    assert result == [(5, 5), (6, 4), (7, 3), (8, 2)]


@pytest.mark.parametrize(
    "x1,y1,x2,y2,expected",
    [
        (0, 9, 5, 9, []),
        (8, 0, 0, 8, []),
        (9, 4, 3, 4, []),
        (2, 2, 2, 1, []),
        (7, 0, 7, 4, []),
        (6, 4, 2, 0, []),
        (0, 9, 2, 9, []),
        (3, 4, 1, 4, []),
        (0, 0, 8, 8, []),
        (5, 5, 8, 2, []),
    ]
)
def test_example_input_terminates(x1, y1, x2, y2, expected):
    result = solution.generate_line_coordinates(x1, y1, x2, y2)
