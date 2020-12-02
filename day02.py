#!/usr/bin/env python3

import re
import sys


class OldPasswdRule:
    def __init__(self, min, max, char):
        self.min = min
        self.max = max
        self.char = char

    def match(self, passwd):
        c = passwd.count(self.char)
        return c >= self.min and c <= self.max


class TobogganRule:
    def __init__(self, idx1, idx2, char):
        self.idx1 = idx1
        self.idx2 = idx2
        self.char = char

    def match(self, passwd):
        c1 = passwd[self.idx1]
        c2 = passwd[self.idx2]
        return c1 != c2 and (c1 == self.char or c2 == self.char)


def parse_input(data, rule):
    """Parses lines as password entries with rule"""
    pattern = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"
    prog = re.compile(pattern)
    result = []
    for line in data:
        m = prog.match(line)
        min, max, char, passwd = m.groups()
        result.append((rule(int(min) - 1, int(max) - 1, char), passwd))
    return result


def solve_part1(input):
    """Find matching the passwords using OldPasswdRule"""
    passwords = parse_input(input, OldPasswdRule)
    matches = [rule.match(passwd) for rule, passwd in passwords]
    return sum(matches)


def solve_part2(input):
    """Find matching the passwords requirements using TobogganRule"""
    passwords = parse_input(input, TobogganRule)
    matches = [rule.match(passwd) for rule, passwd in passwords]
    return sum(matches)


def read_data(file):
    with open(file) as f:
        return [line for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: valid passwords {result}")
    result = solve_part2(data)
    print(f"Part 2: valid passwords {result}")


if __name__ == "__main__":
    main()
