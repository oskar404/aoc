import pytest  # noqa: F401  # pylint: disable=unused-import
import utils
from day11 import solve_part1, solve_part2


TEST_DATA = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


def test_solution1():
    utils.VERBOSE = True
    assert solve_part1(TEST_DATA) == 10605
    utils.VERBOSE = False


def test_solution2():
    utils.VERBOSE = True
    assert solve_part2(TEST_DATA) == 2713310158
    utils.VERBOSE = False
