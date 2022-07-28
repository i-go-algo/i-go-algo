# git commit -m "submit : BOJ 01967 트리의 지름 (eonyong)"
import heapq


def bfs(i, nodes, visited):
    que = []
    heapq.heappush(que, (i, 0))
    visited[i] = 0

    while que:
        start, w = heapq.heappop(que)
        for end, dist in nodes[start]:
            if visited[end] == -1:
                visited[end] = max(visited[end], dist + visited[start])
                heapq.heappush(que, (end, visited[end]))

    m = max(visited)
    return visited.index(m), m


n = int(input())
nodes = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    nodes[parent].append([child, weight])
    nodes[child].append([parent, weight])

visited = [-1] * (n + 1)
idx, val = bfs(1, nodes, visited[:])
print(bfs(idx, nodes, visited[:])[1])
