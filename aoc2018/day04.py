#!/usr/bin/env python3

import operator
import sys
from time import strftime, strptime


class LogEntry(object):
    """Container for log entries

    Log entries can be like:
        [1518-11-01 00:00] Guard #10 begins shift
        [1518-11-01 00:05] falls asleep
        [1518-11-01 00:25] wakes up
    """

    def __init__(self, line):
        timestamp, entry = line.strip().split("] ")
        self.ts = strptime(timestamp, "[%Y-%m-%d %H:%M")
        self.sleep = entry.startswith("fall")
        self.guard = -1
        if entry.startswith("Guard"):
            self.guard = int(entry.split()[1][1:])  # some magic

    def __repr__(self):
        ts = strftime("%m-%d %H:%M", self.ts)
        sleep = " sleep" if self.sleep else ""
        return "{}::guard:{}{}".format(ts, self.guard, sleep)

    def __str__(self):
        return self.__repr__()

    def get_min(self):
        if self.ts.tm_hour is 0:
            return self.ts.tm_min
        return 0 if self.ts.tm_hour is 23 else 59


def get_input():
    """Parse input file and sort log entries"""
    assert len(sys.argv) == 2, "Missing input"
    input = []
    with open(sys.argv[1]) as f:
        for line in f:
            input.append(LogEntry(line))
    input.sort(key=operator.attrgetter("ts"))
    guard = 0
    for entry in input:
        if entry.guard > 0:
            guard = entry.guard
        else:
            entry.guard = guard
    return input


def dump_histograms(histograms):
    for id, hist in histograms.items():
        h_str = ""
        for e in hist:
            h_str += "{0: >2}".format(e if e > 0 else "--")
        print("{:>6}: {}".format(id, h_str))


def add_histogram(hist, start, end=59):
    for i in range(start, end):
        hist[i] += 1


def calculate_histograms(input):
    """Calculate sleep histograms for guards who sleep"""
    sleep_times = {}

    entry = None
    for next in input:
        if entry and entry.sleep:
            guard = entry.guard
            hist = sleep_times.get(guard, [0] * 60)
            start = entry.get_min()
            end = next.get_min() if guard is next.guard else 60
            add_histogram(hist, start, end)
            sleep_times[guard] = hist
        entry = next

    # Handle last entry
    if entry and entry.sleep:
        guard = entry.guard
        hist = sleep_times.get(guard, [0] * 60)
        add_histogram(hist, entry.get_min())
        sleep_times[guard] = hist

    return sleep_times


def solve_part1(input):
    sleep_times = calculate_histograms(input)

    dump_histograms(sleep_times)

    bad_guard = 0
    bad_hist = None
    max_mins = 0
    for guard, hist in sleep_times.items():
        mins = sum(hist)
        if mins > max_mins:
            max_mins = mins
            bad_guard = guard
            bad_hist = hist

    bad_min = 0
    max_min = 0
    for i in range(0, 59):
        if bad_hist[i] > max_min:
            max_min = hist[i]
            bad_min = i

    return (bad_guard, max_mins, bad_min, bad_guard * bad_min)


def solve_part2(input):
    sleep_times = calculate_histograms(input)

    bad_guard = 0
    bad_min = 0
    max_min = 0
    bad_hist = None
    for guard, hist in sleep_times.items():
        local_max = max(hist)
        if local_max > max_min:
            max_min = local_max
            bad_guard = guard
            bad_hist = hist
            bad_min = hist.index(local_max)

    return (bad_guard, sum(bad_hist), bad_min, bad_guard * bad_min)


input = get_input()
guard, total_sleep, sleep_min, solution = solve_part1(input)
print(
    "Strategy1: guard: #{} total:{}min worst:{}min answer:{}".format(
        guard, total_sleep, sleep_min, solution
    )
)
guard, total_sleep, sleep_min, solution = solve_part2(input)
print(
    "Strategy2: guard: #{} total:{}min worst:{}min answer:{}".format(
        guard, total_sleep, sleep_min, solution
    )
)
