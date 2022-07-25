import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dijkstra(cur_node):
    dist[cur_node] = 0
    queue = []
    heapq.heappush(queue, (cur_node, 0))

    while queue:
        cur_node, cost = heapq.heappop(queue)

        if dist[cur_node] < cost:
            continue
        for next_node, cost in graph[cur_node]:
            distance = dist[cur_node] + cost
            if distance < dist[next_node]:
                dist[next_node] = distance
                heapq.heappush(queue, (next_node, distance))


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
INF = int(1e9)
dist = [INF for _ in range(n + 1)]

dijkstra(start)
print(dist[end])
