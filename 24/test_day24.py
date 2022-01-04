from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", None, None),
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


def test_example_code():
    code = Path("test_input.txt").read_text().splitlines()
    inter = solution.Interpreter(code)

    assert inter.run([8]) == dict(z=0, y=0, x=0, w=1)
