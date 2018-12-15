#!/usr/bin/env python3

import sys
from copy import deepcopy
from math import pow, sqrt


class Point(object):
    def __init__(self, data):
        self.X = data[0]
        self.Y = data[1]
        self.vx = data[2]
        self.vy = data[3]

    def move(self, steps=1):
        self.X = self.X + steps * self.vx
        self.Y = self.Y + steps * self.vy
        return self

    def dist(self, p):
        return sqrt(pow(self.X - p.X, 2) + pow(self.Y - p.Y, 2))

    def xdist(self, p):
        return abs(self.X - p.X)

    def ydist(self, p):
        return abs(self.Y - p.Y)

    def __repr__(self):
        return 'P({},{})[{},{}]'.format(self.X, self.Y, self.vx, self.vy)

    def __str__(self):
        return 'P({},{})[{},{}]'.format(self.X, self.Y, self.vx, self.vy)


def get_input():
    def to_list(line):
        replaced = ['position=<', '> velocity=<', '>', ',']
        for r in replaced:
            line = line.replace(r, ' ')
        return [int(x) for x in line.split()]

    assert len(sys.argv) == 2, "Missing input"
    input = []
    with open(sys.argv[1]) as f:
        for line in f:
            input.append(Point(to_list(line)))
    return input


def dump(data, tag, pic=True):
    min_x = min([p.X for p in data])
    min_y = min([p.Y for p in data])
    max_x = max([p.X for p in data]) + 1
    max_y = max([p.Y for p in data]) + 1
    sizex = max_x - min_x
    sizey = max_y - min_y
    print('round: {} [{}x{}]'.format(tag, sizex, sizey))
    if not pic:
        return
    canvas = [' '] * sizex * sizey
    for p in data:
        xp = p.X - min_x
        yp = p.Y - min_y
        canvas[xp + sizex*yp] = '*'
    for y in range(sizey):
        print(''.join(canvas[y*sizex:(y+1)*sizex]))


def solve_part1(input):
    def distance(data):
        return sum([p.xdist(q) for p in data for q in data])
    def move(data, steps=1):
        return [p.move(steps) for p in data]

    data = deepcopy(input)
    # Find minimum distance of stars during one night (60*60*12)
    # This is too simple brute force algorithm. It works but takes a long time
    # Better way would be to calculate intersections of the lines before trying
    # to find the minimum
    night = 60 * 60 * 12 # Seconds in night?
    candidate = (0, distance(data))
    for n in range(1, night):
        data = move(data)
        current = (n, distance(data))
        if current[1] < candidate[1]:
            candidate = current
    data = move(deepcopy(input), candidate[0])
    dump(data, 'n:{} d:{}'.format(candidate[0], candidate[1]))
    return candidate


input = get_input()
print('Part1: (n:{})'.format(solve_part1(input)))

