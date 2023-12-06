import pytest  # noqa: F401  # pylint: disable=unused-import
import day06


DATA = """
Time:      7  15   30
Distance:  9  40  200
"""


def test_solution1():
    result = day06.solve_part1(DATA.strip())
    assert result == 288
