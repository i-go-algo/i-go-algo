# git commit -m "submit : BOJ 02606 바이러스 (yoonseok)"
from os import link
from queue import Queue
N = int(input())
P = int(input())
links = [[False]*(N+1) for i in range(N+1)]
for i in range(P):
    i,j = map(int,input().split())
    links[i][j] = True
    links[j][i] = True
q = Queue()
visited = [False]*(N+1)
q.put(1)
visited[1]=True
ans = 0
while not q.empty():
    now =q.get()
    for i in range(N+1):
        if visited[i]:
            continue
        if not links[now][i]:
            continue
        ans+=1
        visited[i]=True
        q.put(i)
print(ans)