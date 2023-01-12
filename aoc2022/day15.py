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


@utils.timeit
def scan_line(data, distances, y):
    """Scan line y to for coverage"""

    # care about beacons in line only
    beacons = {b.x for b in data.values() if b.y == y}
    # project sensors to line
    coverage = set()
    for sensor, distance in distances.items():
        radius = distance - abs(sensor.y - y)
        if radius >= 0:
            for x in range(sensor.x - radius, sensor.x + radius + 1):
                coverage.add(x)

    # create result
    result = {}
    for x in coverage:
        result[Coord(x, y)] = CVER
    for x in beacons:
        result[Coord(x, y)] = BCON

    return result


def collect_distances(data):
    """Return dict containing distance for each sensor"""
    distances = {}
    for sensor, beacon in data.items():
        distance = manhattan_distance(sensor, beacon)
        distances[sensor] = distance
    return distances


def solve_part1(data, y=2000000):
    """Consult the report from the sensors you just deployed. In the row
    where y=2000000, how many positions cannot contain a beacon?
    """

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


@utils.timeit
def scan_line2(distances, y, min_x, max_x):
    """Scan line y and return non covered points"""

    line = set(range(min_x, max_x + 1))

    # project sensors to line and remove covered from line
    for sensor, distance in distances.items():
        radius = distance - abs(sensor.y - y)
        if radius >= 0:
            coverage = set(range(sensor.x - radius, sensor.x + radius + 1))
            line = line - coverage

    return line


def solve_part2(data, min_p=0, max_p=4000000):
    """Find the only possible position for the distress beacon. What is
    its tuning frequency?"""

    def tuning_frequency(x, y):
        return 4000000 * x + y

    result = -1

    data = parse(data)
    distances = collect_distances(data)
    for y in range(min_p, max_p + 1):
        print(f"{y}")
        line = scan_line2(distances, y, min_p, max_p)
        if len(line) > 0:
            assert len(line) == 1
            result = tuning_frequency(line.pop(), y)
            break

    return result


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
