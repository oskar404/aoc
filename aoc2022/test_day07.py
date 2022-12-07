import pytest  # noqa: F401  # pylint: disable=unused-import
from day07 import solve_part1, solve_part2

TEST_DATA = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def test_solution1():
    assert solve_part1(TEST_DATA) == 95437


def test_solution2():
    assert solve_part2(TEST_DATA) == 24933642
