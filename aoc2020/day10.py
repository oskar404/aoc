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


cache = {
    1: 2,
    2: 4,
}


def permutate(size):
    """Calculate number of permutations for a size. Max distance can be 3.
    Calculate with bit masks i.e. max 2 consecutive bits can be zero"""
    assert size > 0
    if size in cache:
        return cache[size]
    max_permutations = pow(2, size)
    result = 0
    for candidate in range(max_permutations):
        bit0 = 1
        bit1 = 1
        for shift in range(size):
            bit2 = (candidate >> shift) & 1
            if bit0 + bit1 + bit2 == 0:
                break
            bit0 = bit1
            bit1 = bit2
        else:
            result += 1
    cache[size] = result
    return result


def solve_part2(data, verbose=False):

    # Add start jolt and built-in adapter jolt to sequence and keep it sorted
    data = [0] + data
    data.sort()
    data.append(data[-1] + 3)
    if verbose:
        print(f"data: {data}")

    # Mark the static jolts which can not be removed (distance to 3)
    static = [True for _ in data]
    for i in range(1, len(data) - 1):
        static[i] = data[i] - data[i - 1] == 3 or data[i + 1] - data[i] == 3
    if verbose:
        print(f"static: {static}")

    # Search slices which can be permuted
    permutations = 1
    start = 0
    for i in range(1, len(data)):
        if start == i - 1 and static[i]:
            start = i
        elif static[i]:
            size = i - (start + 1)
            combinations = permutate(size)
            permutations *= combinations
            if verbose:
                print(f"slice: {size} -> {combinations}:{permutations}")
            start = i

    return permutations


def read_data(file):
    with open(file) as f:
        return [int(l.strip()) for l in f if l.strip()]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: Jolt adapters - check sum: {solve_part1(data)}")
    print(f"Part 2: Jolt adapters - permutations: {solve_part2(data)}")


if __name__ == "__main__":
    main()
