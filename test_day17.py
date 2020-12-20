import pytest
import day17


input1 = """
    .#.
    ..#
    ###
"""


def test_solution1():
    assert day17.solve_part1(input1, True) == 112


def test_solution2():
    pass
