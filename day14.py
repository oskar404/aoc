#!/usr/bin/env python3

import sys


def parse_data(input):
    def _parse(chem):
        """Return tuple of quantity and ID for """
        c = chem.strip().split()
        return (int(c[0]), c[1])

    data = {}
    for line in input.splitlines():
        formula, _, result = line.partition('=>')
        if result:  # Ignore empty lines
            quantity, chemical = _parse(result)
            assert chemical not in data, f"Chemical '{chemical}' defined twice"
            reaction =  list(map(_parse, [c for c in formula.strip().split(',')]))
            data[chemical] = (quantity, reaction)
    return data


def read_data(file):
    with open(file) as f:
        return parse_data(f.read())


class NanoFactory:
    """Logic for FUEL production"""
    def __init__(self, rules):
        self.rules = rules  # Production rules
        self.storage = {}   # Produced materials
        self.ore = 0        # Number of use ORE

    def reset(self):
        """Make testing easier"""
        self.storage = {}
        self.ore = 0

    def _get_chemical(self, units, name):
        """Get x units of named chemical component"""
        while name not in self.storage or units > self.storage[name]:
            self.produce_chemical(name)
        self.storage[name] -= units

    def produce_chemical(self, name):
        """Produce name item(s)"""
        quantity, formula = self.rules[name]
        for q, c in formula:
            if c == 'ORE':
                self.ore += q
            else:
                self._get_chemical(q, c)
        if name in self.storage:
            self.storage[name] += quantity
        else:
            self.storage[name] = quantity

    def run(self):
        """Run FUEL production and return used of ORE count"""
        self.produce_chemical('FUEL')
        return self.ore


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    factory = NanoFactory(data)
    print(f"Minimum amount of ORE for 1 FUEL: {factory.run()}")


if __name__ == "__main__":
    main()
