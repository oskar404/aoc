import pytest
from day12 import Moon, simulate, total_energy, dump


def check(a, b):
    for i in range(3):
        assert a[i] == b[i]


def check_moon(moon, pos, vel):
    check(moon.position, pos)
    check(moon.velocity, vel)


def test_data1():
    data = [
        Moon('A', [-1, 0, 2]),
        Moon('B', [2, -10, -7]),
        Moon('C', [4, -8, 8]),
        Moon('D', [3, 5, -1])
    ]
    postions = [
        (2, 1, -3),
        (1, -8, 0),
        (3, -6, 1),
        (2, 0, 4),
    ]
    velocities = [
        (-3, -2, 1),
        (-1, 1, 3),
        (3, 2, -3),
        (1, -1, -1)
    ]
    simulate(data, 10, debug = dump)
    for i in range(4):
        check_moon(data[i], postions[i], velocities[i])
    assert total_energy(data) == 179
