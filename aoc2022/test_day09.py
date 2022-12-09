import pytest  # noqa: F401  # pylint: disable=unused-import
from day09 import solve_part1, solve_part2

TEST_DATA1 = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

TEST_DATA2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


def test_solution1():
    assert solve_part1(TEST_DATA1) == 13


def test_solution2():
    assert solve_part2(TEST_DATA1) == 1
    assert solve_part2(TEST_DATA2) == 36
