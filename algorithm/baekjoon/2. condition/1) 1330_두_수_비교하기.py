import sys

A, B = map(int, sys.stdin.readline().split())
compare = ""

if A > B:
    compare = ">"
elif A < B:
    compare = "<"
elif A == B:
    compare = "=="

sys.stdout.writelines(compare)
