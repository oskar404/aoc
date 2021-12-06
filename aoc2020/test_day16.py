import pytest
from aoc2020 import day16


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


input2 = """
    class: 0-1 or 4-19
    row: 0-5 or 8-19
    seat: 0-13 or 16-19

    your ticket:
    11,12,13

    nearby tickets:
    3,9,18
    15,1,5
    5,14,9
"""


def test_solution2():
    ticket = day16.parse_ticket(input2, True)
    assert ticket["class"] == 12
    assert ticket["row"] == 11
    assert ticket["seat"] == 13
