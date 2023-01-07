#!/usr/bin/env python3

import math
import re
from collections import namedtuple
import utils


# You feel the ground rumble again as the distress signal leads you to a large
# network of subterranean tunnels. You don't have time to search them all, but
# you don't need to: your pack contains a set of deployable sensors that you
# imagine were originally built to locate lost Elves.


SNSR = "S"
BCON = "B"
CVER = "#"

Coord = namedtuple("Coord", ["x", "y"])


SENSOR = r"Sensor\sat\sx=(-?[0-9]+),\sy=(-?[0-9]+):\s"
BEACON = r"closest\sbeacon\sis\sat\sx=(-?[0-9]+),\sy=(-?[0-9]+)"
PATTERN = f"{SENSOR}{BEACON}"


def parse(data):
    """Parse sensor data into dict"""

    pattern = re.compile(PATTERN)

    sensors = {}
    for line in data.strip().splitlines():
        result = pattern.match(line)
        sensor = Coord(int(result.group(1)), int(result.group(2)))
        beacon = Coord(int(result.group(3)), int(result.group(4)))
        sensors[sensor] = beacon
    return sensors


def map_corners(data):
    """Returns coordinates for left upper corner (min) and right lower
    corner (max) as tuple
    """
    min_x = math.inf
    min_y = math.inf
    max_x = -1
    max_y = -1

    def check_min(pos):
        """Get min x,y"""
        return min(min_x, pos.x), min(min_y, pos.y)

    def check_max(pos):
        """Get max x,y"""
        return max(max_x, pos.x), max(max_y, pos.y)

    for sensor, beacon in data.items():
        min_x, min_y = check_min(sensor)
        min_x, min_y = check_min(beacon)
        max_x, max_y = check_max(sensor)
        max_x, max_y = check_max(beacon)
    return (Coord(min_x, min_y), Coord(max_x, max_y))


def dump(data):
    """Dump the map data to screen"""
    min_pos, max_pos = map_corners(data)
    print(f"{min_pos=}")
    print(f"{max_pos=}")
    sensors = set(data.keys())
    beacons = set(data.values())
    for y in range(min_pos.y, max_pos.y + 1):
        row = [f"{y:8} "]

        for x in range(min_pos.x, max_pos.x + 1):
            coord = Coord(x, y)
            if coord in sensors:
                row.append(SNSR)
            elif coord in beacons:
                row.append(BCON)
            else:
                row.append(" ")
        print("".join(row))


def manhattan_distance(loc1, loc2):
    """Return Manhattan distance of two points"""
    return abs(loc1.x - loc2.x) + abs(loc1.y - loc2.y)


def scan_line(data, distances, y):
    """Scan line y to for coverage"""
    result = {}
    beacons = set(data.values())
    for sensor in data.keys():
        coverage = distances[sensor]

        # scan to left from x
        loc = Coord(sensor.x, y)
        while manhattan_distance(sensor, loc) <= coverage:
            if loc in beacons:
                result[loc] = BCON
            else:
                result[loc] = CVER
            loc = Coord(loc.x - 1, y)

        # scan to right from x
        loc = Coord(sensor.x + 1, y)
        while manhattan_distance(sensor, loc) <= coverage:
            if loc in beacons:
                result[loc] = BCON
            else:
                result[loc] = CVER
            loc = Coord(loc.x + 1, y)

    return result


def solve_part1(data, y=2000000):
    """Consult the report from the sensors you just deployed. In the row
    where y=2000000, how many positions cannot contain a beacon?
    """

    def collect_distances(data):
        """Return dict containing distance for each sensor"""
        distances = {}
        for sensor, beacon in data.items():
            distance = manhattan_distance(sensor, beacon)
            distances[sensor] = distance
        return distances

    def coverage(line):
        """Return coverage on the line"""
        return len([x for x in line.values() if x == CVER])

    data = parse(data)
    distances = collect_distances(data)
    line = scan_line(data, distances, y)
    if utils.VERBOSE:
        dump(data)
        print()  # just empty line
        print(f"{y:8} {''.join(line.values())}")
    return coverage(line)


def solve_part2(data):
    """Find the only possible position for the distress beacon. What is
    its tuning frequency?"""
    # Fix this
    return len(data)


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
