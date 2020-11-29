#!/usr/bin/env python3

import sys
import intcode


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


assert len(sys.argv) == 2, "Missing input"

data = read_data(sys.argv[1])
io = intcode.IntCodeIO([1])
state = intcode.IntCodeState(data)
intcode.run(state, io)
print(f"Diagnostics (input:{io.stdin[0]}): {io.stdout[-1]}")
io2 = intcode.IntCodeIO([5])
state2 = intcode.IntCodeState(data)
intcode.run(state2, io2)
print(f"Diagnostics (input:{io2.stdin[0]}): {io2.stdout[-1]}")
