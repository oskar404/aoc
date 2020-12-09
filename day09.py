#!/usr/bin/env python3

import sys


def get_xmas_weakness(data, preamble, verbose=False):
    index = None
    value = None
    assert preamble < len(data), f"Not enough data for preamble: {preamble}"
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


def solve_part1(data, preamble, verbose=False):
    return get_xmas_weakness(data, preamble, verbose)


def solve_part2(data, preamble, verbose=False):
    _, weakness = get_xmas_weakness(data, preamble, verbose)
    sequence = None
    assert len(data) > 1, f"Too little data, len(data): {len(data)}"
    for start in range(len(data) - 1):
        seq = [data[start]]
        for i in range(start + 1, len(data)):
            seq.append(data[i])
            if sum(seq) >= weakness:
                break
        if verbose:
            print(f"{start}: seq{seq}")
        if sum(seq) == weakness:
            sequence = seq
            break
    if sequence and len(sequence) >= 2:
        return (min(sequence) + max(sequence), sequence)
    return (None, None)


def read_data(file):
    with open(file) as f:
        return [int(l.strip()) for l in f if l.strip()]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    idx, val = solve_part1(data, 25)
    print(f"Part 1: XMAS attack - invalid value: (idx: {idx}, value: {val})")
    val, seq = solve_part2(data, 25)
    print(f"Part 2: XMAS attack - sequence sum: {val} -> {seq}")


if __name__ == "__main__":
    main()
