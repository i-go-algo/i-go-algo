# git commit -m "submit : BOJ 02252 줄 세우기 (eonyong)"

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

answer = []
ls = deque()
degrees = [[] for _ in range(n + 1)]
cnts = [0 for _ in range(n + 1)]

refs = [list(map(int, input().split())) for _ in range(m)]

for a, b in refs:
    cnts[b] += 1
    degrees[a].append(b)

for idx in range(1, n + 1):
    if not cnts[idx]:
        ls.append(idx)


while ls:
    start = ls.popleft()
    answer.append(start)
    for e in degrees[start]:
        cnts[e] -= 1
        if not cnts[e]:
            ls.append(e)

print(*answer)