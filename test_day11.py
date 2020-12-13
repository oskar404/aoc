import pytest
import day11


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


def test_solution2():
    pass
