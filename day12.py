#!/usr/bin/env python3

import sys


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

    def __repr__(self):
        return str(self)

    def __str__(self):
        p = self._pos
        v = self._vel
        return f"{self.id:<8} pos=<x={p[0]}, y={p[1]}, z={p[2]}>, vel=<x={v[0]}, y={v[1]}, z={v[2]}>"


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


def dump(number, moons):
    print(f"step: {number}")
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


def total_energy(moons):
    energy = 0
    for m in moons:
        energy += m.potential_energy * m.kinetic_energy
    return energy


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    simulate(data)
    dump(1000, data)
    print(f"Total energy after 1000 steps: {total_energy(data)}")


if __name__ == "__main__":
    main()
