#!/usr/bin/env python3

import intcode
import sys
from intcode import IntCodeState


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(",")]


class RobotIO:
    """Hull Robot IO Interface

    Colors:
        0:  black
        1:  white

    Output with pairs :
        out[0]:     paint to color
        out[1]:     0 -> 90 degrees to left + move
                    1 -> 90 degrees to rigth + move
    """

    dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

    def __init__(self, start=0):
        self.pos = (0, 0)  # Current robot position
        self.dir = 0  # array lower left corner 0,0
        self.paint = True  # Should output paint or move
        self.hull = {self.pos: start}  # visited positions

    def _move(self, turn):
        step = 1 if turn == 1 else -1
        self.dir = (self.dir + step) % 4
        adder = RobotIO.dirs[self.dir]
        self.pos = (self.pos[0] + adder[0], self.pos[1] + adder[1])

    def read_in(self):
        """Read color"""
        return self.hull[self.pos] if self.pos in self.hull else 0

    def has_in(self):
        """Return true always"""
        return True

    def add_in(self, value):
        """Unsupported for Robot IO"""
        assert False

    def write_out(self, value):
        """Paint or move"""
        assert value == 1 or value == 0
        if self.paint:
            self.hull[self.pos] = value
        else:
            self._move(value)
        self.paint = not self.paint

    def next_out(self):
        """Unsupported for Robot IO"""
        assert False

    def __str__(self):
        return f"hull:{self.hull}"

    def __repr__(self):
        return f"hull:{self.hull}"


def run_robot(data, start_color=0):
    """RUn the robot with IntCode computer"""
    io = RobotIO(start=start_color)
    state = IntCodeState(data)
    halted = intcode.run(state, io)
    assert halted, f"Robot not halted"
    return io.hull


def render(data):
    hull = run_robot(data, start_color=1)
    min_pos = (
        min(hull.keys(), key=(lambda k: k[0]))[0],
        min(hull.keys(), key=(lambda k: k[1]))[1],
    )
    x_shift = 0 - min_pos[0]
    y_shift = 0 - min_pos[1]
    size = (
        max(hull.keys(), key=(lambda k: k[0]))[0] - min_pos[0] + 1,
        max(hull.keys(), key=(lambda k: k[1]))[1] - min_pos[1] + 1,
    )
    canvas = [[" " for _ in range(size[0])] for _ in range(size[1])]
    print(f"min:{min_pos} size:{size} ({x_shift},{y_shift})")
    for p in hull:
        if hull[p] == 1:
            canvas[p[1] + y_shift][p[0] + x_shift] = "0"
    # Somehow the image is upside down .. so reverse iteration
    canvas.reverse()
    for line in canvas:
        print("".join(line))


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    hull = run_robot(data)
    print(f"Visited spots: {len(hull)}")
    render(data)


if __name__ == "__main__":
    main()
