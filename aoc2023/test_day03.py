import pytest  # noqa: F401  # pylint: disable=unused-import
import day03


DATA = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

DATA2 = """
12.......*..
+.........34
.......-12..
..78........
..*....60...
78..........
.......23...
....90*12...
............
2.2......12.
.*.........*
1.1.......56
"""


def test_solution1():
    result = day03.solve_part1(DATA.strip())
    assert result == 4361
    result = day03.solve_part1(DATA2.strip())
    assert result == 413


def test_solution2():
    result = day03.solve_part2(DATA.strip())
    assert result == 467835
