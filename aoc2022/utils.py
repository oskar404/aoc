""" Utilities for all solutions to get rid of copy-pasta """

import argparse
import contextlib
import functools
import re
import time


# Flag for solutions to use bit more verbosity
VERBOSE = False

# Flag for solutions to print timeit decorator results
TIMING_DATA = False


@contextlib.contextmanager
def verbose():
    """Context manager for verbose output.
    This is not a thread safe implementation
    """
    global VERBOSE  # pylint: disable=global-statement
    original_verbosity = VERBOSE
    global TIMING_DATA  # pylint: disable=global-statement
    original_timing = TIMING_DATA
    VERBOSE = True
    TIMING_DATA = True
    yield
    VERBOSE = original_verbosity
    TIMING_DATA = original_timing


# timeit() decorator originally from:
# https://zyxue.github.io/2017/09/21/python-timeit-decorator.html


def timeit(func):
    """Decorator to time the function execution"""

    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        """Returned wrap function printing"""
        start_tic = time.perf_counter()
        result = func(*args, **kwargs)
        end_tic = time.perf_counter()
        elapsed = end_tic - start_tic
        if TIMING_DATA:
            print(f"{func.__name__}(): {elapsed:0.5f}s")
        return result

    return timer_wrapper


def read_data(input_file):
    """Read input file"""
    with open(input_file, mode="r", encoding="utf-8") as infile:
        return infile.read()


def get_day(user):
    """Extract day number from file string e.g. "day10.py" """
    pattern = re.compile(".*day(\\d\\d)\\.py")
    result = pattern.match(user)
    return result.group(1)


def read_input(user):
    """Parse command line arguments and read data from file.
    Returns the data
    """
    day = get_day(user)

    parser = argparse.ArgumentParser(
        description="Advent of Code solution",
        epilog="More info on https://adventofcode.com/2022",
    )
    parser.add_argument(
        "file",
        default=f"input{day}.txt",
        help=f'Path to input file. If not given tries to read "input{day}.txt"',
        metavar="FILE",
        nargs="?",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        help="Increase verbosity of the solution (if available)",
        action="store_true",
    )
    parser.add_argument(
        "-t",
        "--timer",
        default=False,
        help="Print timing data",
        action="store_true",
    )
    args = parser.parse_args()

    global VERBOSE  # pylint: disable=global-statement
    VERBOSE = args.verbose
    global TIMING_DATA  # pylint: disable=global-statement
    TIMING_DATA = args.timer

    return read_data(args.file)
