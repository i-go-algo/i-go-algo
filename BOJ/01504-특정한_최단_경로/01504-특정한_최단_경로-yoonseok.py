# git commit -m "submit : BOJ 01504 특정한 최단 경로 (yoonseok)"
N, E = map(int,input().split())
INF = 987654321
gp = [[INF]*(N+1) for i in range(N+1)]
for i in range(N+1):
    gp[i][i] = 0
d = [[INF]*(N+1) for i in range(N+1)]
for i in range(E):
    i,j,c = map(int,input().split())
    gp[i][j]=c
    gp[j][i]=c
def dijkstra(start):
    global d
    global gp
    visited = [False]*(1+N)
    for i in range(1,N+1):
        d[start][i] = gp[start][i]
    visited[start]=True
    for i in range(1,N-1):
        current = 0
        min_d = INF
        for i in range(1,N+1):
            if d[start][i]<min_d and not visited[i]:
                min_d = d[start][i]
                current=i
        visited[current]=True
        for j in range(1,N+1):
            if not visited[j]:
                if d[start][current]+gp[current][j] < d[start][j]:
                    d[start][j]=d[start][current]+gp[current][j]
u,v = map(int,input().split())
dijkstra(1)
dijkstra(u)
dijkstra(N)      
answer = min(d[1][u]+d[u][v]+d[N][v],d[1][v]+d[u][v]+d[N][u])
if answer >= INF:
    print(-1)
else:
    print(min(d[1][u]+d[u][v]+d[N][v],d[1][v]+d[u][v]+d[N][u]))