# git commit -m "submit : BOJ 01931 회의실 배정 (eonyong)"
# 이거 도저히! 너무! 생각이 안나서 블로그 참고 했습니다 ㅠㅠㅠ 우울하네요 흑

import sys

n = int(sys.stdin.readline())
timeTables = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
timeTables.sort(key=lambda x: (x[1], x[0]))
classTime, cnt = 0, 0
for start, end in timeTables:
    if start >= classTime:
        cnt += 1
        classTime = end
print(cnt)