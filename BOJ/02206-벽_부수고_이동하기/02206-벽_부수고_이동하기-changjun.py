# git commit -m "submit : BOJ 02206 벽 부수고 이동하기 (changjun)"
from collections import deque

n, m = map(int, input().split())

lst = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 1))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = -1
while q:
    x, y, flag = q.popleft()
    if x == n - 1 and y == m - 1:
        ans = visited[x][y][flag] + 1
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if lst[nx][ny] == 0:
                if visited[nx][ny][flag] == 0 or visited[nx][ny][flag] > visited[x][y][flag] + 1:
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                    q.append((nx, ny, flag))
            else:
                if flag:
                    if visited[nx][ny][0] == 0 or visited[nx][ny][0] > visited[x][y][flag] + 1:
                        visited[nx][ny][0] = visited[x][y][flag] + 1
                        q.append((nx, ny, 0))

print(ans)
