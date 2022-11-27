#!/usr/bin/env python3

import sys
import numpy as np


def solve_part1(data):
    pass


def solve_part2(data):
    pass


def read_data(file):
    """Reads data of format '692,826 -> 692,915'

    :returns: ((int,int),(int,int))
    """
    def parse(line):
        s, e = line.split(sep="->")
        sx, sy = s.split(sep=",")
        ex, ey = e.split(sep=",")
        return ((int(sx), int(sy)), (int(ex), int(ey)))
    with open(file) as f:
        return [parse(line.strip()) for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    p1 = solve_part1(data)
    print(f"Part 1: {p1}")
    p2 = solve_part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
