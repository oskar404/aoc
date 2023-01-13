import pytest  # noqa: F401  # pylint: disable=unused-import
import utils
from day15 import Coord, stress_signal_candidates
from day15 import solve_part1, solve_part2


DATA = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


def test_solution1():
    with utils.verbose():
        assert solve_part1(DATA, y=10) == 26


def test_candidates():
    with utils.verbose():
        distances = {Coord(5, 5): 4}
        assert len(stress_signal_candidates(distances, 0, 20)) == 20


def test_solution2():
    with utils.verbose():
        assert solve_part2(DATA, 0, 20) == 56000011
