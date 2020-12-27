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


def do_push(stack, token):
    stack.append(token)


def do_addition(stack, value):
    stack.pop()
    stack.append(stack.pop() + value)


def do_multiplication(stack, value):
    stack.pop()
    stack.append(stack.pop() * value)


def do_parenthesis(stack, token):
    value = stack.pop()
    while True:
        op = stack.pop()
        if op == "(":
            break
        lhs = stack.pop()
        if op == "+":
            value = lhs + value
        elif op == "*":
            value = lhs * value
    stack.append(value)


def solve_equation_same_precedence(eq, verbose=False):
    """Parse string and return the result"""
    tokens = tokenize(eq)
    if verbose:
        print(f"eq: {tokens}")

    stack = []
    ops = {
        None: do_push,
        "(": do_push,
        ")": do_parenthesis,
        "+": do_addition,
        "*": do_multiplication,
    }

    for t in tokens:
        if isinstance(t, int):
            op = stack[-1] if len(stack) else None
            ops[op](stack, t)
        elif t == "+" or t == "*" or t == "(":
            stack.append(t)
        elif t == ")":
            ops[")"](stack, t)
            # solve pre parenthesis operators
            if len(stack) > 2:
                v = stack.pop()
                assert isinstance(v, int)
                ops[stack[-1]](stack, v)
        else:
            assert False, f"fail token: {t}"

        if verbose:
            print(f"stack: {stack}")

    assert len(stack) == 1
    return stack[0]


def solve_equation_addition_precendence(eq, verbose=False):
    """Parse string and return the result"""
    tokens = tokenize(eq)
    if verbose:
        print(f"eq: {tokens}")

    stack = []
    ops = {
        None: do_push,
        "(": do_push,
        ")": do_parenthesis,
        "+": do_addition,
        "*": do_push,
    }

    for t in tokens:
        if isinstance(t, int):
            op = stack[-1] if len(stack) else None
            ops[op](stack, t)
        elif t == "+" or t == "*" or t == "(":
            stack.append(t)
        elif t == ")":
            ops[")"](stack, t)
            # solve preparenthesis addition
            if len(stack) > 2:
                v = stack.pop()
                assert isinstance(v, int)
                ops[stack[-1]](stack, v)
        else:
            assert False, f"fail token: {t}"

        if verbose:
            print(f"stack: {stack}")

    # solve multiplications
    while len(stack) > 1:
        rhs = stack.pop()
        assert isinstance(rhs, int)
        op = stack.pop()
        if op == "*":
            lhs = stack.pop()
            assert isinstance(lhs, int)
            stack.append(lhs * rhs)
        else:
            assert False, f"invalid operator (not *): {op}"

    assert len(stack) == 1
    return stack[0]


def solve_part1(input, verbose=False):
    """Return sum of the equations (resolved with order)"""
    equations = parse(input)

    result = []
    for eq in equations:
        result.append(solve_equation_same_precedence(eq, verbose))

    if verbose:
        print(f"results: {result}")

    return sum(result)


def solve_part2(input, verbose=False):
    """Return sum of the equations (resolved with + precedence)"""
    equations = parse(input)

    result = []
    for eq in equations:
        result.append(solve_equation_addition_precendence(eq, verbose))

    if verbose:
        print(f"results: {result}")

    return sum(result)


def read_data(file):
    with open(file) as f:
        return f.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    print(f"Part 1: sum: {solve_part1(data)}")
    print(f"Part 2: sum: {solve_part2(data)}")


if __name__ == "__main__":
    main()
