#!/usr/bin/env python3

import sys


def parse(input):
    """Parse input and return dict of active coordinates"""

    pocket = {}

    z = 0
    for y, row in enumerate([l.strip() for l in input.splitlines() if l.strip()]):
        for x, state in enumerate(row):
            if state == "#":
                pocket[(x, y, z)] = True
    return pocket


def pocket_space(pos):
    """Return surrounding space coordinates as list"""
    result = []
    for x in range(pos[0] - 1, pos[0] + 2):
        for y in range(pos[1] - 1, pos[1] + 2):
            for z in range(pos[2] - 1, pos[2] + 2):
                result.append((x, y, z))
    return result


def active_cube(current, pos):
    """Return True if position should be active.

    Rules:
    - If a cube is active and exactly 2 or 3 of its neighbors are also
      active, the cube remains active. Otherwise, the cube becomes
      inactive.
    - If a cube is inactive but exactly 3 of its neighbors are active,
      the cube becomes active. Otherwise, the cube remains inactive.
    """
    state = pos in current
    active = 0
    coords = [p for p in pocket_space(pos) if p != pos]
    for p in coords:
        if p in current:
            active += 1
    return active == 3 or (state and active == 2)


def solve_part1(input, verbose=False):
    """Return error rate"""

    prev = parse(input)
    state = None

    # iterations
    for i in range(6):
        if verbose:
            print(f"state {i}: {prev}")

        # resolve active pocket space
        pocket = set()
        for pos, value in prev.items():
            if value:
                space = pocket_space(pos)
                pocket = pocket.union(set(space))

        # resolve next states
        state = {}
        for pos in pocket:
            if active_cube(prev, pos):
                state[pos] = True

        prev = state

    if verbose:
        print(f"final state: {state}")

    return len(state)


def solve_part2(input):
    pass


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: active cubes after 6 cycles: {solve_part1(data)}")


if __name__ == "__main__":
    main()
