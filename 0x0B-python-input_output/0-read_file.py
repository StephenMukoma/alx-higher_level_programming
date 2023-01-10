#!/usr/bin/python3
"""Reads contents of a file"""


def read_file(filename=""):
    """prints contents of a file"""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
        f.close
