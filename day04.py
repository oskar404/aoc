#!/usr/bin/env python3
"""
Validation of password data. The fields are:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""

from day02 import OldPasswdRule
import re
import sys


def parse_batch(input):
    batch = []
    record = {}
    for line in [bl.strip() for bl in input.splitlines()]:
        if line:
            fields = [f.strip() for f in line.split()]
            for field in fields:
                key, value = field.split(sep=":")
                record[key] = value.strip()
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
        for k in required:
            if k not in record:
                return False
        return True

    batch = parse_batch(input)
    result = [is_valid(r) for r in batch]
    return sum(result)


def validate_byr(value):
    v = int(value)
    return v >= 1920 and v <= 2002


def validate_iyr(value):
    v = int(value)
    return v >= 2010 and v <= 2020


def validate_eyr(value):
    v = int(value)
    return v >= 2020 and v <= 2030


def validate_hgt(value):
    p = re.compile("([0-9]+)(cm|in)")
    m = p.match(value)
    if not m:
        return False
    g = m.groups()
    v = int(g[0])
    if g[1] == "cm":
        return v >= 150 and v <= 193
    elif g[1] == "in":
        return v >= 59 and v <= 76
    return False


def validate_hcl(value):
    if len(value) != 7:
        return False
    p = re.compile("#[0-9a-f]{6}")
    if p.match(value):
        return True
    return False


def validate_ecl(value):
    valid_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return value in valid_values


def validate_pid(value):
    if len(value) != 9:
        return False
    p = re.compile("[0-9]{9}")
    if p.match(value):
        return True
    return False


validator = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid,
}


def solve_part2(input):
    """Calculate valid passports - improved validation"""

    def is_valid(record):
        """Test that required fields exist and they follow the specs"""
        required = validator.keys()
        for k in required:
            if k not in record:
                return False
            else:
                v = record[k]
                if not validator[k](v):
                    return False
        return True

    batch = parse_batch(input)
    result = [is_valid(r) for r in batch]
    return sum(result)


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: valid passports {solve_part1(data)}")
    print(f"Part 2: valid passports {solve_part2(data)}")


if __name__ == "__main__":
    main()
