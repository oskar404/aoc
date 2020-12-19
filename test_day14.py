import pytest
import day14


input = """
    mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0
"""


def test_solution1():
    code = day14.solve_part1(input, True)
    assert code == 165


def test_solution2():
    pass
