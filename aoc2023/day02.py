#!/usr/bin/env python3
"""
You're launched high into the atmosphere! The apex of your trajectory
just barely reaches the surface of a large island floating in the sky.
You gently land in a fluffy pile of leaves. It's quite cold, but you
don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for
the lack of snow. He'll be happy to explain the situation, but it's a
bit of a walk, so you have some time. They don't get many visitors up
here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are
either red, green, or blue. Each time you play this game, he will hide a
secret number of cubes of each color in the bag, and your goal is to
figure out information about the number of cubes.
"""

import argparse


def parse(data: str) -> dict[int, list[dict[str, int]]]:
    """Parse input data"""
    games = {}
    for line in data.splitlines():
        tokens = line.split(":")
        game_id = int(tokens[0].strip().split(" ")[1])
        game = []
        draws = tokens[1].strip().split(";")
        for draw in draws:
            draw_result = {"red": 0, "green": 0, "blue": 0}
            parts = draw.strip().split(",")
            for part in parts:
                count, color = part.strip().split(" ")
                draw_result[color.strip()] = int(count.strip())
            game.append(draw_result)
        games[game_id] = game
    return games


def solve_part1(data: str) -> int:
    """What is the sum of all of the calibration values?"""

    def possible(draw: dict[str, int]) -> bool:
        """Check if draw is possible with the cubes in the bag"""
        in_bag = {"red": 12, "green": 13, "blue": 14}
        for color, count in draw.items():
            if in_bag[color] < count:
                return False
        return True

    games = parse(data)
    total = 0
    for game_id, game in games.items():
        # get first and last digit
        valid = True
        for draw in game:
            if not possible(draw):
                valid = False
                break
        if valid:
            total += game_id
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
        default="input02.txt",
        help='Path to input file. If not given tries to read "input02.txt"',
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


if __name__ == "__main__":
    main()
