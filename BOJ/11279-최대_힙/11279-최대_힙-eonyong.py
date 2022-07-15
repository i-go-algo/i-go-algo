# git commit -m "submit : BOJ 11279 최대 힙 (eonyong)"
import heapq
import sys

que = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if not n:
        try:
            print(-heapq.heappop(que))
        except:
            print(0)
    else:
        heapq.heappush(que, -n)
