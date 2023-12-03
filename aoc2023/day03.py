#!/usr/bin/env python3
"""
You and the Elf eventually reach a gondola lift station; he says the
gondola lift will take you up to the water source, but this is as far as
he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a
problem: they're not moving.

    "Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't
working right now; it'll still be a while before I can fix it." You
offer to help.
"""

import argparse
import collections
import pathlib
import re


def _day(filename: str = __file__) -> str:
    """Return day number based on file name"""
    name = pathlib.Path(filename).name
    return str(re.findall(r"\d+", name)[0])


# default input file
INPUT = f"input{_day()}.txt"

# URL for adventofcode.com day puzzle
URL = f"https://adventofcode.com/2023/day/{int(_day())}"


def create_parser() -> argparse.ArgumentParser:
    """ArgumentParser factory method"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
        epilog=f"More info on {URL}",
    )
    parser.add_argument(
        "file",
        default=INPUT,
        help=f'Path to input file. If not given tries to read "{INPUT}"',
        metavar="FILE",
        nargs="?",
    )
    return parser


def read_input(input_file: str) -> str:
    """Read input file"""
    with open(input_file, mode="r", encoding="utf-8") as infile:
        return infile.read()


def parse(data: str) -> set[tuple[int, int]]:
    """Parse input data and return a set with the coordinates of
    missing engine parts"""

    parts = set()
    rows = data.splitlines()
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char not in "0123456789.":
                parts.add((x, y))
    return parts


def solve_part1(data: str) -> int:
    """What is the sum of all of the part numbers in the engine
    schematic?
    """

    part_list = parse(data)

    def get_edges(row: int, start_col: int, end_col: int) -> set[tuple[int, int]]:
        """Return the edge coordinates of a current code"""
        return {
            (x, y)
            for y in (row - 1, row, row + 1)
            for x in range(start_col - 1, end_col + 1)
        }

    part_codes = collections.defaultdict(list)
    rows = data.splitlines()
    for y, row in enumerate(rows):
        for code in re.finditer(r"\d+", row):
            edges = get_edges(y, code.start(), code.end())
            for part in edges & part_list:
                part_codes[part].append(int(code.group()))

    return sum(sum(part) for part in part_codes.values())


def main():
    """Main entry for script"""
    parser = create_parser()
    args = parser.parse_args()
    data = read_input(args.file)
    result = solve_part1(data)
    print(f"Part 1: {result}")


if __name__ == "__main__":
    main()
