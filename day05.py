#!/usr/bin/env python3

import string
import sys


def get_input():
    assert len(sys.argv) == 2, "Missing input"
    with open(sys.argv[1]) as f:
        return list(str(f.read()).strip())


def react(i1, i2):
    return i1.lower() == i2.lower() and (
        (i1.isupper() and i2.islower()) or (i1.islower() and i2.isupper()))


def collapse(data):
    i = 0
    while i < len(data)-1:
        if react(data[i], data[i+1]):
            del data[i+1]
            del data[i]
            i -= 1
        else:
            i += 1
    return len(data)


def solve_part1(input):
    size = len(input)
    data = input.copy()
    return collapse(data), size


def solve_part2(input):
    size = len(input)
    min_size = size
    min_char = ''
    units = list(string.ascii_lowercase)
    for u in units:
        data = list(filter(lambda x: x != u and x != u.upper(), input))
        sz = collapse(data)
        if sz < min_size:
            min_size = sz
            min_char = u
    return min_size, size, min_char


input = get_input()
print('Part1: units left {} (original: {})'.format(*solve_part1(input)))
print('Part2: units left {} (original: {} / del {})'.format(*solve_part2(input)))
