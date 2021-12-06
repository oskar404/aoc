import pytest
from aoc2020 import day08


prog = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def test_solution1():
    idx, acc = day08.solve_part1(prog)
    assert acc == 5
    assert idx == 1


def test_solution2():
    idx, acc, mdx = day08.solve_part2(prog)
    assert mdx == 7
    assert acc == 8
    assert idx == 9
