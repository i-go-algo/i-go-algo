import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [0 for _ in range(n + 1)]

    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        cur_node = queue.popleft()

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] += visited[cur_node] + 1
                queue.append(next_node)

    return sum(visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
cnt_list = [0 for _ in range(n + 1)]
res = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    res.append(bfs(i))

print(res.index(min(res)) + 1)
