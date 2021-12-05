#!/usr/bin/env python3

import copy
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


def parse_ticket(input, verbose=False):
    """Return dict with field name value pairs"""

    def is_valid(value):
        for r in rules:
            if r.match(value):
                return True
        return False

    rules, ticket, scanned = parse(input)

    if verbose:
        print(f"rules: {rules}")
        print(f"scanned: {scanned}")

    # Remove invalid tickets from references
    references = []
    for candidate in scanned:
        for value in candidate:
            if not is_valid(value):
                break
        else:
            references.append(candidate)

    if verbose:
        print(f"references: {references}")

    # Intial map containing all rules for all fields
    reduced = {}
    for i in range(len(ticket)):
        rset = {}
        for r in rules:
            rset[r.name] = r
        reduced[i] = rset

    # Reduce rules candidates based on scanned tickets
    for ref in references:
        for i, value in enumerate(ref):
            rset = {}
            for rule in reduced[i].values():
                if rule.match(value):
                    rset[rule.name] = rule
            reduced[i] = rset

    # Reduce candidates based on singles
    done = False
    while not done:
        for key, rset in reduced.items():
            if len(rset) == 1:
                for name in rset.keys():
                    for k in [k for k in reduced.keys() if k != key]:
                        reduced[k].pop(name, None)
        done = len(ticket) == sum([len(r) for r in reduced.values()])

    if verbose:
        print(f"reduced: {reduced}")

    # Create result
    result = {}
    for i, rules in reduced.items():
        assert len(rules) == 1
        for name in rules:
            result[name] = ticket[i]

    return result


def solve_part2(input):
    ticket = parse_ticket(input)
    result = 1
    for k, v in ticket.items():
        if k.startswith("departure"):
            result *= v
    return result


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: error rate: {solve_part1(data)}")
    print(f"Part 2: departure check sum: {solve_part2(data)}")


if __name__ == "__main__":
    main()
