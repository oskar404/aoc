#!/usr/bin/env python3

import sys


def parse(input):
    """Return list of str objects"""
    return [l.strip() for l in input.splitlines() if l.strip()]


def tokenize(eq):
    """Split equation to list of tokens"""

    def push(token):
        if token != "":
            if token[0].isdigit():
                tokens.append(int(token))
            else:
                tokens.append(token)

    tokens = []
    token = ""

    for t in eq:
        if t == " ":
            push(token)
            token = ""
        if t == "+" or t == "*" or t == "(" or t == ")":
            push(token)
            push(t)
            token = ""
        elif t.isdigit():
            token += t

    push(token)
    return tokens


def solve_equation(eq, verbose=False):
    """Parse string and return the result"""
    tokens = tokenize(eq)
    if verbose:
        print(f"eq: {tokens}")

    stack = []

    def do_sum(t):
        stack.pop()
        stack.append(stack.pop() + t)

    def do_multiplication(t):
        stack.pop()
        stack.append(stack.pop() * t)

    def do_parentheses(t):
        v = stack.pop()
        stack.pop()
        stack.append(v)

    int_ops = {
        "(": lambda t: stack.append(t),
        "+": do_sum,
        "*": do_multiplication,
    }

    for t in tokens:
        if isinstance(t, int):
            if len(stack) == 0:
                stack.append(t)
            else:
                int_ops[stack[-1]](t)
        elif t == "+" or t == "*" or t == "(":
            stack.append(t)
        elif t == ")":
            do_parentheses(t)
            if len(stack) > 2:
                v = stack.pop()
                assert isinstance(v, int)
                if stack[-1] in ["+", "*"]:
                    int_ops[stack[-1]](v)
                elif stack[-1] == "(":
                    stack.append(v)
        else:
            assert False, f"fail token: {t}"

        if verbose:
            print(f"stack: {stack}")

    assert len(stack) == 1
    return stack[0]


def solve_part1(input, verbose=False):
    """Return number of active cubes after six rounds"""
    equations = parse(input)

    result = []
    for eq in equations:
        result.append(solve_equation(eq, verbose))

    if verbose:
        print(f"results: {result}")

    return sum(result)


def solve_part2(input, verbose=False):
    return 0


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: sum: {solve_part1(data)}")


if __name__ == "__main__":
    main()
