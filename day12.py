#!/usr/bin/env python3

import math
import sys


instructions = {
    "N": (0, 1, 0, 0),  # North 0 degrees
    "S": (0, -1, 0, 0),  # South 180 degrees
    "E": (1, 0, 0, 0),  # East 90 degrees
    "W": (-1, 0, 0, 0),  # West 270 degrees
    "L": (0, 0, 1, 0),
    "R": (0, 0, -1, 0),
    "F": (0, 0, 0, 1),
}


def solve_part1(input, verbose=False):
    position = [0, 0, 0]  # x (E-W), y (N-S), d (0 degrees == E)

    for rule in input:
        cmd = instructions[rule[0]]
        val = int(rule[1:])

        position[0] += cmd[0] * val
        position[1] += cmd[1] * val
        position[2] = (position[2] + cmd[2] * val) % 360

        if cmd[3]:
            rad = (position[2] * math.pi) / 180
            position[0] += math.cos(rad) * val
            position[1] += math.sin(rad) * val

        if verbose:
            print(f"cmd: {rule} -> {cmd} / {position}")

    distance = round(abs(position[0]) + abs(position[1]))
    return (distance, position)


def solve_part2(input, verbose=False):
    pass


def read_data(file):
    with open(file) as f:
        return [line.strip() for line in f if line.strip()]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    distance, cord = solve_part1(data)
    print(f"Part 1: distance: {distance} (coordinates:{cord})")


if __name__ == "__main__":
    main()
