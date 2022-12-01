#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    n = len(sys.argv)
    if n == 1:
        print("0")
    else:
        for i in range (1, n):
            total += int(sys.argv[i])
    print("{}".format(total))
