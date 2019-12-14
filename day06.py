#!/usr/bin/env python3

import sys


def read_data(file):
    data = {}
    with open(file) as f:
        for line in f:
            v, k = line.strip().split(')')
            assert k not in data
            data[k] = v
    return data


def recurse_orbits(planet, count, data):
    """Orbit count with recursion. Not very efficient implementation, but works"""
    if planet in data:
        next_planet = data[planet]
        return recurse_orbits(next_planet, count+1, data)
    return count


def orbit_checksum(data):
    chksum = 0
    for planet in data:
        chksum += recurse_orbits(planet, 0, data)
    return chksum


assert len(sys.argv) == 2, "Missing input"
data = read_data(sys.argv[1])
print(f"Orbit checksum: {orbit_checksum(data)}")
#(distance, position) = resolve_shortest_distance(data)
#print(f"Shortest intersect: {distance} ({position.real},{position.imag})")
