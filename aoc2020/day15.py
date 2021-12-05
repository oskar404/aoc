#!/usr/bin/env python3

import sys


puzzle_input = [8, 0, 17, 4, 1, 12]


def solve_puzzle(input, turns=2020, verbose=False):
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


def main():
    print(f"Part 1: say 2020th number : {solve_puzzle(puzzle_input)}")
    print(f"Part 2: say 30000000th number : {solve_puzzle(puzzle_input, 30000000)}")


if __name__ == "__main__":
    main()
