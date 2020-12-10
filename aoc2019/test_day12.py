import pytest
import copy
from aoc2019.day12 import Moon, simulate, total_energy, naive_search, cycle_search, dump


def check(a, b):
    for i in range(3):
        assert a[i] == b[i]


def check_moon(moon, pos, vel):
    check(moon.position, pos)
    check(moon.velocity, vel)


def test_data1():
    data = [
        Moon("A", [-1, 0, 2]),
        Moon("B", [2, -10, -7]),
        Moon("C", [4, -8, 8]),
        Moon("D", [3, 5, -1]),
    ]
    postions = [
        (2, 1, -3),
        (1, -8, 0),
        (3, -6, 1),
        (2, 0, 4),
    ]
    velocities = [(-3, -2, 1), (-1, 1, 3), (3, 2, -3), (1, -1, -1)]
    simulate(data, 10, debug=dump)
    for i in range(4):
        check_moon(data[i], postions[i], velocities[i])
    assert total_energy(data) == 179


def test_data2():
    data = [
        Moon("A", [-8, -10, 0]),
        Moon("B", [5, 5, 10]),
        Moon("C", [2, -7, 3]),
        Moon("D", [9, -8, -3]),
    ]
    postions = [
        (8, -12, -9),
        (13, 16, -3),
        (-29, -11, -1),
        (16, -13, 23),
    ]
    velocities = [(-7, 3, 0), (3, -11, -5), (-3, 7, 4), (7, 1, 1)]
    simulate(data, 100)
    for i in range(4):
        check_moon(data[i], postions[i], velocities[i])
    assert total_energy(data) == 1940


def test_naivesearch_for_data1():
    data = [
        Moon("A", [-1, 0, 2]),
        Moon("B", [2, -10, -7]),
        Moon("C", [4, -8, 8]),
        Moon("D", [3, 5, -1]),
    ]
    rounds = naive_search(data, debug=dump)
    assert rounds == 2772


def test_cyclesearch_for_data1():
    data = [
        Moon("A", [-1, 0, 2]),
        Moon("B", [2, -10, -7]),
        Moon("C", [4, -8, 8]),
        Moon("D", [3, 5, -1]),
    ]
    rounds = cycle_search(data, debug=dump)
    assert rounds == 2772


def test_cycle_for_data2():
    data = [
        Moon("A", [-8, -10, 0]),
        Moon("B", [5, 5, 10]),
        Moon("C", [2, -7, 3]),
        Moon("D", [9, -8, -3]),
    ]
    rounds = cycle_search(data, debug=dump)
    assert rounds == 4686774924
