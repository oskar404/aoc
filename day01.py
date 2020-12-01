#!/usr/bin/env python3

import sys


def solve_part1(input):
    """Solve with set and iteration"""
    data = set(input)
    for v1 in input:
        v2 = 2020 - v1
        if v2 in data:
            return (v1*v2, v1, v2)


def read_data(file):
    with open(file) as f:
        return [int(line) for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result, value1, value2 = solve_part1(data)
    print(f"Part 1: {value1} + {value2} = {value1+value2} => {value1} * {value2} = {result}")


if __name__ == "__main__":
    main()
