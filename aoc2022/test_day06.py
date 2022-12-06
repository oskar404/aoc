import pytest  # noqa: F401  # pylint: disable=unused-import
from day06 import solve_part1, solve_part2


def test_solution1():
    assert solve_part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert solve_part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert solve_part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert solve_part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert solve_part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_solution2():
    assert solve_part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert solve_part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert solve_part2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert solve_part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert solve_part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
