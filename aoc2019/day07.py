#!/usr/bin/env python3

import itertools
import intcode
import sys
from intcode import IntCodeIO, IntCodeState


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(",")]


def amplify(data, phases):
    register = 0
    for phase in phases:
        io = IntCodeIO([phase, register])
        state = IntCodeState(data)
        intcode.run(state, io)
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
        amps.append((IntCodeState(data), IntCodeIO([phase])))
    while True:
        halt = False
        for state, io in amps:
            io.add_in(input)
            halt = intcode.run(state, io)
            input = io.next_out()
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
    thrust, phase = max_thrust(
        [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
    )
    assert thrust == 43210 and phase == (4, 3, 2, 1, 0), f"{thrust}, {phase}"
    thrust, phase = max_thrust(
        [
            3,
            23,
            3,
            24,
            1002,
            24,
            10,
            24,
            1002,
            23,
            -1,
            23,
            101,
            5,
            23,
            23,
            1,
            24,
            23,
            23,
            4,
            23,
            99,
            0,
            0,
        ]
    )
    assert thrust == 54321 and phase == (0, 1, 2, 3, 4), f"{thrust}, {phase}"
    thrust, phase = max_thrust(
        [
            3,
            31,
            3,
            32,
            1002,
            32,
            10,
            32,
            1001,
            31,
            -2,
            31,
            1007,
            31,
            0,
            33,
            1002,
            33,
            7,
            33,
            1,
            33,
            31,
            31,
            1,
            32,
            31,
            31,
            4,
            31,
            99,
            0,
            0,
            0,
        ]
    )
    assert thrust == 65210 and phase == (1, 0, 4, 3, 2), f"{thrust}, {phase}"
    # part2 tests
    thrust, phase = more_thrust(
        [
            3,
            26,
            1001,
            26,
            -4,
            26,
            3,
            27,
            1002,
            27,
            2,
            27,
            1,
            27,
            26,
            27,
            4,
            27,
            1001,
            28,
            -1,
            28,
            1005,
            28,
            6,
            99,
            0,
            0,
            5,
        ]
    )
    assert thrust == 139629729 and phase == (9, 8, 7, 6, 5), f"{thrust}, {phase}"
    thrust, phase = more_thrust(
        [
            3,
            52,
            1001,
            52,
            -5,
            52,
            3,
            53,
            1,
            52,
            56,
            54,
            1007,
            54,
            5,
            55,
            1005,
            55,
            26,
            1001,
            54,
            -5,
            54,
            1105,
            1,
            12,
            1,
            53,
            54,
            53,
            1008,
            54,
            0,
            55,
            1001,
            55,
            1,
            55,
            2,
            53,
            55,
            53,
            4,
            53,
            1001,
            56,
            -1,
            56,
            1005,
            56,
            6,
            99,
            0,
            0,
            0,
            0,
            10,
        ]
    )
    assert thrust == 18216 and phase == (9, 7, 8, 5, 6), f"{thrust}, {phase}"


assert len(sys.argv) == 2, "Missing input"

if sys.argv[1] == "-t" or sys.argv[1] == "--test":
    self_test()
else:
    data = read_data(sys.argv[1])
    thrust, phase = max_thrust(data)
    print(f"Max thrust: {thrust} {phase}")
    thrust, phase = more_thrust(data)
    print(f"More thrust: {thrust} {phase}")
