#!/usr/bin/env python3

import math
from collections import namedtuple
import utils


# The distress signal leads you to a giant waterfall! Actually, hang on -
# the signal seems like it's coming from the waterfall itself, and that
# doesn't make any sense. However, you do notice a little path that leads
# behind the waterfall.

WALL = "#"
SAND = "o"
FREE = " "

Coord = namedtuple("Coord", ["x", "y"])


def parse(data):
    """Parse data to dict with x,y coordinates as key and "#" value as
    value"""

    def coordinate(spec):
        """Parse "x,y" string into Coord"""
        raw = spec.split(",")
        return Coord(int(raw[0]), int(raw[1]))

    def point_iterator(start, end):
        """Iterate over points between start and end"""
        if start.x != end.x:
            direction = 1 if start.x <= end.x else -1
            for x in range(start.x, end.x, direction):
                yield Coord(x, start.y)
        else:
            direction = 1 if start.y <= end.y else -1
            for y in range(start.y, end.y, direction):
                yield Coord(start.x, y)

    walls = {}
    for path in data.strip().splitlines():
        coords = [coordinate(i) for i in path.strip().split(" -> ")]
        prev = coords[0]
        for point in coords[1:]:
            for step in point_iterator(prev, point):
                walls[step] = WALL
            prev = point
        walls[prev] = WALL  # set last block
    return walls


def simulate(data):
    """Simulate falling sand. Add location of sand into map data
    where key is x,y coordinates and "o" value as value
    """
    return data


def dump(data):
    """Dump the map data to screen"""

    min_x = math.inf
    min_y = 0
    max_x = -1
    max_y = -1
    for loc in data.keys():
        min_x = min(min_x, loc.x)
        max_x = max(max_x, loc.x)
        max_y = max(max_y, loc.y)

    for y in range(min_y, max_y + 1):
        row = [f"{y:3} "]

        for x in range(min_x, max_x + 1):
            coord = Coord(x, y)
            if coord in data:
                row.append(data[coord])
            else:
                row.append(FREE)
        print("".join(row))


def solve_part1(data):
    """Using your scan, simulate the falling sand. How many units of
    sand come to rest before sand starts flowing into the abyss below?
    """

    def sandcheck(state):
        """Calculate number of sandunits on map_state"""
        return len([x for x in state if x == "o"])

    data = parse(data)
    dump(data)
    data = simulate(data)
    return sandcheck(data)


def solve_part2(data):
    """Good luck!"""

    return len(data)


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
