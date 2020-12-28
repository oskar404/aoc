import pytest
import day19


input1 = """
    0: 4 1 5
    1: 2 3 | 3 2
    2: 4 4 | 5 5
    3: 4 5 | 5 4
    4: "a"
    5: "b"

    ababbb
    bababa
    abbbab
    aaabbb
    aaaabbb
"""


def test_solution1():
    matches, pattern, _ = day19.solve_part1(input1, True)
    assert pattern == "a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b"
    assert matches == 2


def test_solution2():
    pass
