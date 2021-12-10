from pathlib import Path

import pytest
from pytest import param

import solution

files = [
    ("test_input.txt", 26397, 288957),
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


def test_completion():
    assert solution.complete_line("[[{{<<(<") == ">)>>}}]]"


def test_score_completion():
    assert solution.score_completion("}}]])})]") == 288957
    assert solution.score_completion(")}>]})") == 5566
    assert solution.score_completion("}}>}>))))") == 1480781
    assert solution.score_completion("]]}}]}]}>") == 995444
    assert solution.score_completion("])}>") == 294
