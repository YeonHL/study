# 내장 함수 divmod는 몫과 나머지를 반환합니다.

import sys

H, M = map(int, sys.stdin.readline().split())
total_minutes = (H * 60 + M - 45) % 1440
H, M = divmod(total_minutes, 60)

sys.stdout.writelines(f"{H} {M}")
