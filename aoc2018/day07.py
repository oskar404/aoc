#!/usr/bin/env python3

import sys
from collections import defaultdict


def get_input():
    assert len(sys.argv) == 2, "Missing input"
    data = []
    with open(sys.argv[1]) as f:
        for line in f:
            l = line.split()
            data.append((l[1], l[7]))
    return data


def print_graph(graph):
    print("graph")
    for n in sorted(graph.keys()):
        print("{}->{}".format(n, "".join(sorted(graph[n]))))


def solve_part1(input):
    graph = defaultdict(set)
    invrs = defaultdict(set)

    for edge in input:
        graph[edge[0]].add(edge[1])
        invrs[edge[1]].add(edge[0])

    # find root nodes
    queue = [n for n in graph.keys() if n not in invrs.keys()]
    path = []

    while queue:
        queue = sorted(queue)
        node = queue.pop(0)
        path.append(node)
        for n in graph[node]:
            if invrs[n].issubset(path):
                queue.append(n)

    return "".join(path)


class Workers(object):
    """Implements worker queues"""

    def __init__(self):
        self.workers = [
            {"task": None, "eta": 0},
            {"task": None, "eta": 0},
            {"task": None, "eta": 0},
            {"task": None, "eta": 0},
            {"task": None, "eta": 0},
        ]

    def next_slot(self, ctime):
        first = min([w["eta"] for w in self.workers if w["task"]])
        return first if first > ctime else ctime

    def available(self, ctime):
        return len([w["eta"] for w in self.workers if w["eta"] <= ctime]) >= 1

    def is_task(self, task):
        return len([w for w in self.workers if w["task"] is task]) >= 1

    def assign(self, task, ctime):
        available = [w for w in self.workers if not w["task"] or w["eta"] <= ctime]
        assert available, "assign error: use available()"
        task_time = 61 + ord(task) - ord("A")
        available[0]["task"] = task
        available[0]["eta"] = ctime + task_time

    def finish(self, ctime):
        ready = []
        for w in [w for w in self.workers if w["eta"] <= ctime]:
            task = w["task"]
            if task:
                ready.append(task)
            w["task"] = None
        return sorted(ready)

    def dump(self):
        log = "["
        for w in self.workers:
            log += " {}:{}".format(w["task"] if w["task"] else "-", w["eta"])
        log += " ]"
        print(log)


def solve_part2(input):
    graph = defaultdict(set)
    invrs = defaultdict(set)
    tasks = set()
    workers = Workers()

    for edge in input:
        graph[edge[0]].add(edge[1])
        invrs[edge[1]].add(edge[0])
        tasks.add(edge[0])
        tasks.add(edge[1])

    # find root nodes
    queue = [n for n in graph.keys() if n not in invrs.keys()]
    path = []
    ctime = 0

    while tasks:
        queue = sorted(queue)
        # print('{:>4} -> {:<6} (tasks:{} path:{})'.format(
        #        ctime, ''.join(queue), ''.join(sorted(tasks)), ''.join(path)))
        while workers.available(ctime) and queue:
            workers.assign(queue.pop(0), ctime)

        ctime = workers.next_slot(ctime)
        ready = workers.finish(ctime)

        for n in ready:
            path.append(n)
            tasks.remove(n)
            for m in graph[n]:
                if invrs[m].issubset(path) and not workers.is_task(m):
                    queue.append(m)

    return ctime, "".join(path)


input = get_input()
print("Part1: assembly order {}".format(solve_part1(input)))
print("Part2: assembly time {} (order {})".format(*solve_part2(input)))
