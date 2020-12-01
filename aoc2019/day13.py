#!/usr/bin/env python3

import intcode
import sys
from intcode import IntCodeState


def read_data(file):
    with open(file) as f:
        return [int(i) for i in f.read().split(",")]


class ArcadeIO:
    """Arcade Cabinet IO

    Every three output instructions specify the x position (distance from the
    left), y position (distance from the top), and tile ID.

    Tile ID:
    - 0 is an empty tile. No game object appears in this tile.
    - 1 is a wall tile. Walls are indestructible barriers.
    - 2 is a block tile. Blocks can be broken by the ball.
    - 3 is a horizontal paddle tile. The paddle is indestructible.
    - 4 is a ball tile. The ball moves diagonally and bounces off objects.
    """

    tile = {0: " ", 1: "X", 2: "B", 3: "_", 4: "o"}

    def __init__(self):
        self._screen = [[" "]]  # Screen array of arrays
        self._px = None
        self._py = None
        self._input = []
        self._score = 0
        self._ball = 0
        self._paddle = 0

    @property
    def screen(self):
        return self._screen

    @property
    def score(self):
        return self._score

    def _draw(self, x, y, tile):
        """Draw tile to screen and enlarge it if needed"""
        if y >= len(self._screen):
            self._screen += [[" "]] * ((y + 1) - len(self._screen))
        if x >= len(self._screen[y]):
            self._screen[y] += [" "] * ((x + 1) - len(self._screen[y]))
        self._screen[y][x] = tile

    def read_in(self):
        """Return joy stick movements"""
        if self._ball > self._paddle:
            return 1
        return -1 if self._paddle > self._ball else 0

    def has_in(self):
        """Return True always"""
        return True

    def add_in(self, value):
        """Unsupported in ArcadeIO"""
        assert False

    def write_out(self, value):
        """Add tile to screen when all x, y and tile_id is received"""
        if self._px == None:
            self._px = value
        elif self._py == None:
            self._py = value
        else:
            if self._px >= 0:
                self._draw(self._px, self._py, ArcadeIO.tile[value])
                if value == 4:
                    self._ball = self._px
                elif value == 3:
                    self._paddle = self._px
            else:
                self._score = value
            self._px = None
            self._py = None

    def next_out(self):
        """Unsupported for ArcadeIO"""
        assert False

    def __str__(self):
        return f"screen:{self._screen}"

    def __repr__(self):
        return f"screen:{self._screen}"


def render(screen):
    """Print the screen"""
    for r in screen:
        print("".join(r))


def play_game(data, coins=None):
    io = ArcadeIO()
    state = IntCodeState(data)
    if coins:
        state.prog[0] = coins
    halted = intcode.run(state, io)
    assert halted, f"Game halted"
    render(io.screen)
    blocks = 0
    for x in range(len(io.screen)):
        blocks += sum([1 if p == "B" else 0 for p in io.screen[x]])
    return blocks, io.score


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    blocks, _ = play_game(data)
    print(f"Number of block tiles: {blocks}")
    _, score = play_game(data, 2)
    print(f"High score: {score}")


if __name__ == "__main__":
    main()
