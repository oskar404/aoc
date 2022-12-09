#!/usr/bin/env python3

import sys
import utils

# One Elf has the important job of loading all of the rucksacks with supplies
# for the jungle journey. Unfortunately, that Elf didn't quite follow the
# packing instructions, and so a few items now need to be rearranged.


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
    """The list of items for each rucksack is given as characters all on a
    single line. A given rucksack always has the same number of items in each of
    its two compartments, so the first half of the characters represent items in
    the first compartment, while the second half of the characters represent
    items in the second compartment.
    """
    return [line.strip() for line in data.splitlines() if len(line.strip()) != 0]


def solve_part1(data):
    """Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?
    """

    def get_priority(first, second):
        for item in first:
            if item in second:
                return priority(item)
        assert False

    result = 0
    data = parse_data(data)
    for line in data:
        first = line[: int(len(line) / 2)]
        second = line[int(len(line) / 2) :]
        result = result + get_priority(first, second)
    return result


def solve_part2(data):
    """Find the item type that corresponds to the badges of each three-Elf
    group. What is the sum of the priorities of those item types?"""

    def badge(elfos):
        for item in elfos[0]:
            if item in elfos[1] and item in elfos[2]:
                return item
        assert False

    result = 0
    data = parse_data(data)
    for idx in range(0, len(data), 3):
        result = result + priority(badge(data[idx : idx + 3]))
    return result


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = utils.read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
