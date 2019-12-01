#!/usr/bin/env python3

import sys
from math import floor


# First 'simple' solution

def solve_part1(file):
    total = 0
    with open(file) as f:
        for line in f:
            total += floor(int(line)/3)-2
    return total


def fuel_requirement(mass):
    total = 0
    fuel = mass
    while True:
        fuel = floor(fuel/3)-2
        if fuel <= 0:
            break
        total += fuel
    return total


def solve_part2(file):
    total = 0
    with open(file) as f:
        for line in f:
            total += fuel_requirement(int(line))
    return total


assert len(sys.argv) == 2, "Missing input"
print(f"Fuel requirements (for modules): {solve_part1(sys.argv[1])}")
print(f"Fuel requirements (for modules+fuel): {solve_part2(sys.argv[1])}")


# Solve problem with list comprehension magic

def read_data(file):
    with open(file) as f:
        return [int(line) for line in f]

data = read_data(sys.argv[1])
result1 = sum([floor(i/3)-2 for i in data])
print(f"Fuel requirements (for modules): {result1}")
result2 = sum([fuel_requirement(i) for i in data])
print(f"Fuel requirements (for modules+fuel): {result2}")
