import pytest  # noqa: F401  # pylint: disable=unused-import
import utils
from day13 import parse_data, parse_packet, tokenize, compare, Node
from day13 import solve_part1, solve_part2


MESSAGES = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


def test_parse_data():
    packets = parse_data(MESSAGES)
    print(packets)
    assert len(packets) == 8
    assert packets[0]["left"] == "[1,1,3,1,1]"
    assert packets[0]["right"] == "[1,1,5,1,1]"


def test_tokenize():
    tokens = tokenize("[[1],24]")
    print(tokens)
    assert len(tokens) == 6
    assert tokens[0] == "["
    assert tokens[-1] == "]"
    assert tokens[2] == 1
    assert tokens[4] == 24


def test_parse_packet():
    packet = parse_packet("[[1],4]")
    assert isinstance(packet, Node)
    assert not packet.leaf
    print(str(packet))
    assert str(packet) == "[[1],4]"


def test_compare():
    def run(lhs, rhs, expected):
        print(f"{lhs=} <=> {rhs=} == {expected}")
        assert compare(parse_packet(lhs), parse_packet(rhs)) == expected

    run("[]", "[]", 0)
    run("[1]", "[1]", 0)
    run("[]", "[1]", -1)
    run("[1]", "[]", 1)
    run("[]", "[[]]", -1)
    run("[[]]", "[]", 1)
    run("[1]", "[[1]]", 0)
    run("[[1]]", "[1]", 0)
    run("[1]", "[2]", -1)
    run("[2]", "[1]", 1)
    # run stuff one by one from sample data
    run("[1,1,3,1,1]", "[1,1,5,1,1]", -1)
    run("[[1],[2,3,4]]", "[[1],4]", -1)
    run("[9]", "[[8,7,6]]", 1)
    run("[[4,4],4,4]", "[[4,4],4,4,4]", -1)
    run("[7,7,7,7]", "[7,7,7]", 1)
    run("[]", "[3]", -1)
    run("[[[]]]", "[[]]", 1)
    run("[1,[2,[3,[4,[5,6,7]]]],8,9]", "[1,[2,[3,[4,[5,6,0]]]],8,9]", 1)


def test_solution1():
    with utils.verbose():
        assert solve_part1(MESSAGES) == 13


def test_solution2():
    with utils.verbose():
        assert solve_part2(MESSAGES) is True
