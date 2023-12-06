import pytest  # noqa: F401  # pylint: disable=unused-import
import day05
from day05 import Range, RangeMap


DATA = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def test_solution1():
    result = day05.solve_part1(DATA.strip())
    assert result == 35


def test_range():
    rng = Range(79, 14)
    assert rng.min() == 79
    assert rng.max() == 92


def test_range_map():
    # tested RangeMap
    rngmap = RangeMap(98, 50, 2)
    # test solution 1 interface
    assert 98 in rngmap
    assert 99 in rngmap
    assert 100 not in rngmap
    assert rngmap[98] == 50
    assert rngmap[99] == 51
    # solution 2: out of range
    test_rng = Range(97, 1)
    assert rngmap.map_range(test_rng) is None
    # solution 2: in range
    test_rng = Range(98, 2)
    before, mapped, after = rngmap.map_range(test_rng)
    assert before is None
    assert mapped.min() == 50
    assert mapped.max() == 51
    assert after is None
    # solution 2: before and inside range
    test_rng = Range(97, 2)
    before, mapped, after = rngmap.map_range(test_rng)
    assert before.min() == 97
    assert before.max() == 97
    assert mapped.min() == 50
    assert mapped.max() == 50
    assert after is None
    # solution 2: inside and after range
    test_rng = Range(99, 2)
    before, mapped, after = rngmap.map_range(test_rng)
    assert before is None
    assert mapped.min() == 51
    assert mapped.max() == 51
    assert after.min() == 100
    assert after.max() == 100
    # solution 2: over range
    test_rng = Range(97, 4)
    before, mapped, after = rngmap.map_range(test_rng)
    assert before.min() == 97
    assert before.max() == 97
    assert mapped.min() == 50
    assert mapped.max() == 51
    assert after.min() == 100
    assert after.max() == 100


def test_range_map2():
    # tested RangeMap
    rngmap = RangeMap(50, 52, 48)
    # test solution 1 interface
    assert 50 in rngmap
    assert 97 in rngmap
    assert 98 not in rngmap
    assert rngmap[50] == 52
    assert rngmap[97] == 99


def test_almanac_map():
    data = """
        seed-to-soil map:
        50 98 2
        52 50 48
        """
    amap = day05.AlmanacMap([i.strip() for i in data.strip().splitlines()])
    # test solution 1 interface
    assert amap.name == "seed-to-soil"
    assert len(amap.ranges) == 2
    assert amap[49] == 49
    assert amap[50] == 52
    assert amap[97] == 99
    assert amap[98] == 50
    assert amap[99] == 51
    assert amap[100] == 100
    # solution 2: range in first row
    test_rng = Range(98, 2)
    result = amap.map_range(test_rng)
    assert len(result) == 1
    assert result[0].min() == 50
    assert result[0].max() == 51
    # solution 2: range in two rows
    test_rng = Range(97, 2)
    result = amap.map_range(test_rng)
    assert len(result) == 2
    print(result)
    assert result[0].min() == 50
    assert result[0].max() == 50
    assert result[1].min() == 99
    assert result[1].max() == 99


def test_solution2():
    result = day05.solve_part2(DATA.strip())
    assert result == 46
