#!/usr/bin/env python3

import re
import sys


def parse1(input):
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


ops_v1 = {
    "0": lambda arg, bit: 0,
    "1": lambda arg, bit: 1 << bit,
    "X": lambda arg, bit: arg & (1 << bit),
}


def solve_part1(input, verbose=False):
    """Return code is sum of all memory addresses

    version 1 decoder chip
    """
    data = parse1(input)
    mem = {}

    if verbose:
        print("PROG: ***")
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
                v += ops_v1[mask[35 - pos]](e[1], pos)
            mem[e[0]] = v

    if verbose:
        print("MEM: ***")
        for k, v in mem.items():
            print(f"{k} -> {v}")

    return sum(mem.values())


def parse2(input):
    """Parse input data and return as list of tuples"""
    pattern = r"mem\[([0-9]+)\]"
    matcher = re.compile(pattern)

    def splitter(value):
        k, v = value.split("=")
        k = k.strip()
        if k != "mask":
            v = int(v)
            k = int(matcher.match(k).group(1))
        else:
            v = v.strip()
        return (k, v)

    rows = [splitter(l) for l in input.splitlines() if l.strip()]
    return rows


def set_bit(addrs, bit):
    """Set address bit to one"""
    result = []
    for addr in addrs:
        result.append(addr | (1 << bit))
    return result


def duplicate_bit(addrs, bit):
    """Set address bit to zero and one i.e. duplicate adderesses"""
    id_mask = 0b111111111111111111111111111111111111
    result = []
    for addr in addrs:
        result.append(addr | (1 << bit))
        result.append(addr & ((1 << bit) ^ id_mask))
    return result


ops_v2 = {
    "0": lambda addrs, bit: addrs,
    "1": set_bit,
    "X": duplicate_bit,
}


def solve_part2(input, verbose=False):
    """Return code is sum of all memory addresses

    version 2 decoder chip
    """
    data = parse2(input)
    mem = {}

    if verbose:
        print("PROG: ***")
        for r in data:
            print(r)

    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    for e in data:
        if e[0] == "mask":
            mask = e[1]
            assert len(mask) == 36
        else:
            addrs = [e[0]]
            for pos in range(36):
                addrs = ops_v2[mask[35 - pos]](addrs, pos)
            for addr in addrs:
                mem[addr] = e[1]

    if verbose:
        print("MEM: ***")
        for k in sorted(mem.keys()):
            print(f"{k} -> {mem[k]}")

    return sum(mem.values())


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: code: {solve_part1(data)}")
    print(f"Part 2: code: {solve_part2(data)}")


if __name__ == "__main__":
    main()
