import pytest  # noqa: F401  # pylint: disable=unused-import
import utils
from day12 import Node, PriorityQueue
from day12 import parse, size, edges
from day12 import solve_part1, solve_part2


MAP = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def test_queue():
    node1 = Node(1, 2, 3, 0)
    node2 = Node(1, 2, 4, 0)
    node3 = Node(2, 3, 0, 0)
    assert node1 == node2  # __equeue__ operator test
    queue = PriorityQueue()
    assert len(queue) == 0
    queue.add(node1)
    assert len(queue) == 1
    queue.add(node2)
    assert len(queue) == 1  # node2 has same id() as node1
    queue.add(node3)
    assert len(queue) == 2
    popped = queue.pop()
    assert node3 == popped  # node3 has shortest distance
    assert len(queue) == 1


def test_edges_method():
    node1 = Node(0, 0, 0, ord("a"))
    mapdata = parse(MAP)
    mapsize = size(mapdata)
    neighbours = edges(node1, mapdata, mapsize, set())
    assert len(neighbours) == 2
    for node in neighbours:
        assert node.level == ord("a")
    node2 = Node(5, 2, 0, ord("z"))
    neighbours = edges(node2, mapdata, mapsize, set())
    assert len(neighbours) == 4


def test_solution1():
    with utils.verbose():
        assert solve_part1(MAP) == 31


def test_solution2():
    with utils.verbose():
        assert solve_part2(MAP) == 29
