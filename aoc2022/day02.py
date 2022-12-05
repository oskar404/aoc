#!/usr/bin/env python3

import sys

# To decide whose tent gets to be closest to the snack storage, a giant
# Rock Paper Scissors tournament is already in progress.


def parse_data(data):
    """The first column is what your opponent is going to play: A for Rock,
    B for Paper, and C for Scissors. The second column--
    """
    return [line for line in data.splitlines() if len(line.strip()) != 0]


def solve_part1(data):
    """Since you can't be sure if the Elf is trying to help you or trick you,
    you should calculate the score you would get if you were to follow the
    strategy guide.
    """

    # Rock (A,X,1) defeats Scissors (C,Z,3),
    # Scissors (C,Z,3) defeats Paper (B,Y,2), and
    # Paper (B,Y,2) defeats Rock (A,X,1).
    # If both players choose the same shape, the round instead ends in a draw.
    points = {
        "A X": 1 + 3,  # Rock - Rock (draw)
        "A Y": 2 + 6,  # Rock - Paper (win)
        "A Z": 3 + 0,  # Rock - Scissors (lose)
        "B X": 1 + 0,  # Paper - Rock (lose)
        "B Y": 2 + 3,  # Paper - Paper (draw)
        "B Z": 3 + 6,  # Paper - Scissors (win)
        "C X": 1 + 6,  # Scissors - Rock (win)
        "C Y": 2 + 0,  # Scissors - Paper (lose)
        "C Z": 3 + 3,  # Scissors - Scissors (draw)
    }

    result = 0
    data = parse_data(data)
    for line in data:
        result = result + points[line]
    return result


def solve_part2(data):
    """The Elf finishes helping with the tent and sneaks back over to you.
    "Anyway, the second column says how the round needs to end: X means you need
    to lose, Y means you need to end the round in a draw, and Z means you need
    to win. Good luck!"
    """

    # If both players choose the same shape, the round instead ends in a draw.
    points = {
        "A X": 3 + 0,  # Rock - lose
        "A Y": 1 + 3,  # Rock - draw
        "A Z": 2 + 6,  # Rock - win
        "B X": 1 + 0,  # Paper - lose
        "B Y": 2 + 3,  # Paper - draw
        "B Z": 3 + 6,  # Paper - win
        "C X": 2 + 0,  # Scissors - lose
        "C Y": 3 + 3,  # Scissors - draw
        "C Z": 1 + 6,  # Scissors - win
    }

    result = 0
    data = parse_data(data)
    for line in data:
        result = result + points[line]
    return result


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
