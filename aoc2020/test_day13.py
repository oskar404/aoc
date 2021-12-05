import pytest
import day13


input = """
    939
    7,13,x,x,59,x,31,19
"""


def test_solution1():
    code, bus, wait = day13.solve_part1(input, True)
    assert code == 295
    assert bus == 59
    assert wait == 5


data1 = """
XXX
17,x,13,19
"""

data2 = """
XXX
67,7,59,61
"""

data3 = """
XXX
67,x,7,59,61
"""

data4 = """
XXX
67,7,x,59,61
"""

data5 = """
XXX
1789,37,47,1889
"""


def test_solution2():
    assert day13.solve_part2(data1, True) == 3417
    assert day13.solve_part2(data2, True) == 754018
    assert day13.solve_part2(data3, True) == 779210
    assert day13.solve_part2(data4, True) == 1261476
    assert day13.solve_part2(data5, True) == 1202161486
    assert day13.solve_part2(input, True) == 1068781
