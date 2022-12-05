import pytest  # noqa: F401  # pylint: disable=unused-import
import day02


TEST_DATA = """
A Y
B X
C Z
"""


def test_solution1():
    result = day02.solve_part1(TEST_DATA)
    assert result == 15


def test_solution2():
    result = day02.solve_part2(TEST_DATA)
    assert result == 12
