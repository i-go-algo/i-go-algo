import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        cur_node = queue.popleft()

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1
    return


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0 for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(sum(visited) - 1)
