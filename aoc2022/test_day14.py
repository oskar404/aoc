import pytest  # noqa: F401  # pylint: disable=unused-import
import utils
from day14 import solve_part1, solve_part2


WALLS = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def test_solution1():
    with utils.verbose():
        assert solve_part1(WALLS) == 24


def test_solution2():
    with utils.verbose():
        assert solve_part2(WALLS) == 93
