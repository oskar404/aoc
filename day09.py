#!/usr/bin/env python3

import intcode
import sys
from intcode import IntCodeIO, IntCodeState


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


def solve_part1(data):
    """Output the BOOST keycode"""
    io = IntCodeIO([1])
    state = IntCodeState(data, debug=True)
    halted = intcode.run(state, io, debug=intcode.cmd_debugger)
    assert halted, f"BOOST code not halted"
    assert len(io.stdout) == 1, f"BOOST output: {io.stdout}"
    return io.stdout[0]


assert len(sys.argv) == 2, "Missing input"

data = read_data(sys.argv[1])
boost_code = solve_part1(data)
print(f"BOOST code: {boost_code}")
