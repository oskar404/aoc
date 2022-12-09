#!/usr/bin/env python3

import sys
import utils

# This rope bridge creaks as you walk along it. You aren't sure how old it is,
# or whether it can even support your weight.
#
# It seems to support the Elves just fine, though. The bridge spans a gorge
# which was carved out by the massive river far below you.
#
# You step carefully; as you do, the ropes stretch and twist. You decide to
# distract yourself by modeling rope physics; maybe you can even figure out
# where not to step.


def parse_line(line):
    """Return (direction, int(steps))"""
    direction, steps = line.split()
    return direction, int(steps)


def move(pos, direction):
    """Move position according to dir"""
    ops = {
        "R": [+1, 0],
        "L": [-1, 0],
        "U": [0, +1],
        "D": [0, -1],
    }
    pos[0] += ops[direction][0]
    pos[1] += ops[direction][1]


def creep(head, tail):
    """Move tail adjacent to head"""

    def increment(arg1, arg2):
        if arg1 < arg2:
            return -1
        if arg1 > arg2:
            return 1
        return 0

    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        tail[0] += increment(head[0], tail[0])
        tail[1] += increment(head[1], tail[1])


def solve_part1(data):
    """Simulate your complete hypothetical series of motions. How many positions
    does the tail of the rope visit at least once?
    """

    data = data.strip()
    visited = {(0, 0)}  # starting posision
    head = [0, 0]
    tail = [0, 0]

    for line in data.splitlines():
        direction, steps = parse_line(line)
        for _ in range(steps):
            move(head, direction)
            creep(head, tail)
            visited.add(tuple(tail))

    return len(visited)


def solve_part2(data):
    """Simulate your complete series of motions on a larger rope with ten knots.
    How many positions does the tail of the rope visit at least once?
    """

    data = data.strip()
    visited = {(0, 0)}  # starting posision
    rope = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    ]

    for line in data.splitlines():
        direction, steps = parse_line(line)
        for _ in range(steps):
            move(rope[0], direction)
            for i in range(1, len(rope)):
                creep(rope[i - 1], rope[i])
            visited.add(tuple(rope[-1]))

    return len(visited)


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = utils.read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
