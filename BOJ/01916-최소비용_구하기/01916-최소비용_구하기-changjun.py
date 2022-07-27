# git commit -m "submit : BOJ 01916 최소비용 구하기 (changjun)"

from collections import defaultdict
import heapq

n = int(input())
m = int(input())

dic = defaultdict(set)
for _ in range(m):
    s, e, w = map(int,input().split())
    dic[s].add((e,w))

s, e = map(int,input().split())

big = 100000*m*n
lst = [big]*(n+1)
lst[s] = 0
q = []
heapq.heappush(q, (s,0))

while q:
    node, cost = heapq.heappop(q)
    if lst[node] < cost:
        continue
    for new_node, cost in dic[node]:
        if lst[new_node] > lst[node] + cost:
            lst[new_node] = lst[node] + cost
            heapq.heappush(q, (new_node, lst[new_node]))
print(lst[e])







