import pytest
import day06


sample1 = """
abcx
abcy
abcz
"""


sample2 = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def test_solution1():
    assert day06.solve_part1(sample1) == 6
    assert day06.solve_part1(sample2) == 11


def test_solution2():
    pass
