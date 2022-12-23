#!/usr/bin/env python3

import utils

# The preparations are finally complete; you and the Elves leave camp on foot
# and begin to make your way toward the star fruit grove.


def marker(code):
    """To fix the communication system, you need to add a subroutine to the
    device that detects a start-of-packet marker in the datastream. In the
    protocol being used by the Elves, the start of a packet is indicated by a
    sequence of four characters that are all different.
    """
    return len(set(code)) == len(code)


def solve_part1(data):
    """How many characters need to be processed before the first start-of-packet
    marker is detected?
    """
    data = data.strip()
    for idx in range(4, len(data)):
        if marker(data[idx - 4 : idx]):
            return idx
    raise ValueError("no packet marker found")


def solve_part2(data):
    """How many characters need to be processed before the first
    start-of-message marker is detected?
    """
    data = data.strip()
    for idx in range(14, len(data)):
        if marker(data[idx - 14 : idx]):
            return idx
    raise ValueError("no packet marker found")


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
