#!/usr/bin/env python3

import sys


def read_data(file):
    data = []
    with open(file) as f:
        for line in f:
            data.append(line.strip().split(','))
    return data


directions = {
    'U': 0+1j,
    'D': 0-1j,
    'R': 1+0j,
    'L': -1+0j
}


def plot_path(wire):
    """Plot path into dict, where key is position and value is travel length"""
    prev = 0+0j
    dist = 0
    path = { prev: dist }
    for point in wire:
        dir = directions[point[0]]
        steps = int(point[1:])
        for _ in range(steps):
            pos = prev + dir
            dist += 1
            path[pos] = dist
            prev = pos
    return path


def resolve_closest_distance(data):
    """Get the closest point related to (0,0)"""
    wire1 = plot_path(data[0])
    wire2 = plot_path(data[1])
    distance = None
    position = None
    for pos in wire1:
        if pos in wire2:
            d = int(abs(pos.real)) + int(abs(pos.imag))
            if not distance or d < distance:
                distance = d
                position = pos
    return (distance, position)


def resolve_shortest_distance(data):
    """Get the shortest path the wire travels from point (0,0)"""
    wire1 = plot_path(data[0])
    wire2 = plot_path(data[1])
    intersections = {}
    for pos in wire1:
        if pos in wire2 and pos != 0j:
            intersections[pos] = wire1[pos] + wire2[pos]
    distance = None
    position = None
    for k, v in intersections.items():
        if not distance or v < distance:
            distance = v
            position = k
    return (distance, position)


assert len(sys.argv) == 2, "Missing input"
data = read_data(sys.argv[1])
(distance, position) = resolve_closest_distance(data)
print(f"Closest intersect: {distance} ({position.real},{position.imag})")
(distance, position) = resolve_shortest_distance(data)
print(f"Shortest intersect: {distance} ({position.real},{position.imag})")
