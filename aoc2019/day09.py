#!/usr/bin/env python3

import intcode
import sys
from intcode import IntCodeIO, IntCodeState


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


def run_boost(data, value):
    """Output the BOOST code"""
    io = IntCodeIO([value])
    state = IntCodeState(data)
    halted = intcode.run(state, io)
    assert halted, f"BOOST code not halted"
    assert len(io.stdout) == 1, f"BOOST output: {io.stdout}"
    return io.stdout[0]


assert len(sys.argv) == 2, "Missing input"

data = read_data(sys.argv[1])
print(f"TEST mode: {run_boost(data, 1)}")
print(f"BOOST mode: {run_boost(data, 2)}")
