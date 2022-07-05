import sys
import heapq
input = sys.stdin.readline

h = []
n = int(input())

for i in range(n):
    x = int(input())

    if x:
        heapq.heappush(h, x)
    else:
        print(heapq.heappop(h) if h else 0)
        
