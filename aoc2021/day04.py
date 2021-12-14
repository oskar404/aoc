#!/usr/bin/env python3

import sys
import numpy as np


def bingo(board, mask, idx):
    """Return True and row or col if bingo"""
    # check row
    if mask[idx[0], :].sum() == 0:
        return True, board[idx[0], :]
    # check column
    if mask[:, idx[1]].sum() == 0:
        return True, board[:, idx[1]]
    return False, None


def check_sum(draw, board, mask):
    """Return check sum use by AOC to validate algorithm"""
    masked = board * mask
    return masked.sum() * draw


def solve_part1(input, boards):
    """Bingo"""
    masks = np.ones(boards.shape)
    for draw in input:
        for i, board in enumerate(boards):
            idx = np.where(board == draw)
            if len(idx[0]):
                masks[i, idx[0], idx[1]] = 0
                # bingo for row
                winner, codes = bingo(board, masks[i], idx)
                if winner:
                    return draw, codes, board, check_sum(draw, board, masks[i])

    return None, None, None, None


def solve_part2(input, boards):
    """Try to loose i.e. choose board which wins last"""
    masks = np.ones(boards.shape)
    chart = np.ones(boards.shape[0])
    for draw in input:
        for i, board in enumerate(boards):
            if chart[i] == 0:
                continue
            idx = np.where(board == draw)
            if len(idx[0]):
                masks[i, idx[0], idx[1]] = 0
                # bingo for row
                winner, codes = bingo(board, masks[i], idx)
                if winner:
                    if chart.sum() == 1:
                        return draw, codes, board, check_sum(draw, board, masks[i])
                    else:
                        chart[i] = 0

    return None, None, None, None


def read_data(file):
    with open(file) as f:
        lines = [line.strip() for line in f]
    draw = [int(d) for d in lines[0].split(sep=",")]
    boards = []
    buffer = []
    for line in lines[2:]:
        if line:
            buffer.append([int(b) for b in line.split()])
        else:
            boards.append(np.array(buffer))
            buffer = []
    return draw, np.array(boards)


def main():
    assert len(sys.argv) == 2, "Missing input"
    input, boards = read_data(sys.argv[1])
    draw, codes, board, checksum = solve_part1(input, boards)
    print(f"Part 1: \nboard: \n{board}")
    print(f"row: {codes}")
    print(f"draw: {draw}")
    print(f"check: {checksum}")
    draw, codes, board, checksum = solve_part2(input, boards)
    print(f"Part 2: \nboard: \n{board}")
    print(f"row: {codes}")
    print(f"draw: {draw}")
    print(f"check: {checksum}")


if __name__ == "__main__":
    main()
