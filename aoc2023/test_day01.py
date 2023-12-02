import pytest  # noqa: F401  # pylint: disable=unused-import
import day01


DATA1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

DATA2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def test_solution1():
    result = day01.solve_part1(DATA1.strip())
    assert result == 142


def test_solution2():
    result = day01.solve_part2(DATA2.strip())
    assert result == 281
