#!/usr/bin/env python3
"""
The ferry quickly brings you across Island Island. After asking around,
you discover that there is indeed normally a large pile of sand
somewhere near here, but you don't see anything besides lots of water
and the small island where the ferry has docked.

As you try to figure out what to do next, you notice a poster on a wall
near the ferry dock. "Boat races! Open to the public! Grand prize is an
all-expenses-paid trip to Desert Island!" That must be where the sand
comes from! Best of all, the boat races are starting in just a few
minutes.

You manage to sign up as a competitor in the boat races just in time.
The organizer explains that it's not really a traditional race -
instead, you will get a fixed amount of time during which your boat has
to travel as far as it can, and you win if your boat goes the farthest.
"""
import argparse
import math
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


def solve_part1(data: str) -> int:
    """What do you get if you multiply these numbers together?"""

    lines = data.splitlines()
    times = [int(i) for i in lines[0].split(":")[1].strip().split()]
    distances = [int(i) for i in lines[1].split(":")[1].strip().split()]
    faster = [0] * len(times)

    assert len(times) == len(distances)

    for i, time in enumerate(times):
        for j in range(1, time):
            distance = j * (time - j)
            if distance > distances[i]:
                faster[i] += 1

    return math.prod(faster)


def main():
    """Main entry for script"""
    parser = create_parser()
    args = parser.parse_args()
    data = read_input(args.file)
    result = solve_part1(data)
    print(f"Part 1: {result}")


if __name__ == "__main__":
    main()
