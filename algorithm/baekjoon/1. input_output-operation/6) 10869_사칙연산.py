import sys

A, B = map(int, sys.stdin.readline().split())
result = [A + B, A - B, A * B, A // B, A % B]

for value in result:
    sys.stdout.writelines(f"{value}\n")
