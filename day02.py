#!/usr/bin/env python3

import sys


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


def processor(data, noun, verb):
    """Load the program into this processor, set the inputs and run the program

    :returns: result
    """

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

    # Load program and set inputs
    prog = data.copy()
    prog[1] = noun
    prog[2] = verb

    # Run the program
    idx = 0
    try:
        while True:
            opcode = operands.get(prog[idx])
            assert opcode, f"operation failed at {idx} with opcode: {opcode}"
            if opcode(idx):
                idx += 4
            else:
                return prog[0]
    except IndexError:
        assert False, f"Invalid input: {noun} {verb}"


def search(data, result):
    """Iterate over the search space for correct input"""
    for noun in range(100):
        for verb in range(100):
            output = processor(data, noun, verb)
            if output == result:
                return (noun, verb)


assert len(sys.argv) == 2, "Missing input"
data = read_data(sys.argv[1])
print(f"1202 program alarm state: {processor(data, 12, 2)}")
noun, verb = search(data, 19690720)
print(f"Gravity assist 19690720 ({noun},{verb}) -> {100 * noun + verb} ")
