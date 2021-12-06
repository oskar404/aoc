import pytest
import day01


def test_solution1():
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    result = day01.solve_part1(data)
    assert result == 7


def test_solution2():
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    result = day01.solve_part2(data)
    assert result == 5
