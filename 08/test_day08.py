from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 26, 61229),
]


@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, expected, _ in files],
)
def test_part_1(file: Path, expected):
    lines = file.read_text().splitlines()

    result = solution.part_1(solution.parse(lines))
    assert result == expected

def test_resolve():
    sequence = ["acedgfb","cdfbe","gcdfa","fbcad","dab","cefabd","cdfgeb","eafb","cagedb","ab",]
    out = ["cdfeb","fcadb","cdfeb","cdbaf"]

    assert solution.solve(sequence + out)["ab"] == 1

@pytest.mark.parametrize(
    "file,expected",
    [param(Path(file), expected, id=file) for file, _, expected in files],
)
def test_part_2(file: Path, expected):
    lines = file.read_text().splitlines()

    result = solution.part_2(solution.parse(lines))
    assert result == expected