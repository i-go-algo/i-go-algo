# git commit -m "submit : BOJ 13549 숨바꼭질 3 (yoonseok)"
import heapq
vis = [False]*100001

N,k = map(int,input().split())
q = []
heapq.heappush(q,(0,N))
vis[N]=True
while q:
    time, nn = heapq.heappop(q)
    if nn==k:
        print(time)
        break
    while nn*2<=100000 and (not vis[nn*2]):
        heapq.heappush(q,(time,nn*2))
        vis[nn*2]=True
        nn*=2
    if nn-1>=0 and (not vis[nn-1]):
        heapq.heappush(q,(time+1,nn-1))
        vis[nn-1]=True
    if nn+1<=100000 and (not vis[nn+1]):
        heapq.heappush(q,(time+1,nn+1))
        vis[nn+1]=True
    