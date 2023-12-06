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
from typing import Optional


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


class Range:
    """Provides a range mapped to destination range"""

    def __init__(self, start: int, rng: int) -> None:
        """Initialize with start and range"""
        self.start = start
        self.end = start + (rng - 1)

    def __repr__(self) -> str:
        """Return string representation"""
        return f"({self.start}-{self.end})"

    def min(self) -> int:
        """Return minimum value of range"""
        return self.start

    def max(self) -> int:
        """Return maximum value of range"""
        return self.end


class RangeMap:
    """Provides a source range mapped to destination range"""

    def __init__(self, src: int, dst: int, rng: int) -> None:
        """Initialize with source, destination, and range"""
        self.first = src
        self.last = src + rng - 1
        self.dst = dst

    def __contains__(self, src: int) -> bool:
        """Return True if src is in range"""
        return src in range(self.first, self.last + 1)

    def __getitem__(self, src: int) -> int:
        """Returns value for src. Does not check if inside range"""
        return self.dst + (src - self.first)

    def __repr__(self) -> str:
        """Return string representation"""
        sources = f"{self.first}-{self.last}"
        destinations = f"{self.dst}-{self.dst + (self.last - self.first)}"
        return f"({sources})->({destinations})"

    def map_range(
        self, src: Range
    ) -> Optional[tuple[Range | None, Range, Range | None]]:
        """Return list of ranges if part source range

        Returns None if source range is not in this range
        If in range, first item is unmapped range before mapping, second
        is mapped range, and last one is unmapped range after mapping
        """
        # Check outside range
        if src.max() < self.first or src.min() > self.last:
            return None
        # Must be inside range
        before = None
        mapped = None
        after = None
        start = src.min()
        end = src.max()
        if src.min() < self.first:
            before = Range(src.min(), self.first - src.min())
            start = self.first
        if src.max() > self.last:
            after = Range(self.last + 1, src.max() - self.last)
            end = self.last
        mapped = Range(self.dst + (start - self.first), end - start + 1)
        return before, mapped, after


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

    def map_range(self, rng: Range) -> list[Range]:
        """Return list of Ranges"""
        results: list[Range] = []
        cache = [rng]
        for mapper in self.ranges:
            data = cache
            cache = []
            for item in data:
                mapping = mapper.map_range(item)
                if mapping:
                    before, mapped, after = mapping
                    results.append(mapped)
                    if before:
                        cache.append(before)
                    if after:
                        cache.append(after)
                else:
                    cache.append(item)
        if cache:
            results.extend(cache)
        return results


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


def solve_part2(data: str) -> int:
    """What is the lowest location number that corresponds to any of the
    initial seed numbers?
    """
    init_seeds, almanac = parse(data)
    seeds = [
        Range(init_seeds[i], init_seeds[i + 1]) for i in range(0, len(init_seeds), 2)
    ]
    for page in almanac:
        cache: list[Range] = []
        for seed in seeds:
            cache = cache + page.map_range(seed)
        seeds = cache
    return min(seed.min() for seed in seeds)


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
