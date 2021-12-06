import pytest
from aoc2020 import day11


layout = """
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
"""


def test_solution1():
    assert day11.occupied_seats(day11.parse(layout)) == 0
    assert day11.occupied_seats(day11.parse(layout), "L") == 71
    assert day11.neighbours(day11.parse(layout), 0, 0) == 0
    assert day11.neighbours(day11.parse(layout), 0, 0, "L") == 2
    assert day11.neighbours(day11.parse(layout), 9, 9, "L") == 2
    assert day11.neighbours(day11.parse(layout), 4, 6, "L") == 6
    assert day11.neighbours(day11.parse(layout), 5, 0, "L") == 4
    assert day11.neighbours(day11.parse(layout), 6, 0, "L") == 3
    occupied, rounds = day11.solve_part1(layout, True)
    assert occupied == 37
    assert rounds == 5


data1 = """
    .......#.
    ...#.....
    .#.......
    .........
    ..#L....#
    ....#....
    .........
    #........
    ...#.....
"""

data2 = """
    .............
    .L.L.#.#.#.#.
    .............
"""

data3 = """
    .##.##.
    #.#.#.#
    ##...##
    ...L...
    ##...##
    #.#.#.#
    .##.##.
"""


def test_solution2():
    assert day11.adjacent(day11.parse(data1), 3, 4) == 8
    assert day11.adjacent(day11.parse(data2), 1, 1) == 0
    assert day11.adjacent(day11.parse(data2), 3, 1) == 1
    assert day11.adjacent(day11.parse(data3), 3, 3) == 0
    occupied, rounds = day11.solve_part2(layout, True)
    assert occupied == 26
    assert rounds == 6
