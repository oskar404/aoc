#!/usr/bin/env python3

import sys


def _incr(tag, x):
    """Calculate increment for input"""
    index = {
        "forward": 0,
        "down": 1,
        "up": 1,
    }
    multiplier = {
        "forward": 1,
        "down": 1,
        "up": -1,
    }
    inc = [0, 0]
    inc[index[tag]] = multiplier[tag] * x
    return inc


def solve_part1(input):
    """Return position coordinates"""
    pos = [0, 0]
    for tag, value in input:
        x, y = _incr(tag, value)
        pos[0] = pos[0] + x
        pos[1] = pos[1] + y
    return (pos[0], pos[1])


def solve_part2(input):
    """Return position coordinates"""
    pos = [0, 0]
    aim = 0
    for tag, value in input:
        x, y = _incr(tag, value)
        aim = aim + y
        if x:
            pos[0] = pos[0] + x
            pos[1] = pos[1] + aim * x
    return (pos[0], pos[1])


def read_data(file):
    with open(file) as f:
        data = [line.split(maxsplit=1) for line in f]
    return [(tag, int(num)) for tag, num in data]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    position = solve_part1(data)
    print(f"Part 1: position: {position}, result: {position[0]*position[1]}")
    position = solve_part2(data)
    print(f"Part 2: position: {position}, result: {position[0]*position[1]}")


if __name__ == "__main__":
    main()
