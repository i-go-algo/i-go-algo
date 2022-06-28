import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        cur_node = queue.popleft()
        print(cur_node, end=' ')
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1


def dfs(cur_node):
    visited[cur_node] = 1
    print(cur_node, end=' ')
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            dfs(next_node)


n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited = [0 for _ in range(n + 1)]
dfs(v)

print()
visited = [0 for _ in range(n + 1)]
bfs(v)
