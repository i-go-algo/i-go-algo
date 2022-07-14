import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0
queue = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))

bfs()

for row in arr:
    for i in row:
        if i == 0:
            print(-1)
            exit(0)
    res = max(res, max(row))

print(res - 1)
