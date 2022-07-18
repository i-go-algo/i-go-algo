from collections import deque


def bfs(start):
    visited = [-1 for _ in range(vertex + 1)]
    queue = deque()
    queue.append(start)
    visited[start] = 0
    max_dist = (0, 0)
    while queue:
        x = queue.popleft()

        for nx, dist in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x] + dist
                queue.append(nx)
                if max_dist[0] < visited[nx]:
                    max_dist = visited[nx], nx
    return max_dist


vertex = int(input())
graph = [[] for _ in range(vertex + 1)]

for _ in range(vertex):
    temp = list(map(int, input().split()))
    i = 1
    while True:
        if temp[i] == -1:
            break
        graph[temp[0]].append((temp[i], temp[i + 1]))
        i += 2

dist, node = bfs(1)
dist, node = bfs(node)
print(dist)
