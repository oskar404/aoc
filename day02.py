#!/usr/bin/env python3

import sys


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


def parse(prog):
    """Parse the program data"""

    def add(idx):
        """Addition operator"""
        prog[prog[idx+3]] = prog[prog[idx+1]] + prog[prog[idx+2]]
        return True

    def mul(idx):
        """Multiplication operator"""
        prog[prog[idx+3]] = prog[prog[idx+1]] * prog[prog[idx+2]]
        return True

    def halt(idx):
        """Halt operation"""
        return False

    operands = {
        1: add,
        2: mul,
        99: halt
    }
    idx = 0
    while True:
        opcode = operands.get(prog[idx])
        assert opcode, f"operation failed at {idx} with opcode: {opcode}"
        if opcode(idx):
            idx += 4
        else:
            return prog


assert len(sys.argv) == 2, "Missing input"
data = read_data(sys.argv[1])
program = data.copy()  # Keep original data intact
program[1] = 12
program[2] = 2
print(f"1202 program alarm state: {parse(program)[0]}")
