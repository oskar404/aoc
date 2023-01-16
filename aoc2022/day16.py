#!/usr/bin/env python3

import utils

# The sensors have led you to the origin of the distress signal: yet another
# handheld device, just like the one the Elves gave you. However, you don't see
# any Elves around; instead, the device is surrounded by elephants! They must
# have gotten lost in these tunnels, and one of the elephants apparently figured
# out how to turn on the distress signal.
#
# The ground rumbles again, much stronger this time. What kind of cave is this,
# exactly? You scan the cave with your handheld device; it reports mostly
# igneous rock, some ash, pockets of pressurized gas, magma... this isn't just
# a cave, it's a volcano!
#
# You need to get the elephants out of here, quickly. Your device estimates that
# you have 30 minutes before the volcano erupts, so you don't have time to go
# back out the way you came in.


def parse(data):
    """Parse input data"""
    return data


@utils.timeit
def solve_part1(data):
    """Work out the steps to release the most pressure in 30 minutes.
    What is the most pressure you can release?
    """
    data = parse(data)
    return len(data)


@utils.timeit
def solve_part2(data):
    """Do it"""
    return len(data)


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
