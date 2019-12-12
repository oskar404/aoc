#!/usr/bin/env python3

import sys


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


class IOInterface:
    """Simple IO Interface implementation"""

    def __init__(self, value=1):
        self.stdout = []
        self.line = 0
        self.stdin = value

    def input(self):
        return self.stdin

    def output(self, value):
        self.stdout.append(value)
        self.line += 1
        print(f"{self.line: >3}: {value}")

    def __str__(self):
        return f"stdin:{self.stdin} stdout:{self.stdout}"

    def __repr__(self):
        return f"stdin:{self.stdin} stdout:{self.stdout}"


def processor(data, io):
    """Load the program into this processor, set the inputs and run the program

    :returns: result
    """

    def parse_opcode(code):
        """Return opcode and modes"""
        opcode = code % 100
        modes = [int(code/100)%10, int(code/1000)%10, int(code/10000)%10]
        return opcode, modes

    def readreg(idx, mode):
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
        prog[prog[idx+3]] = readreg(idx+1, modes[0]) + readreg(idx+2, modes[1])
        return idx+4

    def multiply(idx, modes):
        """Multiplication operator: 02, arg, arg, result*"""
        prog[prog[idx+3]] = readreg(idx+1, modes[0]) * readreg(idx+2, modes[1])
        return idx+4

    def read_input(idx, modes):
        """Take input operator: 03, arg <- read input to arg"""
        prog[prog[idx+1]] = io.input()
        return idx+2

    def write_output(idx, modes):
        """Output operator: 04, arg -> write arg to output output"""
        io.output(readreg(idx+1, modes[0]))
        return idx+2

    def jmp_if_true(idx, modes):
        """Jump-if-true operator: 05, arg, result"""
        if readreg(idx+1, modes[0]) != 0:
            return prog[idx+2]
        return idx+3

    def jmp_if_false(idx, modes):
        """Jump-if-false operator: 06, arg, result"""
        if readreg(idx+1, modes[0]) == 0:
            return prog[idx+2]
        return idx+3

    def less_than(idx, modes):
        """Less-than operator: 07, arg, arg, result"""
        if readreg(idx+1, modes[0]) < readreg(idx+2, modes[1]):
            prog[prog[idx+3]] = 1
        else:
            prog[prog[idx+3]] = 0
        return idx+4

    def equals(idx, modes):
        """Less-than operator: 08, arg, arg, result"""
        if readreg(idx+1, modes[0]) == readreg(idx+2, modes[1]):
            prog[prog[idx+3]] = 1
        else:
            prog[prog[idx+3]] = 0
        return idx+4

    def halt(idx, modes):
        """Halt operator: 99"""
        return -1

    operands = {
        1: add,
        2: multiply,
        3: read_input,
        4: write_output,
        5: jmp_if_true,
        6: jmp_if_true,
        7: less_than,
        8: equals,
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
    assert len(io1.stdout) == 1 and io1.stdout[0] == 1
    result = processor([1002, 4, 3, 4, 33], IOInterface())
    assert result == [1002, 4, 3, 4, 99]
    io2 = IOInterface(value=8)
    result = processor([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], io2)
    assert len(io2.stdout) == 1 and io2.stdout[0] == 1
    io3 = IOInterface(value=88)
    processor([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], io3)
    assert len(io3.stdout) == 1 and io3.stdout[0] == 0


assert len(sys.argv) == 2, "Missing input"

if sys.argv[1] == '-t' or sys.argv[1] == '--test':
    self_test()
else:
    data = read_data(sys.argv[1])
    io = IOInterface()
    result = processor(data, io)
    io2 = IOInterface(value=5)
    result = processor(data, io2)
