# 값의 교환에도 튜플 언패킹을 사용할 수 있습니다.
# 성능을 극대화하려면 함수 호출 오버헤드 제거를 위해 인라인 함수를 고민하세요.

import sys

N, M = map(int, sys.stdin.readline().split())
basket = [number for number in range(1, N + 1)]


for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket[i - 1], basket[j - 1] = basket[j - 1], basket[i - 1]

sys.stdout.write(f"{' '.join(map(str, basket))}")
