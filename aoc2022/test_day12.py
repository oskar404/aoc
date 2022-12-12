import pytest  # noqa: F401  # pylint: disable=unused-import
import utils
from day12 import solve_part1, solve_part2


MAP = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def test_solution1():
    with utils.verbose():
        assert solve_part1(MAP) == 31


def test_solution2():
    with utils.verbose():
        # just a template for testing
        assert solve_part2(MAP)
