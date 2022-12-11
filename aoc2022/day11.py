#!/usr/bin/env python3

import math
import utils

# As you finally start making your way upriver, you realize your pack is much
# lighter than you remember. Just then, one of the items from your pack goes
# flying overhead. Monkeys are playing Keep Away with your missing things!
#
# To get your stuff back, you need to be able to predict where the monkeys will
# throw your items. After some careful observation, you realize the monkeys
# operate based on how worried you are about each item.


def parse_items(spec):
    """Return list of items for parsed line:
    Starting items: 79, 98
    """
    return [int(i.split(",")[0]) for i in spec.strip().split()[2:]]


def parse_operation(spec):
    """Return function object for the operation"""

    class SumOp:
        """Operation: new = old + 6"""

        def __init__(self, value):
            self.value = value

        def calculate(self, value):
            return value + self.value

        def __repr__(self):
            return f"new = old + {self.value}"

    class MultiplicationOp:
        """Operation: new = old * 19"""

        def __init__(self, value):
            self.value = value

        def calculate(self, value):
            return value * self.value

        def __repr__(self):
            return f"new = old * {self.value}"

    class PowerOp:
        """Operation: new = old * old"""

        def __init__(self):
            pass

        def calculate(self, value):
            return value * value

        def __repr__(self):
            return "new = old * old"

    tokens = spec.strip().split()
    if tokens[4] == "+":
        return SumOp(int(tokens[5]))
    if tokens[4] == "*":
        if tokens[5] == "old":
            return PowerOp()
        return MultiplicationOp(int(tokens[5]))
    assert False


def parse_num(spec):
    """Return divider for parsed line:
        Test: divisible by 23
    Or return monkey code for line:
        If true: throw to monkey 2
    """
    return int(spec.strip().split()[-1])


class Inspector:
    """Test what to do with the item"""

    def __init__(self, operation, tester, good_monkey, bad_monkey):
        self.operation = operation
        self.tester = tester
        self.good_monkey = good_monkey
        self.bad_monkey = bad_monkey

    def inspect(self, item):
        """Return tuple of new item value and monkey code"""
        level = self.operation.calculate(item)
        new_level = math.floor(level / 3)
        if new_level % self.tester == 0:
            return level, new_level, self.good_monkey
        return level, new_level, self.bad_monkey

    def __repr__(self):
        return (
            f"inspector:{self.tester} -> "
            f"{self.good_monkey}/{self.bad_monkey} ({self.operation})"
        )


class Monkey:
    """Monkey inspecting item worry levels and throwing them"""

    def __init__(self, items, inspector):
        self.items = items
        self.inspector = inspector
        self.counter = 0

    def inspects(self):
        """Generator for inspecting one item at time"""
        while self.items:
            item = self.items.pop(0)
            self.counter += 1
            yield self.inspector.inspect(item)

    def add(self, item):
        self.items.append(item)

    def __repr__(self):
        return f"items:{self.items} => {self.inspector})"


def parse(data):
    """Parse input data and return list of Monkey objects"""

    def pop_monkey(lines):
        """Pop 7 lines from data begining and return them as Monkey Object"""
        _ = lines.pop(0)  # title is not needed. Monkey code is list index
        items = parse_items(lines.pop(0))
        operation = parse_operation(lines.pop(0))
        tester = parse_num(lines.pop(0))
        good_monkey = parse_num(lines.pop(0))
        bad_monkey = parse_num(lines.pop(0))
        if lines:
            assert not lines.pop(0).strip()  # just test sensibility
        inspector = Inspector(operation, tester, good_monkey, bad_monkey)
        return Monkey(items, inspector)

    monkeys = []
    lines = data.strip().splitlines()
    while lines:
        monkeys.append(pop_monkey(lines))
    return monkeys


def dump(monkeys):
    """For debugging print monkeys"""
    for idx, monkey in enumerate(monkeys):
        print(f"Monkey:{idx} {monkey}")


def solve_part1(data):
    """Figure out which monkeys to chase by counting how many items they inspect
    over 20 rounds. What is the level of monkey business after 20 rounds of
    stuff-slinging simian shenanigans?
    """
    monkeys = parse(data)
    for _ in range(20):
        # print(f"ROUND {i} ===================================")
        # dump(monkeys)
        for monkey in monkeys:
            for _, level, next_monkey in monkey.inspects():
                monkeys[next_monkey].add(level)
    # print("ROUND 20 ===================================")
    # dump(monkeys)
    hoarders = [x.counter for x in monkeys]
    hoarders = sorted(hoarders)
    return hoarders[-1] * hoarders[-2]


def solve_part2(data):
    """Happy coding"""
    return len(data)


def main():
    data = utils.read_input(__file__)
    result = solve_part1(data)
    print(f"Part 1: {result}")
    # result = solve_part2(data)
    # print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
