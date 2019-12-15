import pytest
from intcode import run, IntCodeIO, IntCodeState


def run_intcode(data, io_if, result, halted=True):
    state = IntCodeState(data)
    halt_state = run(state, io_if)
    assert len(io_if.stdout) == 1 and io_if.stdout[0] == result
    assert halt_state == halted


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
        3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,
        0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,
        4,20,1105,1,46,98,99]
    run_intcode(prog2, IntCodeIO([7]), 999)
    run_intcode(prog2, IntCodeIO([8]), 1000)
    run_intcode(prog2, IntCodeIO([9]), 1001)


def test_data_mutation():
    state = IntCodeState([1002, 4, 3, 4, 33])
    halted = run(state, IntCodeIO())
    assert halted == True
    assert state.prog == [1002, 4, 3, 4, 99]
