#!/usr/bin/env python3

import sys
from copy import deepcopy
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
        self.opcode = op_mapper[op]
        self.argument = int(arg)
        self.exec = False

    def __str__(self):
        executed = ""
        if self.exec:
            executed = " (exec)"
        return f"{self.opcode}: {self.argument}{executed}"

    def __repr__(self):
        return str(self)

    def execute(self):
        self.exec = True
        return op_exec[self.opcode](self.argument)


def run(prog, verbose=False):
    """Run program until succeeds or fails"""
    idx = 0
    acc = 0
    success = False
    while idx < len(prog):
        if verbose:
            print(f"{idx}: {prog[idx]}")
        if prog[idx].exec:
            break
        nxt, inc = prog[idx].execute()
        idx += nxt
        acc += inc
    else:
        success = True
    return (idx, acc, success)


def parse(input):
    """Parse command input as list of opcode and arg pairs"""
    prog = []
    for line in [l.strip() for l in input.splitlines() if l.strip()]:
        op, arg = line.split()
        prog.append(Instruction(op.strip(), arg.strip()))
    return prog


def solve_part1(input):
    prog = parse(input)
    idx, acc, success = run(prog)
    assert not success, f"{idx}: {prog[idx]} ({acc}) -> should fail"
    return (idx, acc)


def solve_part2(input):
    def mutate(mdx, prog):
        p = deepcopy(prog)
        while True:
            mdx += 1
            if p[mdx].opcode == OpCode.NOP:
                p[mdx].opcode = OpCode.JMP
                break
            elif p[mdx].opcode == OpCode.JMP:
                p[mdx].opcode = OpCode.NOP
                break
        else:
            assert False
        return (mdx, p)

    prog = parse(input)
    # Brute force algorithm -> try until fix found
    mdx = -1
    idx = 0
    acc = 0
    success = False
    while not success:
        mdx, mprog = mutate(mdx, prog)
        idx, acc, success = run(mprog)
    return (idx, acc, mdx)


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    idx, acc = solve_part1(data)
    print(f"Part 1: (idx: {idx}, acc: {acc})")
    idx, acc, mdx = solve_part2(data)
    print(f"Part 2: (idx: {idx}, acc: {acc}) (fix: {mdx})")


if __name__ == "__main__":
    main()
