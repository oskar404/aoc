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


def recurse_orbits(planet, data, count):
    """Orbit count with recursion. Not very efficient implementation, but works"""
    if planet in data:
        next_planet = data[planet]
        return recurse_orbits(next_planet, data, count+1)
    return count


def orbit_checksum(data):
    chksum = 0
    for planet in data:
        chksum += recurse_orbits(planet, data,  0)
    return chksum


def orbit_path(planet, data, path):
    """Resolve the path to center of planetary system. Use recursion"""
    if planet in data:
        path.append(data[planet])
        return orbit_path(path[-1], data, path)
    return path


def path_to_santa(data):
    orbits1 = orbit_path('YOU', data, [])
    orbits2 = orbit_path('SAN', data, [])
    prev = None
    while orbits1[-1] == orbits2[-1]:
         prev = orbits1[-1]
         orbits1 = orbits1[:-1]
         orbits2 = orbits2[:-1]
    path = orbits1
    path.append(prev)
    orbits2.reverse()
    return path + orbits2


assert len(sys.argv) == 2, "Missing input"
data = read_data(sys.argv[1])
print(f"Orbit checksum: {orbit_checksum(data)}")
path = path_to_santa(data)
print(f"Path to santa: {path})")
print(f"Orbit hops to santa: {len(path)-1}")
