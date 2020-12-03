import pytest
import day03


def test_solution1():
    data = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    result = day03.solve_part1(data)
    assert result == 7


def test_solution2():
    pass
