#!/usr/bin/env python3

import copy
import re
import sys
from enum import Enum


def parse(input):
    """Return tuple with dict of rules and list of str objects"""

    class State(Enum):
        RULES = 1
        PICS = 2

    def tokenize(rule):
        """Split rule to tokens"""

        def type_cast(token):
            if token[0].isdigit():
                return int(token)
            elif token == "|":
                return token
            # trust that value is '"a"' or '"b"'
            return token[1]

        return [type_cast(t) for t in rule.split()]

    rules = {}
    pics = []
    state = State.RULES

    for l in [l.strip() for l in input.splitlines()]:
        if not l and state == State.RULES and rules:
            state = State.PICS
        elif l and state == State.RULES:
            key, rule = l.split(":")
            rules[int(key)] = tokenize(rule)
        elif l and state == State.PICS:
            pics.append(l)

    return (rules, pics)


def create_pattern(rules, root):
    """Return regex pattern from rules"""

    pattern = []
    stack = []

    def push(rule):
        """Push rule to stack"""
        if "|" in rule:
            stack.append(")")
        for i in range(len(rule) - 1, -1, -1):
            stack.append(rule[i])
        if "|" in rule:
            stack.append("(")

    push(rules[root])
    while stack:
        ref = stack.pop()
        if isinstance(ref, int):
            push(rules[ref])
        else:
            pattern.append(ref)

    return "".join(pattern)


def solve_part1(input, verbose=False):
    """Return tuple with number of matches, match regex and matched rows"""
    rules, pics = parse(input)

    if verbose:
        for k, v in rules.items():
            print(f"rule {k}: {v}")

    pattern = create_pattern(rules, 0)

    if verbose:
        print(f"pattern: {pattern}")

    result = []

    prog = re.compile(pattern)
    for p in pics:
        if prog.fullmatch(p):
            result.append(p)

    if verbose:
        print(f"results: {result}")

    return (len(result), pattern, result)


def solve_part2(input, verbose=False):
    pass


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    matches, pattern, _ = solve_part1(data)
    print(f"Part 1: matches: {matches}")
    print(f"Part 1: pattern: {pattern}")


if __name__ == "__main__":
    main()
