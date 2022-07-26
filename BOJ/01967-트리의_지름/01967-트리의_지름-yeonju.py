import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [-1 for _ in range(n + 1)]
    queue = deque()
    queue.append(start)
    visited[start] = 0
    max_value = (0, 0)

    while queue:
        cur_node = queue.popleft()

        for next_node, cost in graph[cur_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[cur_node] + cost
                queue.append(next_node)

    max_value = (max(visited), visited.index(max(visited)))
    return max_value


n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

max_dist, node = bfs(1)
max_dist, node = bfs(node)
print(max_dist)
