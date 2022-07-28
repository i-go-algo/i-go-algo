# git commit -m "submit : BOJ 01865 웜홀 (yoonseok)"
import sys
input = sys.stdin.readline
TC = int(input())
INF = 987654321
def bf(start):
    dist = [INF]*(N+1)
    dist[start]=0
    for k in range(N):
        for i,j,cost in edges:
            if dist[j]>dist[i]+cost:
                dist[j]=dist[i]+cost
                if k == N-1:
                    return True
    return False
for tc in range(TC):
    N, M, W = map(int,input().split())
    edges = []
    for i in range(M):
        i,j,cost = map(int,input().split())
        edges.append((i,j,cost))
        edges.append((j,i,cost))
    for i in range(W):
        i,j,cost = map(int,input().split())
        edges.append((i,j,-cost))
    flag = False
    
    if bf(1):
            
        flag = True
        
    if flag:
        print("YES")
    else:
        print("NO")
                    
    
