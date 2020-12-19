#!/usr/bin/env python3

import sys


def parse(input):
    """Parse input data and return as list of tuples"""

    def splitter(value):
        k, v = value.split("=")
        k = k.strip()
        if k != "mask":
            v = int(v)
        else:
            v = v.strip()
        return (k, v)

    rows = [splitter(l) for l in input.splitlines() if l.strip()]
    return rows


ops = {
    "0": lambda arg, shift: 0,
    "1": lambda arg, shift: 1 << shift,
    "X": lambda arg, shift: arg & (1 << shift),
}


def solve_part1(input, verbose=False):
    """Return code is sum of all memory addresses"""
    data = parse(input)
    mem = {}

    if verbose:
        print("DATA: ***")
        for r in data:
            print(r)

    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    for e in data:
        if e[0] == "mask":
            mask = e[1]
            assert len(mask) == 36
        else:
            v = 0
            for pos in range(36):
                v += ops[mask[35 - pos]](e[1], pos)
            mem[e[0]] = v

    if verbose:
        print("MEM: ***")
        for k, v in mem.items():
            print(f"{k} -> {v}")

    return sum(mem.values())


def solve_part2(input, verbose=False):
    pass


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: code:{solve_part1(data)}")


if __name__ == "__main__":
    main()
