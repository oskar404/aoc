#!/usr/bin/env python3

import utils

# You try contacting the Elves using your handheld device, but the river
# you're following must be too low to get a decent signal.


def solve_part1(data):
    """What is the fewest steps required to move from your current
    position to the location that should get the best signal?
    """

    # Solution is https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    mapdata = [ i.strip() for i in data.strip().splitlines() ]

    # find root/starting point
    start = [0,0]
    for x, line in enumerate(mapdata):
        y = line.find("S")
        if  y >= 0:
            start = [x, y]
            break
    assert mapdata[start[0]][start[1]] == "S"

    # TODO: Implement algorithm here

    return len(data)


def solve_part2(data):
    """Just template
    """

    return len(data) != 0


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
