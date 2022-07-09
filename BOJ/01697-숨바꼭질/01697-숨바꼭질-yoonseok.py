# git commit -m "submit : BOJ 01697 숨바꼭질 (yoonseok)"
from queue import Queue
vis = [False]*100001

N,k = map(int,input().split())
q = Queue()
q.put((N,0))
vis[N]=True
while not q.empty():
    nn, time = q.get()
    if nn==k:
        print(time)
        break
    if nn-1>=0 and (not vis[nn-1]):
        q.put((nn-1,time+1))
        vis[nn-1]=True
    if nn+1<=100000 and (not vis[nn+1]):
        q.put((nn+1,time+1))
        vis[nn+1]=True
    if nn*2<=100000 and (not vis[nn*2]):
        q.put((nn*2,time+1))
        vis[nn*2]=True