import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewelrys = []
for _ in range(n):
    heapq.heappush(jewelrys, list(map(int, input().split())))

bags = sorted([int(input()) for _ in range(k)])

temp = []
res = 0
for bag in bags:
    while jewelrys and bag >= jewelrys[0][0]:
        heapq.heappush(temp, - jewelrys[0][1])
        heapq.heappop(jewelrys)

    if temp:
        res += heapq.heappop(temp)
    elif not jewelrys:
        break

print(-res)
