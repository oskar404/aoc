import pytest
from aoc2020 import day02


def test_solution1():
    data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    result = day02.solve_part1(data)
    assert result == 2


def test_solution2():
    data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    result = day02.solve_part2(data)
    assert result == 1
