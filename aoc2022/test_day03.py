import pytest  # noqa: F401  # pylint: disable=unused-import
from day03 import solve_part1, solve_part2, priority


TEST_DATA = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_priority():
    assert priority("a") == 1
    assert priority("z") == 26
    assert priority("A") == 27
    assert priority("Z") == 52


def test_solution1():
    result = solve_part1(TEST_DATA)
    assert result == 157


def test_solution2():
    result = solve_part2(TEST_DATA)
    assert result == 70
