import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    global cnt
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
            
    cnt += 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())
for tc in range(t):
    m, n, k = map(int, input().split())

    cnt = 0
    arr = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
    print(cnt)
