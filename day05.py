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


def processor(data, io, debug=False):
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
        if debug:
            print(f"add({prog[idx+1]},{prog[idx+2]}) -> {prog[idx+3]} [idx:{idx},modes:{modes}]")
        prog[prog[idx+3]] = readreg(idx+1, modes[0]) + readreg(idx+2, modes[1])
        return idx+4

    def multiply(idx, modes):
        """Multiplication operator: 02, arg, arg, result*"""
        if debug:
            print(f"multiply({prog[idx+1]},{prog[idx+2]}) -> {prog[idx+3]} [idx:{idx},modes:{modes}]")
        prog[prog[idx+3]] = readreg(idx+1, modes[0]) * readreg(idx+2, modes[1])
        return idx+4

    def read_input(idx, modes):
        """Take input operator: 03, arg <- read input to arg"""
        if debug:
            print(f"read_input() -> {prog[idx+1]} [idx:{idx},modes:{modes}]")
        prog[prog[idx+1]] = io.input()
        return idx+2

    def write_output(idx, modes):
        """Output operator: 04, arg -> write arg to output output"""
        if debug:
            print(f"write_output({prog[idx+1]}) [idx:{idx},modes:{modes}]")
        io.output(readreg(idx+1, modes[0]))
        return idx+2

    def jmp_if_true(idx, modes):
        """Jump-if-true operator: 05, arg, result"""
        if debug:
            print(f"jmp_if_true({prog[idx+1]}) -> {prog[idx+2]} [idx:{idx},modes:{modes}]")
        if readreg(idx+1, modes[0]) != 0:
            return readreg(idx+2, modes[1])
        return idx+3

    def jmp_if_false(idx, modes):
        """Jump-if-false operator: 06, arg, result"""
        if debug:
            print(f"jmp_if_false({prog[idx+1]}) -> {prog[idx+2]} [idx:{idx},modes:{modes}]")
        if readreg(idx+1, modes[0]) == 0:
            return readreg(idx+2, modes[1])
        return idx+3

    def less_than(idx, modes):
        """Less-than operator: 07, arg, arg, result"""
        if debug:
            print(f"less_than({prog[idx+1]},{prog[idx+2]}) -> {prog[idx+3]} [idx:{idx},modes:{modes}]")
        if readreg(idx+1, modes[0]) < readreg(idx+2, modes[1]):
            prog[prog[idx+3]] = 1
        else:
            prog[prog[idx+3]] = 0
        return idx+4

    def equals(idx, modes):
        """Less-than operator: 08, arg, arg, result"""
        if debug:
            print(f"equals({prog[idx+1]},{prog[idx+2]}) -> {prog[idx+3]} [idx:{idx},modes:{modes}]")
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
        6: jmp_if_false,
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
            assert opcode, f"operation failed at {idx} opcode: {prog[idx]}"
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
    processor([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], io2)
    assert len(io2.stdout) == 1 and io2.stdout[0] == 1
    io3 = IOInterface(value=88)
    processor([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], io3)
    assert len(io3.stdout) == 1 and io3.stdout[0] == 0
    io4 = IOInterface(value=8)
    processor([3, 3, 1108, -1, 8, 3, 4, 3, 99], io4)
    assert len(io4.stdout) == 1 and io4.stdout[0] == 1
    io5 = IOInterface(value=0)
    processor([3, 3, 1108, -1, 8, 3, 4, 3, 99], io5)
    assert len(io5.stdout) == 1 and io5.stdout[0] == 0
    io6 = IOInterface(value=1)
    processor([3, 3, 1107, -1, 8, 3, 4, 3, 99], io6)
    assert len(io6.stdout) == 1 and io6.stdout[0] == 1
    io7 = IOInterface(value=8)
    processor([3, 3, 1107, -1, 8, 3, 4, 3, 99], io7)
    assert len(io7 .stdout) == 1 and io7.stdout[0] == 0
    io8 = IOInterface(value=1)
    processor([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], io8)
    assert len(io8.stdout) == 1 and io8.stdout[0] == 1
    io9 = IOInterface(value=0)
    processor([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], io9)
    assert len(io9.stdout) == 1 and io9.stdout[0] == 0
    prog = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    ioA = IOInterface(value=7)
    processor(prog, ioA)
    assert len(ioA.stdout) == 1 and ioA.stdout[0] == 999
    ioB = IOInterface(value=8)
    processor(prog, ioB)
    assert len(ioB.stdout) == 1 and ioB.stdout[0] == 1000
    ioC = IOInterface(value=9)
    processor(prog, ioC)
    assert len(ioC.stdout) == 1 and ioC.stdout[0] == 1001


assert len(sys.argv) == 2, "Missing input"

if sys.argv[1] == '-t' or sys.argv[1] == '--test':
    self_test()
else:
    data = read_data(sys.argv[1])
    io = IOInterface()
    result = processor(data, io)
    io2 = IOInterface(value=5)
    result = processor(data, io2, debug=False)
