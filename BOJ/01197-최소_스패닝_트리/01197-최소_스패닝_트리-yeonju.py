import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
visited = [0 for _ in range(v + 1)]
heap = [(0, 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

ans = 0
cnt = 0

while heap:
    if cnt == v:
        break
    weight, cur_node = heapq.heappop(heap)

    if not visited[cur_node]:
        visited[cur_node] = 1
        ans += weight
        cnt += 1

        for adj in graph[cur_node]:
            heapq.heappush(heap, adj)

print(ans)
