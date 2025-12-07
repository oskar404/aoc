#!/usr/bin/env python3
"""
What's the actual password to open the door?
"""

import argparse


def solve_part1(input: str) -> int:
    """Number of times zero is hit. Start from 50"""

    zeroes = 0
    position = 50
    with open(input, mode="r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            direction = 1 if line[0] == "R" else -1
            clicks = int(line[1:])
            position = (position + (direction * clicks)) % 100
            if position == 0:
                zeroes = zeroes + 1
    return zeroes



def solve_part2(data: str):
    """path 2 stub"""

    pass


def read_input(input_file: str) -> str:
    """Read input file"""
    with open(input_file, mode="r", encoding="utf-8") as infile:
        return infile.read()


def create_parser() -> argparse.ArgumentParser:
    """ArgumentParser factory method"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
        epilog="More info on https://adventofcode.com/2025",
    )
    parser.add_argument(
        "file",
        default="input01.txt",
        help='Path to input file. If not given tries to read "input01.txt"',
        metavar="FILE",
        nargs="?",
    )
    return parser


def main():
    """Main entry for script"""
    parser = create_parser()
    args = parser.parse_args()
    result = solve_part1(args.file)
    print(f"Part 1: {result}")
    result = solve_part2(args.file)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
