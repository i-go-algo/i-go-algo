# git commit -m "submit : BOJ 01197 최소 스패닝 트리 (eonyong)"
import sys

input = sys.stdin.readline


def Union(s, e, parents):
    s = Find(s)
    e = Find(e)
    if e < s:
        parents[s] = e
    else:
        parents[e] = s
    return parents


def Find(v):
    if v == parents[v]:
        return v
    parents[v] = Find(parents[v])
    return parents[v]


answer = 0
n, m = map(int, input().split())
nodes = []
for _ in range(m):
    s, e, w = map(int, input().split())
    nodes.append([s, e, w])

nodes.sort(key=lambda x: x[2])

parents = list(range(n + 1))

for s, e, w in nodes:
    if Find(s) != Find(e):
        parents = Union(s, e, parents)
        answer += w

print(answer)
