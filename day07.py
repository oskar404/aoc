#!/usr/bin/env python3

import re
import sys


class BagEntry:
    """Data type bag color and quantity"""

    def __init__(self, color, multiplier):
        self.color = color
        self.multiplier = int(multiplier)

    def __str__(self):
        return f"{self.color}({self.multiplier})"

    def __repr__(self):
        return f"{self.color}({self.multiplier})"


def parse(input):
    """Some nifty regex magic rule would have been cool .."""
    batch = {}
    pattern = r"([0-9]+) ([a-z]+ [a-z]+)"
    matcher = re.compile(pattern)
    for line in [bl.strip() for bl in input.splitlines() if bl.strip()]:
        key, rule = line.split(" bags contain ")
        if rule.strip() == "no other bags.":
            batch[key] = []
        else:
            bags = []
            entries = re.split(r" bag, | bags, | bag\.| bags\.", rule)
            for e in [e.strip() for e in entries if e.strip()]:
                m, c = matcher.match(e).groups()
                bags.append(BagEntry(c, m))
            batch[key] = bags
    return batch


def solve_part1(input):
    def recurse(rules, color):
        result = set()
        if color not in rules:
            return result
        for c in rules[color]:
            result.add(c)
            result = result.union(recurse(rules, c))
        return result

    data = parse(input)
    rules = {}
    for key, bags in data.items():
        for bag in bags:
            refs = set()
            if bag.color in rules:
                refs = rules[bag.color]
            refs.add(key)
            rules[bag.color] = refs
    result = recurse(rules, "shiny gold")
    return len(result)


def solve_part2(input):
    pass


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: How many bag colors? -> {solve_part1(data)}")


if __name__ == "__main__":
    main()
