#!/usr/bin/python3
"""writes to a file"""


def write_file(filename="", text=""):
    """Writing to a file"""

    with open(filename, "w+", encoding="utf-8") as f:
        return f.write(text)
