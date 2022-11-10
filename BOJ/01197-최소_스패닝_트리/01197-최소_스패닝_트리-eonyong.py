# git commit -m "submit : BOJ 01197 최소 스패닝 트리 (eonyong)"
import sys

input = sys.stdin.readline


def Union(s, e, parents):
    parents[max(s, e)] = min(s, e)
    return parents


def Find(v):
    if v == parents[v]:
        return v
    return Find(parents[v])


answer = 0
n, m = map(int, input().split())

nodes = [list(map(int, input().split())) for _ in range(m)]
nodes.sort(key=lambda x: x[2])

parents = list(range(n + 1))

for s, e, w in nodes:
    if Find(s) != Find(e):
        Union(Find(s), Find(e), parents)
        answer += w

print(answer)
