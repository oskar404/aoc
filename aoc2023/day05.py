#!/usr/bin/env python3
"""
You take the boat and find the gardener right where you were told he
would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that
Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it
with! Can't make snow with dirty water. Don't worry, I'm sure we'll get
more sand soon; we only turned off the water a few days... weeks... oh
no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely
forgot to check why we stopped getting more sand! There's a ferry
leaving soon that is headed over in that direction - it's much faster
than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another.
"While you wait for the ferry, maybe you can help us with our food
production problem. The latest Island Island Almanac just arrived and
we're having trouble making sense of it."
"""
import argparse
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


class RangeMap:
    """Provides a source range mapped to destination range"""

    def __init__(self, src: int, dst: int, rng: int) -> None:
        """Initialize with source, destination, and range"""
        self.src = src
        self.dst = dst
        self.rng = rng

    def __contains__(self, src: int) -> bool:
        """Return True if src is in range"""
        return src in range(self.src, self.src + self.rng)

    def __getitem__(self, src: int) -> int:
        """Returns value for src. Does not check if inside range"""
        return self.dst + (src - self.src)

    def __repr__(self) -> str:
        """Return string representation"""
        return f"({self.src}-{self.src + self.rng})->({self.dst}-{self.dst + self.rng})"


class AlmanacMap:
    """Maps source to destination based on the input data"""

    def __init__(self, lines: list[str]) -> None:
        """Initialize with data like

        seed-to-soil map:
        50 98 2
        52 50 48
        """
        self.name = lines.pop(0).split()[0]  # remove header
        self.ranges = []
        for line in lines:
            dst, src, rng = map(int, line.strip().split())
            self.ranges.append(RangeMap(src, dst, rng))

    def __getitem__(self, key: int) -> int:
        """Get value for key"""
        for rng in self.ranges:
            if key in rng:
                return rng[key]
        return key

    def __repr__(self) -> str:
        """Return string representation"""
        return f"{self.name}\n{self.ranges}\n"


def parse(data: str) -> tuple[list[int], list[AlmanacMap]]:
    """Parse data into a list of AlmanacMap objects"""
    almanac: list[AlmanacMap] = []
    pages = data.split("\n\n")
    seeds: list[int] = list(map(int, pages.pop(0).split(":")[1].strip().split()))
    for page in pages:
        almanac.append(AlmanacMap(page.splitlines()))
    return seeds, almanac


def solve_part1(data: str) -> int:
    """What is the lowest location number that corresponds to any of the
    initial seed numbers?
    """
    seeds, almanac = parse(data)

    for page in almanac:
        cache = [-1] * len(seeds)
        for i, seed in enumerate(seeds):
            cache[i] = page[seed]
        seeds = cache
    return min(seeds)


def main():
    """Main entry for script"""
    parser = create_parser()
    args = parser.parse_args()
    data = read_input(args.file)
    result = solve_part1(data)
    print(f"Part 1: {result}")


if __name__ == "__main__":
    main()
