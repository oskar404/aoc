#!/usr/bin/env python3
"""
Validation of password data. The fields are:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
"""

import math
import sys

def parse_batch(input):
    batch = []
    record = {}
    for line in [bl.strip() for bl in input.splitlines()]:
        if line:
            fields = [f.strip() for f in line.split()]
            for field in fields:
                key, value = field.split(sep=":")
                record[key] = value
            pass
        else:
            if record:
                batch.append(record)
            record = {}
    if record:
        batch.append(record)
    return batch


def solve_part1(input):
    """Calculate valid passports - accept also North Pole ID"""

    def is_valid(record):
        """Test that following fields exist:  ecl pid eyr hcl byr iyr hgt"""
        required = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
        valid = True
        for k in required:
            if k not in record:
                valid = False
        return valid

    batch = parse_batch(input)
    result = [is_valid(r) for r in batch]
    return sum(result)


def solve_part2(input):
    pass


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: valid passports {result}")


if __name__ == "__main__":
    main()
