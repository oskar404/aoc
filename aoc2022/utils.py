""" Utilities for all solutions to get rid of copy-pasta """

import argparse
import datetime
import re
import time
from contextlib import contextmanager
from functools import wraps
from typing import Any, Callable


# Flag for solutions to use bit more verbosity
VERBOSE = False


@contextmanager
def verbose():
    """Context manager for verbose output.
    This is not a thread safe implementation
    """
    global VERBOSE  # pylint: disable=global-statement
    original = VERBOSE
    VERBOSE = True
    yield
    VERBOSE = original


# From: https://zyxue.github.io/2017/09/21/python-timeit-decorator.html

def timeit(func: Callable[..., Any]) -> Callable[..., Any]:
    """Times a function, usually used as decorator"""

    @wraps(func)
    def timed_func(*args: Any, **kwargs: Any) -> Any:
        """Returns the timed function"""
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = datetime.timedelta(seconds=(time.time() - start))
        print(f"time {func.__name__}: {elapsed}")
        return result

    return timed_func


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
    args = parser.parse_args()

    global VERBOSE  # pylint: disable=global-statement
    VERBOSE = args.verbose

    return read_data(args.file)
