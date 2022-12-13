import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
infos = []
graph = [[] for i in range(n + 1)]
in_degree = [0] * (n + 1)
queue = deque()

for _ in range(m):
    a, b = map(int, input().split())
    infos.append((a, b))
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, n + 1):
    if not in_degree[i]:
        queue.append(i)

while queue:
    cur = queue.popleft()
    for i in graph[cur]:
        in_degree[i] -= 1
        if not in_degree[i]:
            queue.append(i)
    print(cur, end=' ')
