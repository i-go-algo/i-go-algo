# git commit -m "submit : BOJ 01149 RGB거리 (yoonseok)"
N = int(input())
cost = [[0,0,0] for i in range(N)]

for i in range(N):
    r,g,b = map(int,input().split())
    if i==0:
        cost[i][0],cost[i][1],cost[i][2] = r,g,b
    else:
        nr = r+min(cost[i-1][1],cost[i-1][2])
        ng = g+min(cost[i-1][0],cost[i-1][2])
        nb = b+min(cost[i-1][0], cost[i-1][1])
        cost[i][0],cost[i][1],cost[i][2] = nr,ng,nb
print(min(cost[N-1]))