#!/usr/bin/env python3

import intcode
import sys
from intcode import IntCodeState


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(',')]


class DroidBrain:
    """Repare Droid Control Logic

    Input:
        1: move north
        2: move south
        3: move west
        4: move east
    Output:
        0: Wall - position not changed
        1: Move OK
        2: Move OK and location is oxygen system
    """

    tile = {
        0: '#',
        1: '.',
        2: 'O',
    }

    def __init__(self):
        self._screen = [[]]*50  # Screen array of arrays
        for i in range(len(self._screen)):
            self._screen[i] = [' '] * 50
        self._px = 25
        self._py = 25
        print(len(self._screen))
        self._screen[self._py][self._px] = self.tile[1]
        self._previous = 1  # Current position is empty
        self._input = [1]   # Start with north
        self._running = True

    @property
    def screen(self):
        return self._screen

    def _draw(self, x, y, value):
        """Draw tile to screen and enlarge it if needed"""
        # handle negative indexes
        tile = self.tile[value]
        if y >= len(self._screen):
            self._screen += [[' ']] * ((y+1) - len(self._screen))
        if x >= len(self._screen[y]):
            self._screen[y] += [' '] * ((x+1) - len(self._screen[y]))
        self._screen[y][x] = tile

    def read_in(self):
        """Return next move"""
        # Insert logic here - still just playinng around
        if self._previous == 1:  # continue same direction
            self._input.append(self._input[-1])
        else:
            move = self._input[-1]+1 if self._input[-1]+1 <= 4 else 1
            self._input.append(move)
        print(self._input[-1])
        return self._input[-1]

    def has_in(self):
        """Return True always"""
        return self._running

    def add_in(self, value):
        """Unsupported"""
        del value
        assert False

    def _next(self):
        """Return next position"""
        cmd = self._input[-1]
        x, y = self._px, self._py
        if cmd == 1:
            y += 1
        elif cmd == 2:
            y -= 1
        elif cmd == 3:
            x -= 1
        elif cmd == 4:
            x += 1
        else:
            assert False
        return x, y

    def write_out(self, value):
        """Move droid"""
        self._previous = value
        x, y = self._next()
        self._draw(x, y, value)
        if value == 1 or value == 2:  # Not wall
            self._px, self._py = x, y
        if value == 2:  # Oxygen system found
            self._running = False
            print(f"FOUND")
        if len(self._input) > 200:
            self._running = False

    def next_out(self):
        """Unsupported"""
        assert False

    def __str__(self):
        return f"screen:{self._screen}"

    def __repr__(self):
        return f"screen:{self._screen}"


def render(screen):
    """Print the screen"""
    s = screen[:]
    s.reverse()
    for r in s:
        print(''.join(r))


def find_oxygen_system(data):
    io = DroidBrain()
    state = IntCodeState(data)
    halted = intcode.run(state, io)
    print(f"Robot halted: {halted}")
    render(io.screen)
    return 0


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    moves = find_oxygen_system(data)
    print(f"Shortest path to oxygen system: {moves}")


if __name__ == "__main__":
    main()
