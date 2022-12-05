import pytest  # noqa: F401  # pylint: disable=unused-import
import day01


TEST_DATA = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_solution1():
    result = day01.solve_part1(TEST_DATA)
    assert result == 24000


def test_solution2():
    result = day01.solve_part2(TEST_DATA)
    assert result == 45000
