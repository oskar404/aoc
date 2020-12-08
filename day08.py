#!/usr/bin/env python3

import sys
from enum import Enum


class OpCode(Enum):
    """Operation codes"""

    NOP = 1
    ACC = 2
    JMP = 3


op_mapper = {
    "nop": OpCode.NOP,
    "acc": OpCode.ACC,
    "jmp": OpCode.JMP,
}


op_exec = {
    OpCode.NOP: lambda arg: (1, 0),
    OpCode.ACC: lambda arg: (1, arg),
    OpCode.JMP: lambda arg: (arg, 0),
}


class Instruction:
    """Instruction -> operation, int arg"""

    def __init__(self, op, arg):
        self.operation = op_mapper[op]
        self.argument = int(arg)
        self.exec = False

    def __str__(self):
        executed = ""
        if self.exec:
            executed = " (exec)"
        return f"{self.operation}: {self.argument}{executed}"

    def __repr__(self):
        return str(self)

    def execute(self):
        self.exec = True
        return op_exec[self.operation](self.argument)


def run(prog):
    """Run program until some operation is run second time"""
    idx = 0
    acc = 0
    while not prog[idx].exec:
        print(f"{idx}: {prog[idx]}")
        nxt, inc = prog[idx].execute()
        idx += nxt
        acc += inc
        assert idx < len(prog)
    return (idx, acc)


def parse(input):
    """Some nifty regex magic rule would have been cool .."""
    prog = []
    for line in [l.strip() for l in input.splitlines() if l.strip()]:
        print(f"parse -> {line}")
        op, arg = line.split()
        prog.append(Instruction(op.strip(), arg.strip()))
    return prog


def solve_part1(input):
    prog = parse(input)
    return run(prog)


def solve_part2(input):
    pass


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    idx, acc = solve_part1(data)
    print(f"Part 1: (idx: {idx}, acc: {acc})")


if __name__ == "__main__":
    main()
