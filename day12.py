#!/usr/bin/env python3

import sys


class Moon:

    def __init__(self, position):
        self._pos = position
        self._vel = (0, 0, 0)

    @property
    def position(self):
        return self._pos

    def __repr__(self):
        return str(self)

    def __str__(self):
        p = self._pos
        v = self._vel
        return f"pos=<x={p[0]}, y={p[1]}, z={p[2]}>, \tvel=<x={v[0]}, y={v[1]}, z={v[2]}>"


def read_data(file):
    """Read input into list of Moon instances"""
    def get_moon(l):
        x, _, l = l.partition('=')[2].partition(',')
        y, _, l = l.partition('=')[2].partition(',')
        z = l.partition('=')[2].partition('>')[0]
        return Moon((int(x), int(y), int(z)))

    data = []
    with open(file) as f:
        for line in f:
            data.append(get_moon(line))
    return data


def dump(number, moons):
    print(f"Iteration: {number}")
    for m in moons:
        print(m)


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    dump(0, data)
    #print(f"Many moons: {data}")


if __name__ == "__main__":
    main()
