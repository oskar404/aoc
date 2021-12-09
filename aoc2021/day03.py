#!/usr/bin/env python3

import sys


def solve_part1(input):
    """Return gamma, epsilon and power"""
    # transpose with numpy would be cool, but didn't bother to install it
    # trust that all input lines are same length
    sums = len(input[0]) * [0]  # init with zeroes
    for line in input:
        for idx in range(len(line)):
            sums[idx] = sums[idx] + int(line[idx])
    limit = len(input) / 2
    gamma = 0
    epsilon = 0
    for value in sums:
        if value > limit:  # Might be problem of greater or equal (>=)
            gamma = (gamma << 1) + 1
            epsilon = (epsilon << 1) + 0
        else:
            gamma = (gamma << 1) + 0
            epsilon = (epsilon << 1) + 1
    return (gamma, epsilon, gamma * epsilon)


def solve_part2(input):
    pass


def read_data(file):
    with open(file) as f:
        return [line.strip() for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    g, e, p = solve_part1(data)
    print(f"Part 1: gamma: {g} ({bin(g)}), epsilon: {e} ({bin(e)}) power: {p}")
    unsolved = solve_part2(data)
    print(f"Part 2: {unsolved}")


if __name__ == "__main__":
    main()
