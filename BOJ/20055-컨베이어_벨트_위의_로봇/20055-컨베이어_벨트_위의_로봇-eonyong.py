# git commit -m "submit : BOJ 20055 컨베이어 벨트 위의 로봇 (eonyong)"
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
belts = deque(list(map(int, input().split())))
robots = deque([False for _ in range(n * 2)])
cnt = 0
while True:
    cnt += 1
    # 1단계
    belts.rotate(1)
    robots.rotate(1)
    robots[n] = False
    # 2단계
    for idx in range(n - 1, -1, -1):
        # 끝자리에 도착하면 내려온다.
        if idx == n - 1:
            robots[idx] = False
        # 현재 자리에 로봇이 있고 이동하려는 위치에 로봇이 없고, 내구도가 1이상이면
        # 내구도 1을 깎고 이동
        if belts[idx + 1] > 0 and not robots[idx + 1] and robots[idx]:
            robots[idx + 1], robots[idx] = robots[idx], robots[idx + 1]
            belts[idx + 1] -= 1
    # 3단계
    if belts[0] > 0:
        robots[0] = True
        belts[0] -= 1
    # 4단계
    if belts.count(0) >= k:
        print(cnt)
        break

