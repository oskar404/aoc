import pytest
import day05


data = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
seat_ids = [567, 119, 820]


def test_solution1():
    result, ids = day05.solve_part1(data)
    assert result == 820
    for i, v in enumerate(ids):
        assert seat_ids[i] == v


def test_solution2():
    pass
