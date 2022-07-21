# git commit -m "submit : BOJ 01753 최단경로 (changjun)"

from collections import defaultdict
import heapq

V, E = map(int,input().split())
k = int(input())

dic = defaultdict(dict)
for _ in range(E):
    u, v, w = map(int,input().split())
    
    if dic[u].get(v):
        dic[u][v] = min(dic[u][v], w)
    else:
        dic[u][v] = w



big_num = 300000 * 10
distance = [big_num] * (V+1)
distance[k] = 0
q = []
heapq.heappush(q, (0, k))
while q:
    cost, node = heapq.heappop(q)
    for next_node in dic[node]:
        next_distance = dic[node][next_node]
        if (cost + next_distance) < distance[next_node] :
            distance[next_node] = cost + next_distance
            heapq.heappush(q, (distance[next_node], next_node))

for i in range(1, V+1):
    if distance[i] == big_num:
        print('INF')
    else:
        print(distance[i])
