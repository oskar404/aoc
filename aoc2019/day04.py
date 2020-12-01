#!/usr/bin/env python3

import sys


def validator1(value):
    # Must be positive
    if value < 0:
        return False
    # Get digits, must be 6 digits
    digits = [int(d) for d in str(value)]
    if len(digits) != 6:
        return False
    # test increasing and double
    has_double = False
    previous = -1
    for d in digits:
        if previous > d:
            return False
        if previous == d:
            has_double = True
        previous = d
    return has_double


def validator2(value):
    # Must be positive
    if value < 0:
        return False
    # Get digits, must be 6 digits
    digits = [int(d) for d in str(value)]
    if len(digits) != 6:
        return False
    # test increasing and double groups
    doubles = {}
    previous = -1
    for d in digits:
        if previous > d:
            return False
        if previous == d:
            if d in doubles:
                doubles[d] = doubles[d] + 1
            else:
                doubles[d] = 2
        previous = d
    # Difficult to understand the spec:
    #   the two adjacent matching digits are not part of a larger group of
    #   matching digits
    # The min(doubles.values()) == 2 solved the problem but does not pass the
    # the test: 111111 should be valid
    return len(doubles) > 0 and min(doubles.values()) == 2


def search(start, end, validator):
    """Iterate over seach space and return candidates"""
    result = []
    for i in range(start, end):
        if validator(i):
            result.append(i)
    return result


def self_test():
    """Test validator functions"""
    # Test validator1()
    assert validator1(111111)
    assert validator1(122459)
    assert not validator1(223450)  # Decreasing
    assert not validator1(123789)  # No double
    assert not validator1(12237)  # Too short, not six digit
    assert not validator1(-11456)  # Negative integer
    # Test validator2()
    assert validator2(111111)
    assert validator2(122459)
    assert not validator2(223450)  # Decreasing
    assert not validator2(123789)  # No double
    assert not validator2(12237)  # Too short, not six digit
    assert not validator2(-11456)  # Negative integer
    assert validator2(112233)
    assert not validator2(123444)  # Part of large group
    assert validator2(111122)


if len(sys.argv) != 1:
    self_test()
else:
    candidates = search(206938, 679128, validator1)
    print(f"Num of password candidates [validator1()]: {len(candidates)}")
    candidates = search(206938, 679128, validator2)
    print(f"Num of password candidates [validator2()]: {len(candidates)}")
