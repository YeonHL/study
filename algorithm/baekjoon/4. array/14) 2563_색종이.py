# 얕은 복사: 리스트를 그대로 복사하면 주소값만 복사하므로 for문으로 별도의 리스트 객체를 생성해야 함
# 0과 1만 있을 경우, 반복문을 사용할 필요 없이 sum으로 처리 가능

import sys

drawing_paper = [[0] * 100 for _ in range(100)]
paper_count = int(sys.stdin.readline())

for _ in range(paper_count):
    x, y = map(int, sys.stdin.readline().split())

    for row in range(y, y + 10):
        drawing_paper[row][x : x + 10] = [1] * 10

area = sum(sum(row) for row in drawing_paper)

sys.stdout.write(str(area))
