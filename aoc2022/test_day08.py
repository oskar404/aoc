import pytest  # noqa: F401  # pylint: disable=unused-import
from day08 import solve_part1, solve_part2

TEST_DATA = """
30373
25512
65332
33549
35390
"""


def test_solution1():
    assert solve_part1(TEST_DATA) == 21


def test_solution2():
    assert solve_part2(TEST_DATA) == 8
