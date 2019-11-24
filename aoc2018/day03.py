#!/usr/bin/env python3

import re
import sys


def get_input():
    """Parse file with lines: '#<id> @ <x>,<y>: <width>x<height>'"""
    assert len(sys.argv) == 2, "Missing input"
    input = []
    template = '#(?P<id>\d+?) @ (?P<x>\d+?),(?P<y>\d+?): (?P<width>\d+?)x(?P<height>\d+)'
    p = re.compile(template)
    with open(sys.argv[1]) as f:
        for line in f:
            d = p.match(line.strip()).groupdict()
            input.append(dict([a, int(x)] for a, x in d.items()))
    return input


def solve_part1(input):
    xsize = 1000
    ysize = 1000
    fabric = [[0]*xsize for i in range(ysize)]
    for claim in input:
        for x in range(claim['x'], claim['x'] + claim['width']):
            for y in range(claim['y'], claim['y'] + claim['height']):
                fabric[x][y] += 1
    overlapping = 0
    for x in range(xsize):
        for y in range(ysize):
            overlapping += 1 if fabric[x][y] > 1 else 0
    return overlapping


def solve_part2(input):
    xsize = 1000
    ysize = 1000
    fabric = [[0]*xsize for i in range(ysize)]
    claim_list = dict([claim['id'], True] for claim in input)
    for claim in input:
        for x in range(claim['x'], claim['x'] + claim['width']):
            for y in range(claim['y'], claim['y'] + claim['height']):
                if fabric[x][y] > 0:
                    claim_list[fabric[x][y]] = False
                    claim_list[claim['id']] = False
                fabric[x][y] = claim['id']
    return [id for id, valid in claim_list.items() if valid]


input = get_input()
print('Overlapping: {}'.format(solve_part1(input)))
print('Clean claim: {}'.format(solve_part2(input)))
