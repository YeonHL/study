# 값을 비교할 때, 조건문이 많을 경우 Dictionary와 Tuple을 활용할 수 있습니다.

import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

quadrants = {(True, True): 1, (False, True): 2, (False, False): 3, (True, False): 4}
quadrant = quadrants[(x > 0, y > 0)]

sys.stdout.writelines(str(quadrant))
