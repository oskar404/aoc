#!/usr/bin/env python3
"""IntCode computer

The IntCode computer uses list of integers as instruction set"""


class IntCodeIO:
    """IntCode Computer IO Interface"""

    def __init__(self, input_values=None):
        self._idx = 0
        self.stdin = input_values if not None else []
        self._odx = 0
        self.stdout = []

    def read_in(self):
        """Read next int from input queue"""
        self._idx += 1
        return self.stdin[self._idx-1]

    def has_in(self):
        """Return true if input queue has data"""
        return self._idx < len(self.stdin)

    def add_in(self, value):
        """Add int value to input queue"""
        self.stdin.append(value)

    def write_out(self, value):
        """Write int value to output queue"""
        self.stdout.append(value)

    def next_out(self):
        """Return next item from output queue"""
        self._odx += 1
        return self.stdout[self._odx-1]

    def __str__(self):
        return f"stdin:{self.stdin} [{self._idx}] stdout:{self.stdout} [{self._odx}]"

    def __repr__(self):
        return f"stdin:{self.stdin} [{self._idx}] stdout:{self.stdout} [{self._odx}]"


class IntCodeState:
    """IntCode processor state.

    Returns True if halted. If False waiting for input."""

    def __init__(self, data, debug=False):
        """Load program into this state"""
        self.prog = data.copy()  # Processor byte code
        self._idx = 0             # Current instruction
        self._halt = False       # Processor in halt state
        self._relative_base = 0
        self._dbg = debug

    @property
    def idx(self):
        """Return current program index"""
        return self._idx

    @property
    def base(self):
        """Return relative base"""
        return self._relative_base

    def read(self, offset=0, addr=None):
        """Return value from memory"""
        ptr = addr if addr != None else self._idx + offset
        assert ptr >= 0, f"Invalid read(offset={offset}) from: {ptr}"
        if ptr >= len(self.prog):
            return 0
        return self.prog[ptr]

    def writ(self, value, offset=0):
        """Write value to memory, extend memory if no space"""
        ptr = self.read(offset)
        if ptr >= len(self.prog):
            self.prog.extend([0] * ((ptr + 1) - len(self.prog)))
        if self._dbg:
            print(f"writ({value},offset={offset}) -> self.prog[{ptr}]")
        self.prog[ptr] = value

    def next(self, offset=0):
        """Progress to next instruction"""
        self._idx += offset

    def rbse(self, offset=0):
        """Set relative base"""
        self._relative_base += offset

    def jump(self, ptr):
        """Jump to instruction"""
        self._idx = ptr

    def halt(self):
        """Return true if halted"""
        return self._halt

    def hlcf(self):
        """Halt and catch fire. Set halt() to True"""
        self._halt = True

    def inst(self):
        """Return opcode and modes"""
        code = self.read()
        opcode = code % 100
        modes = [int(code/100)%10, int(code/1000)%10, int(code/10000)%10]
        return opcode, modes

    def parm(self, offset, mode):
        """Read parameter based on mode"""
        value = self.read(offset)
        if mode == 0:       # position mode
            return self.read(addr=value)
        elif mode == 1:     # immediate mode
            return value
        elif mode == 2:     # relative mode
            return self.read(addr=self._relative_base+value)
        assert False, f"Failed with mode: {mode}"


def null_debugger(*args):
    """Null debugger, no output"""
    del args


def cmd_debugger(state, cmd, modes, args, result):
    """Dump processor instructions to stdout"""
    arglist = []
    for i in range(args):
        arglist.append(state.read(i+1))
    res = state.read(args+1) if result else '<undef>'
    print(f"{cmd}({arglist} m:{modes}) -> {res} [idx:{state.idx},base:{state.base}]")


def run(state, io, debug=null_debugger):
    """Run IntCode processor"""

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
        if io.has_in():
            state.writ(io.read_in(), offset=1)
            state.next(2)
            return True
        return False

    def write_output(modes):
        """Output operator: 04, arg -> write arg to output output"""
        debug(state, 'write_output', modes, 1, False)
        io.write_out(state.parm(1, modes[0]))
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

    def set_relative_base(modes):
        """Set relative base operator: 09, arg -> change relative base"""
        debug(state, 'relative_base', modes, 1, False)
        state.rbse(state.parm(1, modes[0]))
        state.next(2)
        return True

    def halt(modes):
        """Halt operator: 99"""
        debug(state, 'halt', modes, 0, False)
        state.hlcf()
        return False

    # Supported operators
    operators = {
        1: add,
        2: multiply,
        3: read_input,
        4: write_output,
        5: jmp_if_true,
        6: jmp_if_false,
        7: less_than,
        8: equals,
        9: set_relative_base,
        99: halt
    }

    assert not state.halt()
    try:
        while True:
            code, modes = state.inst()
            opcode = operators.get(code)
            assert opcode, f"operation failed at {state.idx} -> {state.read()}"
            if not opcode(modes):
                return state.halt()

    except IndexError:
        assert False, f"Invalid index: {state.idx}"
