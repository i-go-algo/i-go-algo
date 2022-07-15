# git commit -m "submit : BOJ 07576 토마토 (yoonseok)"
from collections import deque
import sys

N, M = map(int,input().split())
box = [list(map(int,input().split())) for i in range(M)]
q = deque()
dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = 0
for i in range(M):
    for j in range(N):
        if box[i][j]==1:
            q.append((i,j,0))
while q:
    i,j,c = q.popleft()
    ans = c
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        if ni <0 or nj < 0 or ni>=M or nj >= N:
            continue
        if box[ni][nj]!=0:
            continue
        box[ni][nj]=1
        q.append((ni,nj,c+1))

full = True
for i in range(M):
    for j in range(N):
        if box[i][j]==0:
            full = False
            break
    if not full:
        break
if full:
    print(ans)
else:
    print(-1)

