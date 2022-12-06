#!/usr/bin/env python3

import sys

# The expedition can depart as soon as the final supplies have been unloaded
# from the ships. Supplies are stored in stacks of marked crates, but because
# the needed supplies are buried under many other crates, the crates need to be
# rearranged.


def parse_data(data):
    """They do, however, have a drawing of the starting stacks of crates and the
    rearrangement procedure
    """

    def get_op(line):
        """Get index 1, 3 and 5 from splitted string like "move 1 from 4 to 1" """
        tokens = line.split()
        return [int(tokens[1]), int(tokens[3]), int(tokens[5])]

    stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    operations = []

    for line in data.splitlines():
        if len(line) == 0:
            continue
        if line[0] == "m":
            # operation e.g. "move 1 from 4 to 1"
            operations.append(get_op(line))
        else:
            for idx in range(1, len(line), 4):
                if line[idx].isalpha():
                    stack_id = int((idx - 1) / 4 + 1)
                    stacks[stack_id].append(line[idx])

    for stack in stacks.values():
        stack.reverse()

    return (stacks, operations)


def solve_part1(data):
    """After the rearrangement procedure completes, what crate ends up on top of
    each stack?
    """
    stacks, operations = parse_data(data)
    for crates, from_stack, to_stack in operations:
        for _ in range(0, crates):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)

    result = [stack.pop() for _, stack in stacks.items() if stack]
    return "".join(result).strip()


def solve_part2(data):
    """Some mud was covering the writing on the side of the crane, and you
    quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover
    9001.
    """
    stacks, operations = parse_data(data)
    for cnt, from_stack, to_stack in operations:
        crates = stacks[from_stack][-1 * cnt :]
        stacks[from_stack] = stacks[from_stack][: -1 * cnt]
        stacks[to_stack].extend(crates)

    result = [stack.pop() for _, stack in stacks.items() if stack]
    return "".join(result).strip()


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
