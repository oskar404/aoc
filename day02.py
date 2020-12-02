#!/usr/bin/env python3

import re
import sys


class PasswdRule:
    def __init__(self, min, max, char):
        self.min = min
        self.max = max
        self.char = char

    def match(self, passwd):
        c = passwd.count(self.char)
        return c >= self.min and c <= self.max


def parse_input(data):
    """Parses lines as password entries with rule"""
    pattern = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"
    prog = re.compile(pattern)
    result = []
    for line in data:
        m = prog.match(line)
        min, max, char, passwd = m.groups()
        result.append((PasswdRule(int(min), int(max), char), passwd))
    return result


def solve_part1(input):
    """Find number of entries matching the password requirements"""
    passwords = parse_input(input)
    found = 0
    for entry in passwords:
        if entry[0].match(entry[1]):
            found += 1
    return found


def solve_part2(input):
    pass


def read_data(file):
    with open(file) as f:
        return [line for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: valid passwords {result}")


if __name__ == "__main__":
    main()
