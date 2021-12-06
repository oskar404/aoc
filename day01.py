#!/usr/bin/env python3

import sys


def solve_part1(input):
    """Return steps how many times depth increases"""
    # NB! idx of input[1:] is one off
    return sum([dpth > input[idx] for idx, dpth in enumerate(input[1:])])


def solve_part2(input):
    """Return steps how many times depth increases of sliding window"""

    def window(idx):
        return sum(input[idx : idx + 3])

    return sum([window(idx + 1) > window(idx) for idx in range(len(input) - 3)])


def read_data(file):
    with open(file) as f:
        return [int(line) for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
