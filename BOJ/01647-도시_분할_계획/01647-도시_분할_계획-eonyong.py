# git commit -m "submit : BOJ 01647 도시 분할 계획 (eonyong)"

import sys

input = sys.stdin.readline


def Union(s, e, parents):
    parents[max(s, e)] = min(s, e)
    return parents


def Find(v):
    if v == parents[v]:
        return v
    return Find(parents[v])


n, k = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(k)]
nodes.sort(key=lambda x: x[2])

parents = list(range(n + 1))

answer, max_val = 0, 0
for s, e, w in nodes:
    if Find(s) != Find(e):
        Union(Find(s), Find(e), parents)
        max_val = max(max_val, w)
        answer += w

print(answer - max_val)
