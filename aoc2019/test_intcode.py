import pytest
import intcode
from intcode import run, IntCodeIO, IntCodeState


def run_prog(data, result, halted=True):
    state = IntCodeState(data)
    halt_state = run(state, IntCodeIO())
    assert state.prog == result
    assert halt_state == halted


def run_intcode(data, io_if, result, halted=True):
    state = IntCodeState(data)
    halt_state = run(state, io_if)
    assert len(io_if.stdout) == 1 and io_if.stdout[0] == result
    assert halt_state == halted


def test_add_operator():
    run_prog([1, 0, 0, 0, 99], [2, 0, 0, 0, 99])
    run_prog([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])


def test_multiplication_operator():
    run_prog([2, 3, 0, 3, 99], [2, 3, 0, 6, 99])
    run_prog([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801])


def test_basic_io():
    run_intcode([3, 0, 4, 0, 99], IntCodeIO([1]), 1)


def test_equals_operator():
    run_intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], IntCodeIO([8]), 1)
    run_intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], IntCodeIO([88]), 0)
    run_intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], IntCodeIO([8]), 1)
    run_intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], IntCodeIO([0]), 0)


def test_less_than_operator():
    run_intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], IntCodeIO([1]), 1)
    run_intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], IntCodeIO([8]), 0)


def test_jump_operators():
    prog1 = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    run_intcode(prog1, IntCodeIO([0]), 0)
    prog2 = [
        3,
        21,
        1008,
        21,
        8,
        20,
        1005,
        20,
        22,
        107,
        8,
        21,
        20,
        1006,
        20,
        31,
        1106,
        0,
        36,
        98,
        0,
        0,
        1002,
        21,
        125,
        20,
        4,
        20,
        1105,
        1,
        46,
        104,
        999,
        1105,
        1,
        46,
        1101,
        1000,
        1,
        20,
        4,
        20,
        1105,
        1,
        46,
        98,
        99,
    ]
    run_intcode(prog2, IntCodeIO([7]), 999)
    run_intcode(prog2, IntCodeIO([8]), 1000)
    run_intcode(prog2, IntCodeIO([9]), 1001)


def test_data_mutation():
    state = IntCodeState([1002, 4, 3, 4, 33])
    halted = run(state, IntCodeIO())
    assert halted == True
    assert state.prog == [1002, 4, 3, 4, 99]


def test_memory_handling():
    prog = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    io = IntCodeIO()
    state = IntCodeState(prog)
    halted = run(state, io)
    assert halted
    assert io.stdout == prog


def test_large_number():
    io = IntCodeIO()
    state = IntCodeState([1102, 34915192, 34915192, 7, 4, 7, 99, 0])
    halted = run(state, io)
    assert halted
    assert len(io.stdout) == 1 and len(str(io.stdout[0])) == 16


def test_large_number2():
    io = IntCodeIO()
    state = IntCodeState([104, 1125899906842624, 99])
    halted = run(state, io)
    assert halted
    assert len(io.stdout) == 1 and io.stdout[0] == 1125899906842624
