#!/usr/bin/env python3

import sys


def get_input():
    assert len(sys.argv) == 2, "Missing input"
    with open(sys.argv[1]) as f:
        return list(map(int, f.read().split()))


def solve_part1(input):
    def parse(data):
        license = 0
        if len(data) > 2:
            # parse header
            nodes = data.pop(0)
            meta = data.pop(0)
            # parse children
            for _ in range(nodes):
                license += parse(data)
            # parse meta data
            for _ in range(meta):
                license += data.pop(0)
        return license

    data = input.copy()
    license = parse(data)
    return license


def dump(tree, indent=""):
    print("{}N({}):{}".format(indent, len(tree["nodes"]), tree["meta"]))
    indent = indent + "  "
    for n in tree["nodes"]:
        dump(n, indent)


def solve_part2(data):
    def parse(data):
        node = None
        if len(data) > 2:
            # parse header
            nodes = data.pop(0)
            meta = data.pop(0)
            node = {"nodes": [], "meta": []}
            # parse children
            for _ in range(nodes):
                node["nodes"].append(parse(data))
            # parse meta data
            for _ in range(meta):
                node["meta"].append(data.pop(0))
        return node

    data = input.copy()
    tree = parse(data)

    def calculate(tree):
        license = 0
        if len(tree["nodes"]) == 0:
            license = sum(tree["meta"])
        else:
            for n in tree["meta"]:
                if n > 0 and n - 1 < len(tree["nodes"]):
                    license += calculate(tree["nodes"][n - 1])
        return license

    license = calculate(tree)
    return license


input = get_input()
print("Part1: license data {}".format(solve_part1(input)))
print("Part2: root value {}".format(solve_part2(input)))
