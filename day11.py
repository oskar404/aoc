#!/usr/bin/env python3

import sys


class PowerGrid(object):

    def _cell(x, y, sn):
        rid = x + 10
        raw = (rid * y + sn) * rid
        return int(raw / 100) % 10 - 5

    def __init__(self, sn):
        self.sn = sn
        self.grid = []
        for x in range(300):
            self.grid.append([PowerGrid._cell(x+1,y+1,sn) for y in range(300)])

    def cells(self, x, y, size=3):
        xi = x - 1
        yi = y - 1
        selection = []
        for i in range(size):
            col = self.grid[xi+i][yi:yi+size]
            selection.append(col)
        return selection

    def shift(self, x, y, size, selection):
        if not selection:
            return self.cells(x, y, size)
        xi = x - 1
        yi = y - 1
        selection.pop(0)
        col = self.grid[xi+(size-1)][yi:yi+size]
        selection.append(col)
        return selection


def power(cells):
    return sum([sum(col) for col in cells])


def dump(cells, size=3):
    for y in range(size):
        print('|'.join(['{:>2}'.format(str(x[y])) for x in cells]))


def solve_part1(input):
    grid = PowerGrid(input)
    candidate = (0, 0, 0, [])
    for x in range(1, 300-2):
        for y in range(1, 300-2):
            cells = grid.cells(x, y)
            p = power(cells)
            if candidate[2] < p:
                candidate = (x, y, p, cells)
    dump(candidate[3])
    return candidate


def solve_part2(input):
    grid = PowerGrid(input)
    candidate = (0, 0, 0, [], 0)
    for size in reversed(range(3, 301)):
        limit = size * size * 4
        if candidate[2] >= limit:
            break
        for y in range(1, 301-(size-1)):
            cells = None
            for x in range(1, 301-(size-1)):
                cells = grid.shift(x, y, size, cells)
                p = power(cells)
                if candidate[2] < p:
                    candidate = (x, y, p, cells, size)
    if candidate[4] <= 32:
        dump(candidate[3])
    return candidate


def test_power_grid():
    assert PowerGrid._cell(3,5,8) == 4
    assert PowerGrid._cell(122,79,57) == -5
    assert PowerGrid._cell(217,196,39) == 0
    assert PowerGrid._cell(101,153,71) == 4

    g = PowerGrid(18)
    assert power(g.cells(33, 45)) == 29
    assert power(g.cells(90, 269, 16)) == 113
    g = PowerGrid(42)
    assert power(g.cells(21, 61)) == 30
    assert power(g.cells(232, 251, 12)) == 119


test_power_grid()
print('Part1: power {2} ({0},{1})'.format(*solve_part1(6392)))
print('Part2: power {2} ({0},{1},{4})'.format(*solve_part2(6392)))
