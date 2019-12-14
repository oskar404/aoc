#!/usr/bin/env python3

import itertools
import sys


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


class AmpIo:
    """Amp IO Interface implementation"""

    def __init__(self, phase, input=None):
        self._odx = 0
        self.stdout = []
        self._idx = 0
        self.stdin = [phase]
        if input != None:
            self.stdin.append(input)

    def input(self):
        self._idx += 1
        return self.stdin[self._idx-1]

    def has_input(self):
        return self._idx < len(self.stdin)

    def add_input(self, value):
        self.stdin.append(value)

    def output(self, value):
        self.stdout.append(value)

    def read_output(self):
        self._odx += 1
        return self.stdout[self._odx-1]

    def __str__(self):
        return f"stdin:{self.stdin} [{self._idx}] stdout:{self.stdout} [{self._odx}]"

    def __repr__(self):
        return f"stdin:{self.stdin} [{self._idx}] stdout:{self.stdout} [{self._odx}]"


class ProcessorState:
    """IntCode processor state.

    Load the program into this processor, set the inputs and run the program"""

    def __init__(self, data):
        self.prog = data.copy()  # Processor byte code
        self.idx = 0             # Current instruction
        self._halt = False       # Processor in halt state

    def read(self, offset=0):
        """Return value from memory"""
        return self.prog[self.idx + offset]

    def writ(self, value, offset=0):
        """Write value to memory"""
        self.prog[self.prog[self.idx + offset]] = value

    def next(self, offset=0):
        """Progress to next instruction"""
        self.idx += offset

    def jump(self, ptr):
        """Jump to instruction"""
        self.idx = ptr

    def halt(self):
        """Return true if halted"""
        return self._halt

    def hlcf(self):
        """Halt and catch fire"""
        self._halt = True

    def inst(self):
        """Return opcode and modes"""
        code = self.read()
        opcode = code % 100
        modes = [int(code/100)%10, int(code/1000)%10, int(code/10000)%10]
        return opcode, modes

    def parm(self, offset, mode):
        """Read parameter based on mode"""
        ptr = self.idx + offset
        value = self.prog[ptr]
        if mode == 0:   # position mode
            return self.prog[value]
        return value    # immediate mode


def null_debug(state, cmd, args, result, modes):
    """Null debugger, no output"""
    pass


def debugger(state, cmd, modes, args=0, result=None):
    """Dump processor instructions to stdout"""
    arglist = []
    for i in range(args):
        arglist.append(state.read(i+1))
    res =  state.read(args+1) if result else '<undef>'
    print(f"{cmd}({arglist}) -> {res} [idx:{state.idx},modes:{modes}]")


def processor(state, io, debug=null_debug):
    """IntCode processor.

    Load the program into this processor, set the inputs and run the program"""

    def add(modes):
        """Addition operator: 01, arg, arg, result"""
        debug(state, 'add', modes, 2, True)
        state.writ(state.parm(1, modes[0]) + state.parm(2, modes[1]), 3)
        state.next(4)
        return True

    def multiply(modes):
        """Multiplication operator: 02, arg, arg, result*"""
        debug(state, 'multiply', modes, 2, True)
        state.writ(state.parm(1, modes[0]) * state.parm(2, modes[1]), 3)
        state.next(4)
        return True

    def read_input(modes):
        """Take input operator: 03, arg <- read input to arg"""
        debug(state, 'read_input', modes, 0, True)
        if io.has_input():
            state.writ(io.input(), 1)
            state.next(2)
            return True
        return False

    def write_output(modes):
        """Output operator: 04, arg -> write arg to output output"""
        debug(state, 'write_output', modes, 1, False)
        io.output(state.parm(1, modes[0]))
        state.next(2)
        return True

    def jmp_if_true(modes):
        """Jump-if-true operator: 05, arg, result"""
        debug(state, 'jmp_if_true', modes, 1, True)
        if state.parm(1, modes[0]) != 0:
            state.jump(state.parm(2, modes[1]))
        else:
            state.next(3)
        return True

    def jmp_if_false(modes):
        """Jump-if-false operator: 06, arg, result"""
        debug(state, 'jmp_if_false', modes, 1, True)
        if state.parm(1, modes[0]) == 0:
            state.jump(state.parm(2, modes[1]))
        else:
            state.next(3)
        return True

    def less_than(modes):
        """Less-than operator: 07, arg, arg, result"""
        debug(state, 'less_than', modes, 2, True)
        if state.parm(1, modes[0]) < state.parm(2, modes[1]):
            state.writ(1, 3)
        else:
            state.writ(0, 3)
        state.next(4)
        return True

    def equals(modes):
        """Less-than operator: 08, arg, arg, result"""
        debug(state, 'equals', modes, 2, True)
        if state.parm(1, modes[0]) == state.parm(2, modes[1]):
            state.writ(1, 3)
        else:
            state.writ(0, 3)
        state.next(4)
        return True

    def halt(modes):
        """Halt operator: 99"""
        debug(state, 'halt', modes, 0, False)
        state.hlcf()
        return False

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

    assert not state.halt()
    try:
        while True:
            code, modes = state.inst()
            opcode = operands.get(code)
            assert opcode, f"operation failed at {state.idx} -> {state.read()}"
            if not opcode(modes):
                return state.halt()

    except IndexError:
        assert False, f"Invalid index: {state.idx}"


def amplify(data, phases):
    register = 0
    for phase in phases:
        io = AmpIo(phase, register)
        state = ProcessorState(data)
        processor(state, io)
        assert len(io.stdout) == 1
        register = io.stdout[0]
    return register


def max_thrust(data):
    """Search max thrust configuration (solution for part1)"""
    permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
    max_value = -1
    phase_config = []
    for config in permutations:
        thrust = amplify(data, config)
        if thrust > max_value:
            max_value = thrust
            phase_config = config
    return max_value, phase_config


def amp_feebback_loop(data, phases):
    thruster = 0
    input = 0
    amps = []
    for phase in phases:
        amps.append((ProcessorState(data), AmpIo(phase)))
    while True:
        halt = False
        for state, io in amps:
            io.add_input(input)
            halt = processor(state, io)
            input = io.read_output()
        thruster = input
        if halt:
            break
    return thruster


def more_thrust(data):
    """Search max thrust config with feedback loop (solution for part2)"""
    permutations = list(itertools.permutations([5, 6, 7, 8, 9]))
    max_value = -1
    phase_config = []
    for config in permutations:
        thrust = amp_feebback_loop(data, config)
        if thrust > max_value:
            max_value = thrust
            phase_config = config
    return max_value, phase_config


def self_test():
    # part1 tests
    thrust, phase = max_thrust([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
    assert thrust == 43210 and phase == (4,3,2,1,0), f"{thrust}, {phase}"
    thrust, phase = max_thrust([
        3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,
        99,0,0])
    assert thrust == 54321 and phase == (0,1,2,3,4), f"{thrust}, {phase}"
    thrust, phase = max_thrust([
        3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,
        31,31,1,32,31,31,4,31,99,0,0,0])
    assert thrust == 65210 and phase == (1,0,4,3,2), f"{thrust}, {phase}"
    # part2 tests
    thrust, phase = more_thrust([
        3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
        27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5])
    assert thrust == 139629729 and phase == (9,8,7,6,5), f"{thrust}, {phase}"
    thrust, phase = more_thrust([
            3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
            -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
            53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10])
    assert thrust == 18216 and phase == (9,7,8,5,6), f"{thrust}, {phase}"


assert len(sys.argv) == 2, "Missing input"

if sys.argv[1] == '-t' or sys.argv[1] == '--test':
    self_test()
else:
    data = read_data(sys.argv[1])
    thrust, phase = max_thrust(data)
    print(f"Max thrust: {thrust} {phase}")
    thrust, phase = more_thrust(data)
    print(f"More thrust: {thrust} {phase}")
