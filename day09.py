#!/usr/bin/env python3

import sys


def solve_part1(data, preamble, verbose=False):
    index = None
    value = None
    for i in range(preamble, len(data)):
        v = data[i]
        window = data[i - preamble : i]
        if verbose:
            print(f"{i}: {data[i]} -> {window}")
        for a in window:
            b = v - a
            if b in window:
                break
        else:
            index = i
            value = v
            break
    return (index, value)


def solve_part2(input):
    pass


def read_data(file):
    with open(file) as f:
        return [int(l.strip()) for l in f if l.strip()]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    idx, val = solve_part1(data, 25)
    print(f"Part 1: XMAS attack - invalid value: (idx: {idx}, value: {val})")


if __name__ == "__main__":
    main()
