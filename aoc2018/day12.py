#!/usr/bin/env python3

import sys


class PotState(object):

    def __init__(self, data):
        self.data = data

    # iterator

def get_input():
    assert len(sys.argv) == 2, "Missing input"
    state = []
    rules = set()
    with open(sys.argv[1]) as f:
        for line in f:            
            items = line.split()
            if items and items[0] == 'initial':
                state.append(items[2])
            elif items and items[2] == '#':
                rules.add(items[0])
    return state, rules


def solve_part1(state, rules):
    data = state.copy()
    # extend data, initial data starts from 0
    # for 20 rounds maybe +- 20 additional 
    return 'duh'


def solve_part2(state, rules):
    return 'duh'



state, rules = get_input()
print(state)
print(sorted(rules))
print('Part1: {}'.format(*solve_part1(state, rules)))
#print('Part2: winner {} score {}'.format(*solve_part2(i['players'],i['rounds'])))
