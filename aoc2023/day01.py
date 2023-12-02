#!/usr/bin/env python3
"""
Something is wrong with global snow production, and you've been selected to
take a look. The Elves have even given you a map; on it, they've used stars
to mark the top fifty locations that are likely to be having problems.

As they're making the final adjustments, they discover that their calibration
document (your puzzle input) has been amended by a very young Elf who was
apparently just excited to show off her art skills. Consequently, the Elves
are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line
originally contained a specific calibration value that the Elves now need to
recover. On each line, the calibration value can be found by combining the
first digit and the last digit (in that order) to form a single two-digit
number.
"""

import argparse


def solve_part1(data: str) -> int:
    """What is the sum of all of the calibration values?"""

    def find_digit(string: str) -> int:
        """Find first digit in string"""
        for char in string:
            if char.isdigit():
                return int(char)
        assert False, "No digit found"

    total = 0
    for line in data.splitlines():
        # get first and last digit
        first = find_digit(line)
        last = find_digit(reversed(line))
        # combine to form a single two-digit number
        number = first * 10 + last
        # add to sum
        total += number
    return total


valid_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solve_part2(data: str):
    """path 2 stub"""

    def find_digit(string: str, reverse: bool = False) -> int:
        """Find first digit in string"""
        if reverse:
            string = string[::-1]
        for i, char in enumerate(string):
            if char.isdigit():
                return int(char)
            # check is string starts with a valid digit name
            candidate = string[i : i + 5]
            for key, value in valid_digits.items():
                if reverse:
                    key = key[::-1]
                if candidate.startswith(key):
                    return value
        assert False, "No digit found"

    total = 0
    for line in data.splitlines():
        # get first and last digit
        first = find_digit(line)
        last = find_digit(line, reverse=True)
        # combine to form a single two-digit number
        number = first * 10 + last
        # add to sum
        total += number
    return total


def read_input(input_file: str) -> str:
    """Read input file"""
    with open(input_file, mode="r", encoding="utf-8") as infile:
        return infile.read()


def create_parser() -> argparse.ArgumentParser:
    """ArgumentParser factory method"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
        epilog="More info on https://adventofcode.com/2023",
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
    data = read_input(args.file)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
