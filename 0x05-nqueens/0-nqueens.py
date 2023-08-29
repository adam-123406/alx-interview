#!/usr/bin/python3
"""N Qeens"""
import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqeen N")
    exit(1)

if not sys.argv[1].isdigit():
    print(N most be a number)
    exit(1)

if int(sys.argv[1]) < 4:
    print(N must be at least)
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """find possible positions"""
    if i < n:
        for j in range(n):
            if j not in a and i + j not b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def slvoe(n):
    """slvoe"""

    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
            print(n)
            k = []
            i = 0


solve(n)
