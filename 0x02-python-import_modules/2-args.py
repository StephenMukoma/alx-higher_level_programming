#!/usr/bin/python3
import sys

n = len(sys.argv)
n = n - 1

if n == 0:
    print("{} arguments.".format(n))
elif n == 1:
    print("{} argument:".format(n))
    print("{}: {}".format(n,sys.argv[1]))
else:
    print("{} arguments:".format(n))
    for i in range(n + 1):
        print("{}: {}".format(i,sys.argv[i]))
