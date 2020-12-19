#!/usr/bin/env python3

import sys


puzzle_input = [8, 0, 17, 4, 1, 12]


def solve_part1(input, turns=2020, verbose=False):
    if verbose:
        print(f"input: {input}")

    mem = {}
    for i, n in enumerate(input[:-1]):
        mem[n] = i + 1
    prev = input[-1]
    for i in range(len(input), turns):
        speak = 0
        if prev in mem:
            speak = i - mem[prev]
        mem[prev] = i
        prev = speak

    if verbose:
        print(f"mem: {mem}")

    return prev


def solve_part2(input, verbose=False):
    pass


def main():
    print(f"Part 1: say 2020th number : {solve_part1(puzzle_input)}")


if __name__ == "__main__":
    main()
