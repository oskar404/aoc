""" Utilities for all solutions to get rid of copy-pasta """

import argparse
import re


# Flag for solutions to use bit more verbosity
VERBOSE = False


def read_data(input_file):
    """Read input file"""
    with open(input_file, mode="r", encoding="utf-8") as infile:
        return infile.read()


def get_day(user):
    """Extract day number from file string e.g. "day10.py" """
    pattern = re.compile(".*day(\\d\\d)\\.py")
    result = pattern.match(user)
    return result.group(1)


def read_input(user):
    """Parse command line arguments and read data from file.
    Returns the data
    """
    day = get_day(user)

    parser = argparse.ArgumentParser(
        description="Advent of Code solution",
        epilog="More info on https://adventofcode.com/2022",
    )
    parser.add_argument(
        "file",
        default=f"input{day}.txt",
        help=f'Path to input file. If not given tries to read "input{day}.txt"',
        metavar="FILE",
        nargs="?",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        help="Increase verbosity of the solution (if available)",
        action="store_true",
    )
    args = parser.parse_args()

    global VERBOSE  # pylint: disable=global-statement
    VERBOSE = args.verbose

    return read_data(args.file)
