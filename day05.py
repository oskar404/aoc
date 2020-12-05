#!/usr/bin/env python3

import sys


def solve_part1(input):
    def calculte_row(record):
        multipliers = [
            0b1000000,
            0b0100000,
            0b0010000,
            0b0001000,
            0b0000100,
            0b0000010,
            0b0000001,
        ]
        row = 0
        for i in range(7):
            flag = 1 if record[i] == "B" else 0
            row += flag * multipliers[i]
        return row

    def calculte_seat(record):
        multipliers = [0b100, 0b010, 0b001]
        seat = 0
        for i in range(3):
            flag = 1 if record[7 + i] == "R" else 0
            seat += flag * multipliers[i]
        return seat

    def calculate_seat_id(record):
        return calculte_row(record) * 8 + calculte_seat(record)

    result = [calculate_seat_id(r) for r in input]
    return (max(result), result)


def solve_part2(input):
    _, seat_ids = solve_part1(input)
    seat_ids = sorted(seat_ids)
    for i in range(len(seat_ids)):
        if seat_ids[i] + 1 != seat_ids[i + 1]:
            return seat_ids[i] + 1
    assert False


def read_data(file):
    with open(file) as f:
        return [line.strip() for line in f]


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: max seat id {solve_part1(data)[0]}")
    print(f"Part 1: my seat id {solve_part2(data)}")


if __name__ == "__main__":
    main()
