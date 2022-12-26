#!/usr/bin/env python3

import copy
from dataclasses import dataclass
import utils


# You try contacting the Elves using your handheld device, but the river
# you're following must be too low to get a decent signal.


def parse(data):
    """return list of strings representing the map"""
    return [list(i.strip()) for i in data.strip().splitlines()]


def size(mapdata):
    """return map size as tuple (max_x, max_y)"""
    return (len(mapdata[0]), len(mapdata))


@dataclass
class Node:
    """Node (x,y) coordinates and distance d"""

    x: int
    y: int
    distance: int
    level: int

    def loc(self):
        return (self.x, self.y)

    def __eq__(self, obj):
        return isinstance(obj, Node) and self.loc() == obj.loc()

    def __hash__(self):
        return hash(self.loc())


class PriorityQueue:
    """Priority queue for distances"""

    def __init__(self):
        self.queue = {}  # dict

    def add(self, node):
        """Add node to queue"""
        # might override, new value must be shorted distance
        self.queue[node.loc()] = node

    def pop(self):
        """Return min distance node"""
        current = None
        for node in self.queue.values():
            if current is None:
                current = node
            elif node.distance < current.distance:
                current = node
        self.queue.pop(current.loc())
        return current

    def __len__(self):
        return len(self.queue)


def edges(node, graph, mapsize, visited):
    """get edges for the node"""

    def on_map(x, y):
        return 0 <= x < mapsize[0] and 0 <= y < mapsize[1]

    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    neighbours = []
    for inc in dirs:
        x = node.x + inc[0]
        y = node.y + inc[1]
        if on_map(x, y):
            level = ord(graph[y][x])
            if (level - node.level) <= 1:
                neighbour = Node(x, y, -1, level)
                if neighbour not in visited:
                    neighbours.append(neighbour)
    return neighbours


def dijkstra(graph, start, end):
    """Implement greedy Dijkstra"""

    mapsize = size(graph)

    # Unvisited nodes with some distance
    unvisited = PriorityQueue()
    unvisited.add(start)

    visited = set()

    # Save the cost of visiting node
    # and update it as we traverse the graph
    shortest = {start: 0}

    # Store shortest known path
    previous = {}

    # Algorithm executes until all nodes visited or end poit found
    while len(unvisited) > 0:

        # node with the lowest distance
        current = unvisited.pop()

        # Retrieves neighbors, updates distances and add to unvisited
        neighbors = edges(current, graph, mapsize, visited)
        for neighbor in neighbors:
            distance = shortest[current] + 1
            if neighbor not in shortest or distance < shortest[neighbor]:
                neighbor.distance = distance
                shortest[neighbor] = distance
                # add to unvisited
                unvisited.add(neighbor)
                # update the best path for current node
                previous[neighbor] = current

        # After visiting its neighbors, we mark the node as "visited"
        visited.add(current)

        # break if destination
        if end in visited:
            break

    return previous, shortest


def get_route(previous, end):
    """Return route used to travel to destination"""
    result = set()
    node = end
    while node in previous:
        result.add(node)
        node = previous[node]
    return result


def dump(route, mapdata):
    """Dump route to map and print"""
    mapsize = size(mapdata)
    data = copy.deepcopy(mapdata)
    for node in route:
        data[node.y][node.x] = "."
    print("".join(["="] * mapsize[0]))
    for line in data:
        print("".join(line))
    print("".join(["="] * mapsize[0]))
    return data


def solve_part1(data):
    """What is the fewest steps required to move from your current
    position to the location that should get the best signal?
    """

    # Solution is https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    mapdata = parse(data)

    # find root/starting point
    start = None
    end = None
    for y, line in enumerate(mapdata):
        if "S" in line:
            x = line.index("S")
            start = Node(x, y, 0, ord("a"))
            mapdata[y][x] = "a"
        if "E" in line:
            x = line.index("E")
            end = Node(x, y, -1, ord("z"))
            mapdata[y][x] = "z"
        if start and end:
            break

    if utils.VERBOSE:
        print(f"{start=}")
        print(f"{end=}")

    previous, shortest = dijkstra(mapdata, start, end)

    if utils.VERBOSE:
        route = get_route(previous, end)
        dump(route, mapdata)

    return shortest[end]


def solve_part2(data):
    """Just template"""

    return len(data) != 0


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
