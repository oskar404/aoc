#!/usr/bin/env python3

import sys
import intcode


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


def restore_gravity_assist(data):
    prog = intcode.IntCodeState(data)
    prog.prog[1] = 12
    prog.prog[2] = 2
    intcode.run(prog, intcode.IntCodeIO())
    return prog.prog[0]


def search(data, result):
    """Iterate over the search space for correct input"""
    for noun in range(100):
        for verb in range(100):
            prog = intcode.IntCodeState(data)
            prog.prog[1] = noun
            prog.prog[2] = verb
            intcode.run(prog, intcode.IntCodeIO())
            if prog.prog[0] == result:
                return (noun, verb)


assert len(sys.argv) == 2, "Missing input"

data = read_data(sys.argv[1])
print(f"1202 program alarm state: {restore_gravity_assist(data)}")
noun, verb = search(data, 19690720)
print(f"Gravity assist 19690720 ({noun},{verb}) -> {100 * noun + verb} ")
