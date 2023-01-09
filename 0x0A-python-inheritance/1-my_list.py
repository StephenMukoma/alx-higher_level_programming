#!/usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """Initialites class"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
