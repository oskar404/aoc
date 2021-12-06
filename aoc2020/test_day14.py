import pytest
from aoc2020 import day14


input1 = """
    mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0
"""


def test_solution1():
    code = day14.solve_part1(input1, True)
    assert code == 165


input2 = """
    mask = 000000000000000000000000000000X1001X
    mem[42] = 100
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1
"""


def test_solution2():
    code = day14.solve_part2(input2, True)
    assert code == 208
