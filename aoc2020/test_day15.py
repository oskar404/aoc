import pytest
import day15


def test_solution1():
    assert day15.solve_puzzle([0, 3, 6], 10, True) == 0
    assert day15.solve_puzzle([0, 3, 6], 2020, True) == 436
    assert day15.solve_puzzle([1, 3, 2], 2020, True) == 1
    assert day15.solve_puzzle([2, 1, 3], 2020, True) == 10
    assert day15.solve_puzzle([1, 2, 3], 2020, True) == 27
    assert day15.solve_puzzle([2, 3, 1], 2020, True) == 78
    assert day15.solve_puzzle([3, 2, 1], 2020, True) == 438
    assert day15.solve_puzzle([3, 1, 2], 2020, True) == 1836
