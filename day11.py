#!/usr/bin/env python3

import copy
import sys


def parse(input):
    """Parse seat layout to list of strings"""
    return [list(l.strip()) for l in input.splitlines() if l.strip()]


def dump(layout, round):
    print(f"*** ROUND: {round} ***")
    for row in layout:
        print(f"{''.join(row)}")
    print(f"")


def occupied_seats(layout, marker="#"):
    return sum([row.count(marker) for row in layout])


def neighbours(state, x, y, marker="#"):
    result = 0
    for yi in range(-1, 2):
        yp = y + yi
        if yp >= 0 and yp < len(state):
            for xi in range(-1, 2):
                xp = x + xi
                if not (xp == x and yp == y) and xp >= 0 and xp < len(state[yp]):
                    if state[yp][xp] == marker:
                        result += 1
    return result


def solve_part1(input, verbose=False):
    layout = parse(input)
    round = 0
    state = copy.deepcopy(layout)

    if verbose:
        dump(state, round)

    while True:

        round += 1
        prev_state = copy.deepcopy(state)
        for y, line in enumerate(prev_state):
            for x, c in enumerate(line):
                if c == "L":
                    if neighbours(prev_state, x, y) == 0:
                        state[y][x] = "#"
                elif c == "#":
                    if neighbours(prev_state, x, y) >= 4:
                        state[y][x] = "L"

        if verbose:
            dump(state, round)

        if prev_state == state:
            break

    return (occupied_seats(state), round - 1)


# List the coordinate directions
directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def adjacent(state, xp, yp):
    """Return number of adjacent chairs which are occupied"""
    occupied = 0

    for xd, yd in directions:
        x = xp + xd
        y = yp + yd
        while y >= 0 and y < len(state) and x >= 0 and x < len(state[y]):
            if state[y][x] == "#":
                occupied += 1
                break
            elif state[y][x] == "L":
                break
            x += xd
            y += yd

    return occupied


def solve_part2(input, verbose=False):
    layout = parse(input)
    round = 0
    state = copy.deepcopy(layout)

    if verbose:
        dump(state, round)

    while True:

        round += 1
        prev_state = copy.deepcopy(state)
        for y, line in enumerate(prev_state):
            for x, c in enumerate(line):
                if c == "L":
                    if adjacent(prev_state, x, y) == 0:
                        state[y][x] = "#"
                elif c == "#":
                    if adjacent(prev_state, x, y) >= 5:
                        state[y][x] = "L"

        if verbose:
            dump(state, round)

        if prev_state == state:
            break

    return (occupied_seats(state), round - 1)


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    occupied, rounds = solve_part1(data)
    print(f"Part 1: occupied seats: {occupied} (rounds:{rounds})")
    occupied, rounds = solve_part2(data)
    print(f"Part 2: occupied seats: {occupied} (rounds:{rounds})")


if __name__ == "__main__":
    main()
