# git commit -m "submit : BOJ 01389 케빈 베이컨의 6단계 법칙 (yoonseok)"
from queue import Queue
def bfs(graph,start):
    global kevin
    visited = [False]*(N+1)
    q = Queue()
    q.put((start,0))
    visited[start]=True
    while(not q.empty()):
        now,cost = q.get()
        for i in range(1,N+1):
            if visited[i]:
                continue
            if not graph[i][now]:
                continue
            visited[i]=True
            kevin[start]+=cost
            q.put((i,cost+1))

N, M = map(int,input().split())
graph = [[False]*(N+1) for i in range(N+1)]
kevin = [0]*(N+1)
kevin[0]=987654321
for i in range(M):
    i, j = map(int,input().split())
    graph[i][j] = True
    graph[j][i] = True
for i in range(1,N+1):
    bfs(graph,i)
print(kevin.index(min(kevin)))
