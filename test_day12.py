import pytest
import day12


input = ["F10", "N3", "F7", "R90", "F11"]


def test_solution1():
    distance, _ = day12.solve_part1(input, True)
    assert distance == 251


def test_solution2():
    pass
