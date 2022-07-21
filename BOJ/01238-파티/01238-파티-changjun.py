# git commit -m "submit : BOJ 01238 파티 (changjun)"

from collections import defaultdict
import heapq

n, m, x = map(int,input().split())

dic = defaultdict(dict)
for _ in range(m):
    s, e, t = map(int,input().split())
    dic[s][e] = t


distance = [[100*n for _ in range(n+1)] for _ in range(n+1)]




for i in range(1, n+1):
    tmp_distance = distance[i]

    tmp_distance[i] = 0
    q = []
    heapq.heappush(q, (0, i))
    while q:
        cost, node = heapq.heappop(q)
        for next_node in dic[node]:
            if (cost + dic[node][next_node]) < tmp_distance[next_node] :
                tmp_distance[next_node] = cost + dic[node][next_node]
                heapq.heappush(q, (tmp_distance[next_node], next_node))
# print(distance)
max_dist = 0
for i in range(1, n+1):
    tmp = distance[i][x] + distance[x][i]
    if tmp > max_dist:
        max_dist = tmp
print(max_dist)



        