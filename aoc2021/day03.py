#!/usr/bin/env python3

import sys


def solve_part1(input):
    """Return gamma, epsilon and power"""
    # transpose with numpy would be cool, but didn't bother to install it
    # trust that all input lines are same length
    sums = len(input[0]) * [0]  # init with zeroes
    for line in input:
        for idx in range(len(line)):
            sums[idx] = sums[idx] + int(line[idx])
    limit = len(input) / 2
    gamma = 0
    epsilon = 0
    for value in sums:
        if value > limit:  # Might be problem of greater or equal (>=)
            gamma = (gamma << 1) + 1
            epsilon = (epsilon << 1) + 0
        else:
            gamma = (gamma << 1) + 0
            epsilon = (epsilon << 1) + 1
    return (gamma, epsilon, gamma * epsilon)


def solve_part2(input):
    """Return oxygen generator rating, CO2 scrubber rating, life support rating"""

    def oxygen_selector(list1, list2):
        return list1 if len(list1) >= len(list2) else list2

    def co2_selector(list1, list2):
        return list1 if len(list1) < len(list2) else list2

    def algortihm(data, selector):
        """Return the rate value as int"""
        for idx in range(len(data[0])):
            if len(data) == 1:
                return int(data[0], base=2)
            ones = []
            zeroes = []
            for v in data:
                if v[idx] == "1":
                    ones.append(v)
                else:
                    zeroes.append(v)
            data = selector(ones, zeroes)
        assert False

    oxygen_rate = algortihm(input, oxygen_selector)
    co2_rate = algortihm(input, co2_selector)
    return oxygen_rate, co2_rate, oxygen_rate * co2_rate


def read_data(file):
    with open(file) as f:
        return [line.strip() for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    g, e, p = solve_part1(data)
    print(f"Part 1: gamma: {g} ({bin(g)}), epsilon: {e} ({bin(e)}) power: {p}")
    o, co2, life = solve_part2(data)
    print(
        f"Part 2: oxygen: {o} ({bin(o)}), co2: {co2} ({bin(co2)}) life support: {life}"
    )


if __name__ == "__main__":
    main()
