#!/usr/bin/python3

if __name__ == "__main__":
    """Print an infite addition that adds all arguments"""

import sys

count = len(sys.argv) - 1
total = 0

if count == 0:
    print("{}".format(total))
else:
    for i in sys.argv[1:]:
        i = int(i)
        total += i
    print("{}".format(total))
