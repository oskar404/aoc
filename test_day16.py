import pytest
import day16


input1 = """
    class: 1-3 or 5-7
    row: 6-11 or 33-44
    seat: 13-40 or 45-50

    your ticket:
    7,1,14

    nearby tickets:
    7,3,47
    40,4,50
    55,2,20
    38,6,12
"""


def test_solution1():
    assert day16.solve_part1(input1, True) == 71


def test_solution2():
    pass
