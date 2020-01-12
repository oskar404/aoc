#!/usr/bin/env python3

import math
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
        self.ore = 0        # Number of used ORE

    def reset(self):
        """Make testing easier"""
        self.storage = {}
        self.ore = 0

    def _get_chemical(self, units, name):
        """Get x units of named chemical component"""
        if units > self.storage.get(name, 0):
            self.produce_chemical(name, units-self.storage.get(name, 0))
        self.storage[name] -= units

    def produce_chemical(self, name, units=1):
        """Produce name item(s)"""
        quantity, formula = self.rules[name]
        m = math.ceil(units / quantity)
        for q, c in formula:
            if c == 'ORE':
                self.ore += q * m
            else:
                self._get_chemical(q*m, c)
        self.storage[name] = self.storage.get(name, 0) + quantity * m

    def run(self):
        """Run FUEL production for one cell. Return used ORE count"""
        self.produce_chemical('FUEL')
        return self.ore

    def run_production(self, reserve=1000000000000):
        """Create FUEL cells from all ORE stash. Return number of FUEL cells

        Use minmax algorithm to solve the problem
        """
        fuel_min = 1
        fuel_max = 100000000
        while (fuel_max - fuel_min) > 1:
            units = (fuel_min + fuel_max) // 2
            self.produce_chemical('FUEL', units)
            if self.ore <= reserve:
                fuel_min = units
            else:
                fuel_max = units
            self.reset()
        return fuel_min


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    factory = NanoFactory(data)
    print(f"Minimum amount of ORE for 1 FUEL: {factory.run()}")
    factory.reset()
    print(f"FUEL: {factory.run_production()} for 1000000000000 ORE")


if __name__ == "__main__":
    main()
