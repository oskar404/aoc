import pytest  # noqa: F401  # pylint: disable=unused-import
from day05 import solve_part1, solve_part2


TEST_DATA = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def test_solution1():
    result = solve_part1(TEST_DATA)
    assert result == "CMZ"


def test_solution2():
    result = solve_part2(TEST_DATA)
    assert result == "MCD"
