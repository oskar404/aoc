#!/usr/bin/env python3

import re
import sys
from enum import Enum
from typing import List


class Rotation(Enum):
    """Enumerates possible permutations of the tile"""

    # T=top(1), R=right(2), B=bottom(3), L=left(4)
    TRBL = 1  # A: 1234 - Original position
    RBLT = 2  # B: 2341 - Counter clockwise rotation one step
    BLTR = 3  # C: 3412 - Counter clockwise rotation two steps
    LTRB = 4  # D: 4123 - Clockwise rotation three steps
    TLBR = 5  # E: 1432 - Flip around vertical axis
    BRTL = 6  # F: 3214 - Flip around horizontal axis
    LBRT = 7  # G: 4321 - Flip around vertical axis and rotate counter clockwise
    RTLB = 8  # H: 2143 - Flip around horizontal axisand rotate clockwise


class Tile:
    def __init__(self, tile: int, pic: List[str]):
        self.tile = tile
        self.pic = pic
        self.T = pic[0]
        self.R = "".join([r[-1] for r in pic])
        self.B = pic[-1]
        self.L = "".join([r[0] for r in pic])

    def __str__(self):
        return f"tile {self.tile}: [top:{self.T}, right:{self.R}, bottom:{self.B}, left:{self.L}]"

    def __repr__(self):
        return str(self)


def parse(input: str):
    """Return list of Tiles"""
    result = []

    tile = None
    pic = []
    pattern = re.compile(r"Tile ([0-9]+):")
    for l in [l.strip() for l in input.splitlines() if l.strip()]:
        if l.startswith("Tile"):
            if tile and pic:
                result.append(Tile(tile, pic))
            tile = int(pattern.match(l).group(1))
            pic = []
        else:
            pic.append(l)

    return result


def solve_part1(input: str, verbose=False):
    """Return tuple with number of matches, match regex and matched rows"""
    pics = parse(input)

    if verbose:
        for p in pics:
            print(f"{p}")

    return 0


def solve_part2(input: str, verbose=False):
    pass


def read_data(file: str):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: check sum: {solve_part1(data)}")


if __name__ == "__main__":
    main()
