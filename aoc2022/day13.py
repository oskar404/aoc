#!/usr/bin/env python3

import functools
import utils


# You climb the hill and again try contacting the Elves. However, you
# instead receive a signal you weren't expecting: a distress signal.


class Node:
    """Representation of parsed token"""

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.leaf = isinstance(value, int)

    def append(self, value):
        assert isinstance(value, Node)
        self.value.append(value)

    def __str__(self):
        """For debugging purposes"""
        if self.leaf:
            return str(self.value)
        return f"[{','.join([str(x) for x in self.value])}]"


def parse_data(data):
    """return list of packet pairs [{"left": str, "right": str}, ..]"""
    result = []
    pair = {}
    for line in data.strip().splitlines():
        if "left" in pair:
            if "right" in pair:
                result.append(pair)
                pair = {}
            else:
                pair["right"] = line.strip()
        else:
            pair["left"] = line.strip()
    result.append(pair)
    return result


def tokenize(spec):
    """Tokenize spec as list of tokens
    where token is int, or "[" or "]"
    """
    tokens = []

    def finalize_value(value):
        if value is not None:
            tokens.append(value)
            value = None
        return value

    def add_value(value, x):
        if value is None:
            value = int(x)
        else:
            value = value * 10 + int(x)
        assert isinstance(value, int)
        return value

    value = None

    for i, x in enumerate(spec):
        if x in {"[", "]"}:
            value = finalize_value(value)
            tokens.append(x)
        elif x == ",":
            value = finalize_value(value)
        elif x.isdigit():
            value = add_value(value, x)
        else:
            assert False, f"unknown token '{x}' at {i} for '{spec}'"

    return tokens


def parse_packet(spec):
    """Parse a line to as tree of Node objects"""
    tokens = tokenize(spec)

    # handle root node, bootstrap parsing
    assert tokens[0] == "[", f"invalid token '{tokens[0]}' at {0} for '{spec}'"
    current = Node([])
    root = current

    for i in range(1, len(tokens)):
        if tokens[i] == "[":
            node = Node([])
            current.append(node)
            node.parent = current
            current = node
        elif tokens[i] == "]":
            current = current.parent
        elif isinstance(tokens[i], int):
            node = Node(tokens[i])
            current.append(node)
            node.parent = current
        else:
            assert False, f"unknown token '{tokens[i]}' for '{spec}'"

    return root


# pylint: disable=too-many-return-statements,consider-using-enumerate
def compare(lhs, rhs):
    """Compare two node trees.

    Return -1 if left is smaller
    Return 0 if equal
    Return 1 if right is smaller
    """

    # both int values
    if lhs.leaf and rhs.leaf:
        if lhs.value < rhs.value:
            return -1
        if lhs.value == rhs.value:
            return 0
        return 1

    # both lists
    if not lhs.leaf and not rhs.leaf:
        for i in range(len(lhs.value)):
            if len(rhs.value) <= i:
                return 1
            result = compare(lhs.value[i], rhs.value[i])
            if result != 0:
                return result
        if len(lhs.value) < len(rhs.value):
            return -1
        return 0

    # promote rhs
    if not lhs.leaf and rhs.leaf:
        node = Node([])
        node.append(rhs)
        return compare(lhs, node)

    # promote lhs
    if lhs.leaf and not rhs.leaf:
        node = Node([])
        node.append(lhs)
        return compare(node, rhs)

    raise RuntimeError("coding error in correct_order()")


def solve_part1(data):
    """Determine which pairs of packets are already in the right order.
    What is the sum of the indices of those pairs?
    """

    result = 0

    packets = parse_data(data)
    for index, packet in enumerate(packets):
        left = parse_packet(packet["left"])
        right = parse_packet(packet["right"])
        if compare(left, right) == -1:
            result = result + index + 1

    return result


def solve_part2(data):
    """Organize all of the packets into the correct order. What is the decoder
    key for the distress signal?
    """

    def wrapper(lhs, rhs):
        """Wrap compare suitable for functools.cmp_to_key()"""
        return compare(parse_packet(lhs), parse_packet(rhs))

    packets = ["[[2]]", "[[6]]"]

    raw_packets = parse_data(data)
    for packet in raw_packets:
        packets.append(packet["left"])
        packets.append(packet["right"])

    packets = sorted(packets, key=functools.cmp_to_key(wrapper))

    idx1 = packets.index("[[2]]") + 1
    idx2 = packets.index("[[6]]") + 1
    return idx1 * idx2


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
