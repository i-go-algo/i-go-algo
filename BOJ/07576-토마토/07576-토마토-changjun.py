# git commit -m "submit : BOJ 07576 토마토 (changjun)"

from collections import deque


m, n = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

q = deque()
visited = set()

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            q.append((i,j,0))
            visited.add((i,j))
        elif lst[i][j] == -1:
            visited.add((i,j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y, day = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited:
            visited.add((nx,ny))
            if lst[nx][ny] == 0:
                q.append((nx, ny, day+1))

if len(visited) == m*n:
    print(day)
else:
    print(-1)



