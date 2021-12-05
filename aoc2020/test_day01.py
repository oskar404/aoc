import pytest
import day01


def test_solution1():
    data = [1721, 979, 366, 299, 675, 1456]
    result, _, _ = day01.solve_part1(data)
    assert result == 514579


def test_solution2():
    data = [1721, 979, 366, 299, 675, 1456]
    result, _, _, _ = day01.solve_part2(data)
    assert result == 241861950
