#!/usr/bin/env python3

import re
import sys
from enum import Enum


class TicketRule:
    def __init__(self, spec):
        pattern = r"([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)"
        m = re.match(pattern, spec.strip())
        self.name = m[1]
        self.r1_lo = int(m[2])
        self.r1_hi = int(m[3])
        self.r2_lo = int(m[4])
        self.r2_hi = int(m[5])

    def __str__(self):
        return f"{self.name}: {self.r1_lo}-{self.r1_hi} or {self.r2_lo}-{self.r2_hi}"

    def __repr__(self):
        return str(self)

    def match(self, value):
        return (value >= self.r1_lo and value <= self.r1_hi) or (
            value >= self.r2_lo and value <= self.r2_hi
        )


def parse(input):
    """Parse input and return tuple of rules, ticket, scanned tickets"""

    def read_ticket(spec):
        return [int(v) for v in spec.split(",")]

    class State(Enum):
        RULES = 1
        TICKET = 2
        SCANNED = 3

    rules = []
    ticket = None
    scanned = []
    state = State.RULES

    for r in [l.strip() for l in input.splitlines() if l.strip()]:
        if r == "your ticket:":
            state = State.TICKET
        elif r == "nearby tickets:":
            state = State.SCANNED
        elif state == State.RULES:
            rules.append(TicketRule(r))
        elif state == State.TICKET:
            ticket = read_ticket(r)
        elif state == State.SCANNED:
            scanned.append(read_ticket(r))
        else:
            assert False

    return (rules, ticket, scanned)


def solve_part1(input, verbose=False):
    """Return error rate"""

    def is_valid(value):
        for r in rules:
            if r.match(value):
                return True
        return False

    rules, _, scanned = parse(input)

    if verbose:
        print(f"rules: {rules}")
        print(f"scanned: {scanned}")

    error_rate = 0
    for ticket in scanned:
        for value in ticket:
            if not is_valid(value):
                error_rate += value

    return error_rate


def solve_part2(input, verbose=False):
    pass


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: error rate: {solve_part1(data)}")


if __name__ == "__main__":
    main()
