#!/usr/bin/env python3

import itertools
import sys


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


class AmpIo:
    """Amp IO Interface implementation"""

    def __init__(self, phase, input):
        self.stdout = []
        self.ioidx = -1
        self.stdin = [phase, input]

    def input(self):
        self.ioidx += 1
        return self.stdin[self.ioidx]

    def output(self, value):
        self.stdout.append(value)

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


def  amplify(data, phases):
    register = 0
    for phase in phases:
        io = AmpIo(phase, register)
        processor(data, io)
        assert len(io.stdout) == 1
        register = io.stdout[0]
    return register


def max_thrust(data):
    """Search max thruster configuration"""
    permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
    max_value = -1
    phase_config = []
    for config in permutations:
        thrust = amplify(data, config)
        if thrust > max_value:
            max_value = thrust
            phase_config = config
    return max_value, phase_config


def self_test():
    thrust, phase = max_thrust([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
    assert thrust == 43210 and phase == (4,3,2,1,0)
    thrust, phase = max_thrust([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0])
    assert thrust == 54321 and phase == (0,1,2,3,4)
    thrust, phase = max_thrust([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])
    assert thrust == 65210 and phase == (1,0,4,3,2)


assert len(sys.argv) == 2, "Missing input"

if sys.argv[1] == '-t' or sys.argv[1] == '--test':
    self_test()
else:
    data = read_data(sys.argv[1])
    thrust, phase = max_thrust(data)
    print(f"Max thrust: {thrust} {phase}")