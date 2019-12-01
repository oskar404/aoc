#!/usr/bin/env python3

import math
import sys


def solve_part1(file):
    total_fuel = 0
    with open(file) as f:
        for line in f:
            module_fuel = math.floor(int(line)/3)-2
            total_fuel += module_fuel
    return total_fuel


def fuel_requirement(mass):
    total = 0
    fuel = mass
    while True:
        fuel = math.floor(fuel/3)-2
        if fuel <= 0:
            break
        total += fuel
    return total


def solve_part2(file):
    total_fuel = 0
    with open(file) as f:
        for line in f:
            total_fuel += fuel_requirement(int(line))
    return total_fuel


assert len(sys.argv) == 2, "Missing input"
print(f"Fuel requirements (for modules): {solve_part1(sys.argv[1])}")
print(f"Fule requirements (for modules+fuel): {solve_part2(sys.argv[1])}")
