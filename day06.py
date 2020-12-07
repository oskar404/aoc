#!/usr/bin/env python3

import sys


def solve_part1(input):
    def parse(input):
        batch = []
        record = set()
        for line in [bl.strip() for bl in input.splitlines()]:
            if line:
                record = record.union(set(line))
            else:
                if record:
                    batch.append(record)
                record = set()
        if record:
            batch.append(record)
        return batch

    data = parse(input)
    result = [len(r) for r in data]
    return sum(result)


def solve_part2(input):
    def parse(input):
        batch = []
        record = []
        for line in [bl.strip() for bl in input.splitlines()]:
            if line:
                record.append(set(line))
            else:
                if record:
                    batch.append(record)
                record = []
        if record:
            batch.append(record)
        return batch

    data = parse(input)
    result = [len(set.intersection(*r)) for r in data]
    return sum(result)


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: sum of 'yes' {solve_part1(data)}")
    print(f"Part 2: sum of 'yes' {solve_part2(data)}")


if __name__ == "__main__":
    main()
