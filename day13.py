#!/usr/bin/env python3

import sys


def parse(input):
    """Return tuple of timestamp and list of bus ids"""
    rows = [l.strip() for l in input.splitlines() if l.strip()]
    buses = [int(b) for b in rows[1].split(",") if b != "x"]
    return (int(rows[0]), buses)


def solve_part1(input, verbose=False):
    """Return code (wait time*bus id), bus id and wait time"""
    timestamp, buses = parse(input)

    starts = [timestamp] * len(buses)
    for i, bus in enumerate(buses):
        start0 = timestamp % bus
        if start0 != 0:
            starts[i] = (timestamp - start0) + bus

    next_bus = min(starts)
    idx = starts.index(next_bus)
    code = (next_bus - timestamp) * buses[idx]

    return (code, buses[idx], next_bus - timestamp)


def solve_part2(input, verbose=False):
    pass


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    code, bus, wait = solve_part1(data)
    print(f"Part 1: code:{code} bus:{bus} wait:{wait}")


if __name__ == "__main__":
    main()
