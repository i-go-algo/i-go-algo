# git commit -m "submit : BOJ 01927 최소 힙 (eonyong)"
import heapq
import sys # sys.stdin.readline() TLE인데 이거 쓰니까 통과되네요 ㅂㄷㅂㄷ

que = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if not n:
        try:
            print(heapq.heappop(que))
        except:
            print(0)
    else:
        heapq.heappush(que, n)
