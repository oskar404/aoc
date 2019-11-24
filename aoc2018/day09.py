#!/usr/bin/env python3

import sys
import timeit
# Better/faster solution would have been a linked list/tied to a circle
from blist import blist


def get_input():
    assert len(sys.argv) == 2, "Missing input"
    input = []
    with open(sys.argv[1]) as f:
        for line in f:
            items = line.split()
            input.append({'players': int(items[0]), 'rounds': int(items[6])})
    return input


def dump_game(game, current, player):
    def to_str(val):
        return ' {}'.format(val)
    gstr = [to_str(g) for g in game]
    gstr[current] = ' <{}>'.format(game[current])
    print('{}: {}'.format(player + 1, ''.join(gstr)))


def solve_part1(players, rounds):
    game = [0] # starting point
    stats = [0] * players
    current = 1
    player = 1
    for n in range(1,rounds+1):
        if n % 23 == 0:
            stats[player-1] += n
            current = current - 7 if current - 7 >= 0 else len(game) - (7 - current)
            stats[player-1] += game[current]
            del game[current]
        else:
            current = current + 2 if current + 2 <= len(game) else 1
            game.insert(current, n)
        #dump_game(game, current, player)
        player = player + 1 if player < players else 1

    winner = stats.index(max(stats)) + 1
    score = max(stats)
    return winner, score


def solve_part2(players, rounds):
    # Same algorithm, use faster list, insertion is bottleneck in default list
    game = blist([0]) # starting point
    stats = [0] * players
    current = 1
    player = 1
    for n in range(1, 100*rounds+1):
        if n % 23 == 0:
            stats[player-1] += n
            current = current - 7 if current - 7 >= 0 else len(game) - (7 - current)
            stats[player-1] += game[current]
            del game[current]
        else:
            current = current + 2 if current + 2 <= len(game) else 1
            game.insert(current, n)
        player = player + 1 if player < players else 1

    winner = stats.index(max(stats)) + 1
    score = max(stats)
    return winner, score



input = get_input()
for i in input:
    start = timeit.default_timer()
    print('Part1: winner {} score {}'.format(*solve_part1(i['players'],i['rounds'])))
    stop = timeit.default_timer()
    print('Time:', round(stop - start, 3))
    start = timeit.default_timer()
    print('Part2: winner {} score {}'.format(*solve_part2(i['players'],i['rounds'])))
    stop = timeit.default_timer()
    print('Time:', round(stop - start, 3))
