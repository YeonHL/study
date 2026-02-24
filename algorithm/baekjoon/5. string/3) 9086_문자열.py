import sys

T = int(sys.stdin.readline())

for _ in range(T):
    string = sys.stdin.readline().rstrip()
    sys.stdout.write(f"{string[0]}{string[-1]}\n")
