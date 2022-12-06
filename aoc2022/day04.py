#!/usr/bin/env python3

import sys

# Space needs to be cleared before the last supplies can be unloaded from the
# ships, and so several Elves have been assigned the job of cleaning up sections
# of the camp. Every section has a unique ID number, and each Elf is assigned a
# range of section IDs.


def priority(char):
    """To help prioritize item rearrangement, every item type can be converted
    to a priority:

    - Lowercase item types a through z have priorities 1 through 26.
    - Uppercase item types A through Z have priorities 27 through 52.
    """
    if char.isupper():
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1


def parse_data(data):
    """However, as some of the Elves compare their section assignments with each
    other, they've noticed that many of the assignments overlap.
    """

    def assignment(spec):
        start, end = spec.split("-")
        start = int(start)
        end = int(end) + 1
        return set(range(start, end))

    pairs = [
        line.strip().split(",") for line in data.splitlines() if len(line.strip()) != 0
    ]
    result = []
    for first, second in pairs:
        result.append([assignment(first), assignment(second)])
    return result


def solve_part1(data):
    """In how many assignment pairs does one range fully contain the other?"""
    result = 0
    data = parse_data(data)
    for row in data:
        if row[0].issubset(row[1]) or row[1].issubset(row[0]):
            result = result + 1
    return result


def solve_part2(data):
    """In how many assignment pairs do the ranges overlap?"""
    result = 0
    data = parse_data(data)
    for row in data:
        if row[0].intersection(row[1]):
            result = result + 1
    return result


def read_data(file):
    with open(file, mode="r", encoding="utf-8") as infile:
        return infile.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
