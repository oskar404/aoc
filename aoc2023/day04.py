#!/usr/bin/env python3
"""
The gondola takes you up. Strangely, though, the ground doesn't seem to
be coming with you; you're not climbing a mountain. As the circle of
Snow Island recedes below you, an entire new landmass suddenly appears
above you! The gondola carries you to the surface of the new island and
lurches into the station.

As you exit the gondola, the first thing you notice is that the air here
is much warmer than it was on Snow Island. It's also quite humid. Is
this where the water source is?

The next thing you notice is an Elf sitting on the floor across the
station in what seems to be a pile of colorful square cards.

"Oh! Hello!" The Elf excitedly runs over to you. "How may I be of
service?" You ask about water sources.

"I'm not sure; I just operate the gondola lift. That does sound like
something we'd have, though - this is Island Island, after all! I bet
the gardener would know. He's on a different island, though - er, the
small kind surrounded by water, not the floating kind. We really need to
come up with a better naming scheme. Tell you what: if you can help me
with something quick, I'll let you borrow my boat and you can go visit
the gardener. I got all these scratchcards as a gift, but I can't figure
out what I've won."

The Elf leads you over to the pile of colorful cards. There, you
discover dozens of scratchcards, all with their opaque covering already
scratched off. Picking one up, it looks like each card has two lists of
numbers separated by a vertical bar (|): a list of winning numbers and
then a list of numbers you have. You organize the information into a
table (your puzzle input).
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
    """How many points are they worth in total?"""

    card_wins = []
    for card in data.splitlines():
        part1, part2 = card.split(":")[1].split("|")
        winning = set(map(int, part1.split()))
        numbers = set(map(int, part2.split()))
        wins = winning & numbers
        value = int(math.pow(2, len(wins) - 1)) if len(wins) > 0 else 0
        card_wins.append(value)
    return sum(card_wins)


def solve_part2(data: str) -> int:
    """how many total scratchcards do you end up with?"""
    cards = data.splitlines()
    size = len(cards)
    count = [1] * size
    for i, card in enumerate(cards):
        part1, part2 = card.split(":")[1].split("|")
        winning = set(map(int, part1.split()))
        numbers = set(map(int, part2.split()))
        wins = winning & numbers
        if len(wins) > 0:
            for j in range(i + 1, i + len(wins) + 1):
                if j >= size:
                    break
                count[j] += count[i]
    return sum(count)


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
