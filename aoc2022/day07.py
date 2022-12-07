#!/usr/bin/env python3

from pathlib import Path
import sys


# You can hear birds chirping and raindrops hitting leaves as the expedition
# proceeds. Occasionally, you can even hear much louder sounds in the distance;
# how big do the animals get out here, anyway?
#
# The device the Elves gave you has problems with more than just its
# communication system. You try to run a system update:
#
#   $ system-update --please --pretty-please-with-sugar-on-top
#   Error: No space left on device


ROOT = Path("/")
LIMIT = 100000
TOTAL_SPACE = 70000000
MIN_FREE_SPACE = 30000000


class Context:
    """Provides context/environment for shell commands"""

    def __init__(self):
        self.filesys = {}  # file system
        self.cwd = ROOT

    def inode(self):
        self.filesys[self.cwd] = {"dirs": [], "files": 0}

    def change_dir(self, dirname):
        if dirname == "/":
            self.cwd = ROOT
        if dirname == "..":
            assert self.cwd != ROOT
            self.cwd = self.cwd.parent
        else:
            self.cwd = self.cwd / dirname

    def update_dir(self, dirname):
        self.filesys[self.cwd]["dirs"].append(dirname)

    def update_file(self, filesize):
        self.filesys[self.cwd]["files"] += filesize


def parse(data):
    """Parses input stream and returns filesystem"""

    def is_cmd(line):
        return line[0] == "$"

    def parse_cmd(ctx, line):
        """Parse command"""
        tokens = line.split()
        if tokens[1] == "cd":
            # Handle cd command - updates cwd
            ctx.change_dir(tokens[2])
        elif tokens[1] == "ls":
            # Handle ls command - creates node entry to filesystem
            ctx.inode()
        else:
            assert False, "unknown command"

    def parse_ls_output(ctx, line):
        tokens = line.split()
        if tokens[0] == "dir":
            ctx.update_dir(tokens[1])
        else:
            filesize = int(tokens[0])
            ctx.update_file(filesize)

    ctx = Context()
    data = data.strip()
    for line in data.splitlines():
        if is_cmd(line):
            parse_cmd(ctx, line)
        else:
            # must be ls output
            parse_ls_output(ctx, line)

    return ctx.filesys


def solve_part1(data):
    """Find all of the directories with a total size of at most 100000.
    What is the sum of the total sizes of those directories?
    """

    def get_size(filesys, path, inode):
        result = inode["files"]
        if result <= LIMIT:
            # only iterate if small enough
            for dirname in inode["dirs"]:
                subdir = path / dirname
                result += get_size(filesys, subdir, filesys[subdir])
                if result > LIMIT:
                    break  # fail fast
        return result

    filesys = parse(data)
    result = 0
    for path, inode in filesys.items():
        if inode["files"] <= LIMIT:
            candidate = get_size(filesys, path, inode)
            if candidate <= LIMIT:
                result += candidate
    return result


def solve_part2(data):
    """Find the smallest directory that, if deleted, would free up enough space
    on the filesystem to run the update. What is the total size of that
    directory?
    """

    def recurse(path, filesys, sizemap):
        """recurse the whole file hierarchy and update sizemap"""
        pathsize = 0
        for dirname in filesys[path]["dirs"]:
            pathsize += recurse(path / dirname, filesys, sizemap)
        pathsize += filesys[path]["files"]
        sizemap[path] = pathsize
        return pathsize

    filesys = parse(data)
    sizemap = {}
    disk_usage = recurse(ROOT, filesys, sizemap)
    required = MIN_FREE_SPACE - (TOTAL_SPACE - disk_usage)
    result = TOTAL_SPACE  # make it big enough
    for _, pathsize in sizemap.items():
        if pathsize >= required:
            result = min(result, pathsize)
    return result


def read_data(file):
    with open(file, mode="r", encoding="utf-8") as infile:
        return infile.read()


def main():
    assert len(sys.argv) == 2, "Missing input"
    data = read_data(sys.argv[1])
    result = solve_part1(data)
    print(f"Part 1: {result}")
    result = solve_part2(data)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
