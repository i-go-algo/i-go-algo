# git commit -m "submit : BOJ 01916 최소비용 구하기 (eonyong)"
import heapq


def dijkstra(start, city, distances):
    que = []
    heapq.heappush(que, (0, start))
    distances[start] = 0
    while que:
        dist, node = heapq.heappop(que)

        if distances[node] < dist:
            continue

        for c, w in city[node]:
            cost = distances[node] + w
            if cost < distances[c]:
                distances[c] = cost
                heapq.heappush(que, (cost, c))


n = int(input())
m = int(input())
city = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    city[s].append([e, t])
start, end = map(int, input().split())
distances = [float('inf') for _ in range(n + 1)]
distances[start] = 0
dijkstra(start, city, distances)
print(distances[end])
