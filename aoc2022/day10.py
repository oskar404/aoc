#!/usr/bin/env python3

import utils

# You avoid the ropes, plunge into the river, and swim to shore.
#
# The Elves yell something about meeting back up with them upriver, but the
# river is too loud to tell exactly what they're saying. They finish crossing
# the bridge and disappear from view.
#
# Situations like this must be why the Elves prioritized getting the
# communication system on your handheld device working. You pull it out of your
# pack, but the amount of water slowly draining from a big crack in its screen
# tells you it probably won't be of much immediate use.


class Processor:
    """Process input commands"""

    def __init__(self, checks):
        self.instrumentation = checks
        self.register_x = 1
        self.cycle = 0
        self.signal = 0
        self.screen = ["o"] * 240  # init screen

    def clock(self):
        # draw pixel
        pixel = self.cycle % 40
        sprite = self.register_x
        if sprite - 1 <= pixel <= sprite + 1:
            self.screen[self.cycle] = "#"
        else:
            self.screen[self.cycle] = "."
        # tick clock
        self.cycle += 1
        # instrumentation
        if self.cycle in self.instrumentation:
            self.signal += self.cycle * self.register_x

    def noop(self, _):
        self.clock()

    def addx(self, cmd):
        self.clock()
        self.clock()
        self.register_x += int(cmd[1])

    def parse(self, command):
        ops = {
            "noop": self.noop,
            "addx": self.addx,
        }
        cmd = command.split()
        ops[cmd[0]](cmd)


def solve_part1(data):
    """Render the image given by your program. What eight capital letters appear
    on your CRT?
    """
    processor = Processor([20, 60, 100, 140, 180, 220])
    for command in data.strip().splitlines():
        processor.parse(command)
    return processor.signal


def solve_part2(data):
    """Render the image given by your program. What eight capital letters appear
    on your CRT?
    """
    processor = Processor([])
    for command in data.strip().splitlines():
        processor.parse(command)
    screen = ""
    for lnfeed in range(40, 241, 40):
        screen = screen + "".join(processor.screen[lnfeed - 40 : lnfeed]) + "\n"
    return screen.strip()


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: \n{result}")


if __name__ == "__main__":
    main()
