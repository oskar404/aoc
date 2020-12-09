import pytest
import day09


data = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_solution1():
    idx, val = day09.solve_part1(data, 5, True)
    assert idx == 14
    assert val == 127


def test_solution2():
    val, seq = day09.solve_part2(data, 5, True)
    print(f"sequence: {seq}")
    assert val == 62
