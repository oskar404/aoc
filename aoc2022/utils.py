""" Utilities to get rid copy-pasta """


def read_data(input_file):
    """Read input file"""
    with open(input_file, mode="r", encoding="utf-8") as infile:
        return infile.read()
