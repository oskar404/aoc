#!/usr/bin/env python3

import sys


def solve_part1(file):
    sum = 0
    with open(file) as f:
        for line in f:
            sum += int(line)
    return sum


def solve_part2(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(int(line))
    freqs = set()
    sum = 0
    while True:
        for item in input:
            if sum in freqs:
                return sum
            freqs.add(sum)
            sum += item

assert len(sys.argv) == 2, "Missing input"
print('Frequency: {}'.format(solve_part1(sys.argv[1])))
print('Calibration ferquency: {}'.format(solve_part2(sys.argv[1])))
