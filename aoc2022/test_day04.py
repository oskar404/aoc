import pytest  # noqa: F401  # pylint: disable=unused-import
from day04 import solve_part1, solve_part2


TEST_DATA = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_solution1():
    result = solve_part1(TEST_DATA)
    assert result == 2


def test_solution2():
    result = solve_part2(TEST_DATA)
    assert result == 4
