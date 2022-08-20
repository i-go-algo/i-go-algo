# git commit -m "submit : BOJ 11779 최소비용 구하기 2 (eonyong)"
import heapq


def dijkstra(start, city):
    que = []
    tracks = [[] for _ in range(n + 1)]
    tracks[start].append(start)
    distances = [float('inf') for _ in range(n + 1)]
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
                tracks[c] = []
                for p in tracks[node]:
                    tracks[c].append(p)
                tracks[c].append(c)

    return distances, tracks[end]


n = int(input())
m = int(input())
city = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    city[s].append([e, t])
start, end = map(int, input().split())

distances, tracks = dijkstra(start, city)
print(distances[end])
print(len(tracks))
print(*tracks)
