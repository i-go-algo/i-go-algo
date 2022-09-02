# git commit -m "submit : BOJ 11404 플로이드 (yoonseok)"
n = int(input())
m = int(input())
INF = 987654321
cost = [[INF]*n for i in range(n)]
for i in range(n):
    cost[i][i] = 0
for i in range(m):
    i,j,c = map(int,input().split())
    cost[i-1][j-1] = min(cost[i-1][j-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            
            if (cost[i][j]>cost[i][k]+cost[k][j]):
                
                cost[i][j] = cost[i][k]+cost[k][j]
for i in range(n):
    for j in range(n):
        if cost[i][j] == INF:
            print(0, end = ' ')
        else:
            print(cost[i][j],end = ' ')
    print()