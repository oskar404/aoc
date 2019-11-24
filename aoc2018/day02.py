#!/usr/bin/env python3

import sys


def get_input():
    assert len(sys.argv) == 2, "Missing input"
    input = []
    with open(sys.argv[1]) as f:
        for line in f:
            input.append(line.strip())
    return input


def fingerprint(id):
    """Fingerprint based two and three of a kind in string. Return tuple(int, int)"""
    def test(count):
        return 1 if len([c for c in codes.values() if c is count]) > 0 else 0

    codes = {}
    for code in id.strip():
        codes[code] = codes.get(code, 0) + 1
    return (test(2), test(3))


def checksum(fp_list):
    m = [0, 0]
    for x in fp_list:
        m[0] += x[0]
        m[1] += x[1]
    return m[0] * m[1]


def hamming_distance(id1, id2):
    """See: https://en.wikipedia.org/wiki/Hamming_distance"""
    assert len(id1) == len(id2), "Hamming distance fail: unequal length"
    return sum(el1 != el2 for el1, el2 in zip(id1, id2))


def same_chars(id1, id2):
    assert len(id1) == len(id2), "Same chars fail: unequal length"
    result = []
    for i in [el1 for el1, el2 in zip(id1, id2) if el1 == el2]:
        result.append(i)
    return ''.join(result)


def solve_part1(input):
    fp_list = []
    for i in input:
        fp_list.append(fingerprint(i))
    return checksum(fp_list)


def solve_part2(input):
    result = []
    next = 0
    for i in input:
        next += 1
        for j in input[next:]:
            if hamming_distance(i, j) <= 1:
                result.append(same_chars(i, j))
    return result


input = get_input()
print('Checksum: {}'.format(solve_part1(input)))
print('Similar codes: {}'.format(solve_part2(input)))
