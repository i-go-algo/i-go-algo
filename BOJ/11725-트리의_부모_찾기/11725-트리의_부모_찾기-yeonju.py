import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        cur_node = queue.popleft()

        for next_node in graph[cur_node]:
            if not visited[next_node] and parent[next_node] == 0:
                parent[next_node] += cur_node
                visited[next_node] = 1
                queue.append(next_node)


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
parent = defaultdict(int)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
for i in range(2, n + 1):
    print(parent[i])
