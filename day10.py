#!/usr/bin/env python3

import copy
import sys


def solve_part1(data, verbose=False):
    result = [0, 0, 0, 1]  # NB! "built-in adapter is always 3 higher"
    jolt = 0
    data = copy.copy(data)
    data.sort()
    if verbose:
        print(data)
    for x in data:
        jmp = x - jolt
        if verbose:
            print(f"jolt({jolt}) -> jolt({x}) ({jmp})")
        assert jmp == 1 or jmp == 3
        result[jmp] += 1
        jolt = x
    return result[1] * result[3]


def solve_part2(data, verbose=False):
    pass


def read_data(file):
    with open(file) as f:
        return [int(l.strip()) for l in f if l.strip()]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: Jolt adapters - check sum: {solve_part1(data)}")


if __name__ == "__main__":
    main()
