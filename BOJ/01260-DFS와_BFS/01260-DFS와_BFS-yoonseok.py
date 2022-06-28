# git commit -m "submit : BOJ 01260 DFS와 BFS (yoonseok)"
from queue import Queue
N, M, V = map(int,input().split())
graph = [[False]*(N+1) for i in range(N+1)]
def bfs(graph,start):
    visited = [False]*(N+1)
    q = Queue()
    q.put(start)
    visited[start]=True
    print(start,end = ' ')
    while(not q.empty()):
        now = q.get()
        for i in range(1,N+1):
            if visited[i]:
                continue
            if not graph[i][now]:
                continue
            visited[i]=True
            q.put(i)
            print(i, end=' ')
    print()

def dfs(graph,start):
    global visited
    visited[start]=True
    print(start,end= ' ')
    for i in range(1,N+1):
        if visited[i]:
            continue
        if not graph[start][i]:
            continue
        visited[start]=True
        dfs(graph,i)
for i in range(M):
    i,j = map(int,input().split())
    graph[i][j]=True
    graph[j][i]=True
global visited
visited = [False]*(N+1)
dfs(graph,V)
print()
bfs(graph,V)

