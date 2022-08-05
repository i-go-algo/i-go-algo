# git commit -m "submit : BOJ 02206 벽 부수고 이동하기 (yoonseok)"
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
M, N = map(int,input().split())
maze = [list(map(int,input())) for i in range(M)]
vis = [[[False]*2 for i in range(N)] for j in range(M)]
q = deque()
q.append((0,0,0,0))
flag = False

while q:
    i,j,b,c = q.popleft()
    if i==M-1 and j==N-1:
        print(c+1)
        flag = True
        break
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        nb = b
        if ni < 0 or nj <0 or ni>=M or nj>=N or vis[ni][nj][b]:
            continue
        if maze[ni][nj]==1 and b==1:
            continue
        if maze[ni][nj]==1:
            nb = 1
        vis[ni][nj][nb]=True
        q.append((ni,nj,nb,c+1))
if not flag:
    print(-1)
