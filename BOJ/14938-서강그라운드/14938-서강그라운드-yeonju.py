import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dijkstra(start):
    global res
    dist = [1e9 for _ in range(n + 1)]
    dist[start] = 0
    cnt = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if dist[cur_node] < cur_dist:
            continue
        for distance, next_node in graph[cur_node]:
            cost = cur_dist + distance
            if cost < dist[next_node]:
                distance += cur_dist
                dist[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
   
    for node, distance in enumerate(dist):
        if distance <= m:
            cnt += items[node]
    
    if cnt > res:
        res = cnt


n, m, r = map(int, input().split())

items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
res = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

for i in range(1, n + 1):
    dijkstra(i)

print(res)
