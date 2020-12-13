import pytest
import day13


input = """
    939
    7,13,x,x,59,x,31,19
"""


def test_solution1():
    code, bus, wait = day13.solve_part1(input, True)
    assert code == 295
    assert bus == 59
    assert wait == 5


def test_solution2():
    pass
