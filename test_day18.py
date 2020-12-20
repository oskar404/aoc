import pytest
import day18


test_vectors = [
    ["1 + 2 * 3 + 4 * 5 + 6", 71],
    ["1 + (2 * 3) + (4 * (5 + 6))", 51],
    ["2 * 3 + (4 * 5)", 26],
    ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 437],
    ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240],
    ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632],
]


def test_solution1():
    for t in test_vectors:
        assert day18.solve_part1(t[0], True) == t[1]


def test_solution2():
    pass
