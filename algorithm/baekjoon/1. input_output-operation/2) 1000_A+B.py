# Baekjoon 전용: sys.stdin.readline(), sys.stdout.writelines() 사용

import sys

A, B = map(int, sys.stdin.readline().split())
sys.stdout.writelines(str(A + B))
