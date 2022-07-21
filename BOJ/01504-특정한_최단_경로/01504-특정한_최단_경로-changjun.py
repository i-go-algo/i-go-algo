# git commit -m "submit : BOJ 01504 특정한 최단 경로 (changjun)"

from collections import defaultdict
import heapq

n, e = map(int,input().split())

dic = defaultdict(set)
for _ in range(e):
    a, b, c = map(int,input().split())
    dic[a].add((b, c))
    dic[b].add((a, c))

v1, v2 = map(int,input().split())

big_num = e * 1000
# dist_1 = [big_num * (e+1)]
# dist_v1 = [big_num * (e+1)]
# dist_v2 = [big_num * (e+1)]

distance = [[big_num]* (n+1) for _ in range(3)]
tmp_lst =[1, v1, v2] 
for i in range(3):
    tmp_distance = distance[i]
    tmp_distance[tmp_lst[i]] = 0

    q = []
    heapq.heappush(q, (0, tmp_lst[i]))
    while q:
        cost, node = heapq.heappop(q)
        for next_node, next_distance in dic[node]:
            if (cost + next_distance) < tmp_distance[next_node] :
                tmp_distance[next_node] = cost + next_distance
                heapq.heappush(q, (tmp_distance[next_node], next_node))

ans = big_num * big_num
if big_num not in (distance[0][v1], distance[1][v2], distance[2][n]):
    ans = min(ans, distance[0][v1] + distance[1][v2] + distance[2][n])

if big_num not in ( distance[0][v2], distance[2][v1], distance[1][n]):
    ans = min(ans, distance[0][v2] + distance[2][v1] + distance[1][n])
if ans == big_num * big_num:
    ans = -1
print(ans)




        