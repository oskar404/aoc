#!/usr/bin/env python3

import copy
import math
import sys
from functools import reduce


def _gravity(lhs, rhs):
    if rhs > lhs:
        return 1
    return -1 if lhs > rhs else 0


class Moon:

    def __init__(self, name, position):
        self._pos = position  # Expect position to be list
        self._name = name
        self._vel = [0, 0, 0]

    @property
    def id(self):
        return self._name

    @property
    def position(self):
        return self._pos

    @property
    def velocity(self):
        return self._vel

    @property
    def potential_energy(self):
        return sum([abs(d) for d in self._pos])

    @property
    def kinetic_energy(self):
        return sum([abs(d) for d in self._vel])

    def apply_gravity(self, moon):
        for i in range(3):
            self._vel[i] += _gravity(self._pos[i], moon._pos[i])

    def apply_velocity(self):
        for i in range(3):
            self._pos[i] += self._vel[i]

    def to_str(self):
        p = self._pos
        v = self._vel
        return f"{self.id:<8} pos=<x={p[0]}, y={p[1]}, z={p[2]}>, vel=<x={v[0]}, y={v[1]}, z={v[2]}>"

    def clone(self, memo = None):
        m = Moon(self.id, copy.deepcopy(self.position))
        m._vel = copy.deepcopy(self.velocity)
        return m

    __copy__ = clone
    __deepcopy__ = clone
    __repr__ = to_str
    __str__ = to_str

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.id == other.id and
                self.position == other.position and
                self.velocity == other.velocity)
        else:
            return False


def read_data(file):
    """Read input into list of Moon instances"""
    def get_moon(l):
        x, _, l = l.partition('=')[2].partition(',')
        y, _, l = l.partition('=')[2].partition(',')
        z = l.partition('=')[2].partition('>')[0]
        return Moon(names.pop(), [int(x), int(y), int(z)])

    data = []
    names = ['Io', 'Europa', 'Ganymede', 'Callisto']
    with open(file) as f:
        for line in f:
            data.append(get_moon(line))
    return data


def dump(step, moons):
    print(f"step: {step}")
    for m in moons:
        print(m)


def no_dump(number, moons):
    del number, moons


def simulate(moons, rounds = 1000, debug = no_dump):
    debug(0, moons)
    for i in range(1, rounds+1):
        for m in moons:
            for n in moons:
                if n.id != m.id:
                    m.apply_gravity(n)
        for m in moons:
            m.apply_velocity()
        debug(i, moons)
    return moons


def total_energy(moons):
    energy = 0
    for m in moons:
        energy += m.potential_energy * m.kinetic_energy
    return energy


def naive_search(moons, debug = no_dump):
    """Search cycle just by iterating until found"""
    debug(0, moons)
    step = 0
    initial = copy.deepcopy(moons)
    while True:
        step += 1
        for m in moons:
            for n in moons:
                if n.id != m.id:
                    m.apply_gravity(n)
        for m in moons:
            m.apply_velocity()
        if initial == moons:
            debug(step, moons)
            return step


def cycle_search(moons, debug = no_dump):
    """Search cycle for each axis separately"""
    # This solution was inspired by the reddit thread
    # https://www.reddit.com/r/adventofcode/comments/e9j0ve/2019_day_12_solutions/
    def _axis(p):
        p0 = p[:]
        v = [0] * len(p)
        v0 = v[:]
        step = 0
        while True:
            step += 1
            for i in range(len(v)):
                v_change = sum([_gravity(p[i], p[j]) for j in range(len(p))])
                v[i] += v_change
            p = [p[i] + v[i] for i in range(len(p))]
            if p0 == p and v0 == v:
                break
        return step

    def _lcm(p1, p2):
        return p1 * p2 // math.gcd(p1, p2)

    debug(0, moons)
    rx = _axis([m.position[0] for m in moons])
    ry = _axis([m.position[1] for m in moons])
    rz = _axis([m.position[2] for m in moons])
    return reduce(_lcm, [rx, ry, rz])


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    simulated_data = simulate(copy.deepcopy(data))
    print(f"Total energy after 1000 steps: {total_energy(simulated_data)}")
    print(f"Number of steps to repeat: {cycle_search(data)}")


if __name__ == "__main__":
    main()
