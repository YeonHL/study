import sys

A, B, C = map(int, sys.stdin.readline().split())
result = [(A + B) % C, ((A % C) + (B % C)) % C, (A * B) % C, ((A % C) * (B % C)) % C]

for value in result:
    sys.stdout.writelines(f"{value}\n")
