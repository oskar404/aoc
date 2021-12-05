#!/usr/bin/env python3

import sys


def solve_part1(input):
    """Solve with set and iteration.

    Value 600 is not handled correctly
    """
    data = set(input)
    for v1 in input:
        v2 = 2020 - v1
        if v2 in data:
            return (v1 * v2, v1, v2)


def solve_part2(input):
    """Solve with multiple iteration

    Values where same value can be used multiple times in sum will give
    wrong answers
    """
    for v1 in input:
        for v2 in input:
            v3 = 2020 - (v1 + v2)
            if v3 in input:
                return (v1 * v2 * v3, v1, v2, v3)


def read_data(file):
    with open(file) as f:
        return [int(line) for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result, v1, v2 = solve_part1(data)
    print(f"Part 1: {v1} + {v2} = {v1+v2} => {v1} * {v2} = {result}")
    result, v1, v2, v3 = solve_part2(data)
    print(f"Part 1: {v1} + {v2} + {v3} = {v1+v2+v3} => {v1} * {v2} * {v3} = {result}")


if __name__ == "__main__":
    main()
