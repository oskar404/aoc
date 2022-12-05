#!/usr/bin/env python3

import sys

# One important consideration is food - in particular, the number of Calories
# each Elf is carrying (your puzzle input)
#
# Find the Elf carrying the most Calories. How many total Calories is that
# Elf carrying?


def solve_part1(data):
    """Find the Elf carrying the most Calories.
    How many total Calories is that Elf carrying?
    """
    max_calories = 0
    calories = 0
    for line in data.splitlines():
        if line.isdigit():
            calories = calories + int(line)
        else:
            max_calories = max(max_calories, calories)
            calories = 0
    return max_calories


def solve_part2(data):
    """Elves would instead like to know the total Calories carried by the top
    three Elves carrying the most Calories.
    """

    def update_max_list(calories):
        current_min = min(max_calories)
        idx = max_calories.index(current_min)
        max_calories[idx] = max(current_min, calories)

    max_calories = [0, 0, 0]
    calories = 0
    for line in data.splitlines():
        if line.isdigit():
            calories = calories + int(line)
        else:
            update_max_list(calories)
            calories = 0
    update_max_list(calories)

    return sum(max_calories)


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
