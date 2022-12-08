#!/usr/bin/env python3

import sys


# The expedition comes across a peculiar patch of tall trees all planted
# carefully in a grid. The Elves explain that a previous expedition planted
# these trees as a reforestation effort. Now, they're curious if this would be
# a good location for a tree house.


def parse(data):
    """Parse into matrix"""
    result = []
    for line in data.strip().splitlines():
        result.append([int(hght) for hght in line])
    return result


def transpose(rows, cols, matrix):
    """Memory is cheap - transpose a copy for convinient usage"""
    # maybe numpy would have been better . .the init here is horrible
    transposed = [[]] * cols
    for idx in range(cols):
        transposed[idx] = [0] * rows
    for ridx in range(rows):
        for cidx in range(cols):
            transposed[cidx][ridx] = matrix[ridx][cidx]
    return transposed


def solve_part1(data):
    """Consider your map; how many trees are visible from outside the grid?"""

    matrix = parse(data)
    rows = len(matrix)
    cols = len(matrix[0])
    mirror = transpose(rows, cols, matrix)
    result = 2 * rows + 2 * cols - 4  # edge rows & cols are always visible
    for rdx in range(1, rows - 1):
        for cdx in range(1, cols - 1):
            level = matrix[rdx][cdx]
            maxl = max(matrix[rdx][:cdx])
            maxr = max(matrix[rdx][cdx + 1 :])
            maxu = max(mirror[cdx][:rdx])
            maxd = max(mirror[cdx][rdx + 1 :])
            if level > maxl or level > maxr or level > maxu or level > maxd:
                result += 1
    return result


def solve_part2(data):
    """Consider each tree on your map. What is the highest scenic score possible
    for any tree?
    """

    def get_score(rdx, cdx, level):
        """Calculate score for current tree"""
        # ugly copy-pasta but too tired to figure out more clever way
        lscore = 0
        for idx in range(cdx - 1, -1, -1):
            lscore += 1
            if matrix[rdx][idx] >= level:
                break
        rscore = 0
        for idx in range(cdx + 1, cols):
            rscore += 1
            if matrix[rdx][idx] >= level:
                break
        uscore = 0
        for idx in range(rdx - 1, -1, -1):
            uscore += 1
            if matrix[idx][cdx] >= level:
                break
        dscore = 0
        for idx in range(rdx + 1, rows):
            dscore += 1
            if matrix[idx][cdx] >= level:
                break
        return lscore * rscore * uscore * dscore

    matrix = parse(data)
    rows = len(matrix)
    cols = len(matrix[0])

    score = 0
    for rdx in range(1, rows - 1):
        for cdx in range(1, cols - 1):
            level = matrix[rdx][cdx]
            candidate = get_score(rdx, cdx, level)
            score = max(score, candidate)
    return score


def read_data(file):
    with open(file, mode="r", encoding="utf-8") as infile:
        return infile.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
