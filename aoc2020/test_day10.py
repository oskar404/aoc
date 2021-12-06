import pytest
from aoc2020 import day10


adapters_1 = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4,
]

adapters_2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]


def test_solution1():
    assert day10.solve_part1(adapters_1, True) == 35
    assert day10.solve_part1(adapters_2, True) == 220


def test_solution2():
    assert day10.permutate(1) == 2
    assert day10.permutate(2) == 4
    assert day10.permutate(3) == 7
    assert day10.permutate(4) == 13
    assert day10.solve_part2(adapters_1, True) == 8
    assert day10.solve_part2(adapters_2, True) == 19208
