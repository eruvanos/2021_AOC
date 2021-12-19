from pathlib import Path

import pytest
from pytest import param

import solution
from utils.vector import Vec3

files = [
    ("test_input_2d.txt", 3, None, 3),
    ("test_input_3d.txt", 6, None, 6),
    ("test_input_3d_huge.txt", 79, 3621, 12),
]


@pytest.mark.parametrize(
    "file,expected,overlap",
    [param(Path(file), expected, overlap, id=file) for file, expected, _, overlap in files],
)
def test_part_1(file: Path, expected, overlap, capsys):
    with capsys.disabled():
        lines = file.read_text().splitlines()

        result = solution.part_1(solution.parse(lines), overlap)
        assert result == expected


@pytest.mark.parametrize(
    "file,expected,overlap",
    [param(Path(file), expected, overlap, id=file) for file, _, expected, overlap in files],
)
def test_part_2(file: Path, expected, overlap):
    lines = file.read_text().splitlines()

    result = solution.part_2(solution.parse(lines), overlap=overlap)
    assert result == expected


def test_directions(capsys):
    with capsys.disabled():
        print()
        all = {t.pop() for t in solution.geneate_24_transformations({Vec3(1, 2, 3)})}
        assert all == {
            Vec3(1, 2, 3)
        }

    assert len({t.pop for t in solution.geneate_24_transformations({Vec3(5, 6, -4)})}) == 24
