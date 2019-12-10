#!/usr/bin/env python3

import sys


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


class IOInterface:
    """Simple IO Interface implementation"""
    outputs = []

    def input(self):
        return 1

    def output(self, value):
        self.outputs.append(value)
        print(f"stdout: {value}")


def processor(data, io):
    """Load the program into this processor, set the inputs and run the program

    :returns: result
    """

    def parse_opcode(code):
        """Return opcode and modes"""
        opcode = code % 100
        modes = [int(code/100)%10, int(code/1000)%10, int(code/10000)%10]
        return opcode, modes

    def read(idx, mode):
        """Read parameter based on mode"""
        if mode == 0:
            # position mode
            addr = prog[idx]
            assert addr >=0, f"Invalid addr at {idx}: {addr}"
            return prog[addr]
        else:
            # immediate mode
            return prog[idx]

    def add(idx, modes):
        """Addition operator: 01, arg, arg, result"""
        prog[prog[idx+3]] = read(idx+1, modes[0]) + read(idx+2, modes[1])
        return idx+4

    def mul(idx, modes):
        """Multiplication operator: 02, arg, arg, result*"""
        prog[prog[idx+3]] = read(idx+1, modes[0]) * read(idx+2, modes[1])
        return idx+4

    def inp(idx, modes):
        """Take input operator: 03, read input"""
        prog[prog[idx+3]] = io.input()
        return idx+2

    def out(idx, modes):
        """Output operator: 04, output value"""
        io.output(read(idx+1, modes[0]))
        return idx+2

    def halt(idx, modes):
        """Halt operator: 99"""
        return -1

    operands = {
        1: add,
        2: mul,
        3: inp,
        4: out,
        99: halt
    }

    # Load program
    prog = data.copy()

    # Run the program
    idx = 0
    try:
        while True:
            code, modes = parse_opcode(prog[idx])
            opcode = operands.get(code)
            assert opcode, f"operation failed at {idx} with opcode: {prog[idx]}"
            idx = opcode(idx, modes)
            if idx < 0:
                return prog
    except IndexError:
        assert False, f"Invalid index: {idx}"


def self_test():
    io1 = IOInterface()
    processor([3, 0, 4, 0, 99], io1)
    assert len(io1.outputs) == 1 and io1.outputs[0] == 1
    result = processor([1002, 4, 3, 4, 33], IOInterface())
    assert result == [1002, 4, 3, 4, 99]


assert len(sys.argv) == 2, "Missing input"

if sys.argv[1] == '-t' or sys.argv[1] == '--test':
    self_test()
else:
    data = read_data(sys.argv[1])
    io = IOInterface()
    result = processor(data, io)
