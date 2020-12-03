#!/usr/bin/env python3

import math
import sys


def solve_part1(input):
    """Number of tree encounters when slope is (3,1)"""

    def is_tree(cell):
        return 1 if cell == "#" else 0

    def get_cell(row, pos):
        return row[pos % len(row)]

    pos = 0
    trees = 0
    for row in input:
        trees += is_tree(get_cell(row, pos))
        pos += 3
    return trees


def solve_part2(input):
    """Tree encounters for slopes: (1,1), (3,1), (5,1), (7,1), (1,2)"""

    def is_tree(cell):
        return 1 if cell == "#" else 0

    def get_cell(row, pos):
        return row[pos % len(row)]

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    encounters = []

    for slope in slopes:
        pos = 0
        trees = 0
        for row in range(0, len(input), slope[1]):
            trees += is_tree(get_cell(input[row], pos))
            pos += slope[0]
        encounters.append(trees)

    return math.prod(encounters)


def read_data(file):
    with open(file) as f:
        return [line.strip() for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: tree encounters {result}")
    result = solve_part2(data)
    print(f"Part 2: multiples slopes {result}")


if __name__ == "__main__":
    main()
