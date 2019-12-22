#!/usr/bin/env python3

import math
import sys
from collections import OrderedDict


def read_data(file):
    """Read input into list of string"""
    data = []
    with open(file) as f:
        for line in f:
            data.append(line.strip())
    return data


def asteroid_coordinates(data):
    """Return list of coordinates of the asteroids"""
    asteroids = []
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                asteroids.append((x,y))
    return asteroids


def angle(start, end):
    result = math.atan2(end[0] - start[0], start[1] - end[1]) * 180 / math.pi
    if result < 0:
        return 360 + result
    return result


def dist(start, end):
    return abs((end[0]-start[0])+(end[1]-start[1]))


def optimal_position(data):
    """Solve optimal position for asteroid monitoring station"""
    asteroids = asteroid_coordinates(data)
    evaluation = {}  # Number of visible asteroids dict
    for pos in asteroids:
        seen_asteroids = { angle(pos, x) for x in asteroids if pos != x }
        evaluation[pos] = len(seen_asteroids)
    location = max(evaluation.keys(), key=(lambda k:evaluation[k]))
    return location, evaluation[location]


def vaporize(data, lazr):
    """Giant Asteroid Vaporizer Lazer rotator"""
    asteroids = asteroid_coordinates(data)
    asteroids.remove(lazr)
    angles = {}
    for p in asteroids:
        a = angle(lazr, p)
        while a in angles:
            d = dist(lazr, p)
            p0 = angles[a]
            d0 = dist(lazr, p0)
            if d > d0:
                p, p0 = p0, p
            angles[a] = p
            a += 360
            p = p0
        angles[a] = p
    return list(OrderedDict(sorted(angles.items())).values())


def main():
    assert len(sys.argv) == 2, "Missing input"

    data = read_data(sys.argv[1])
    loc, detected = optimal_position(data)
    print(f"Monitoring station position: {loc} detected: {detected}")
    order = vaporize(data, loc)
    bet = order[199][0]*100 + order[199][1]
    print(f"200th asteroid: {order[199]} -> {bet}")


if __name__ == "__main__":
    main()
