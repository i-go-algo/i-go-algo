import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, shark_size):
    visited = [[0] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    temp = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if matrix[nx][ny] <= shark_size:    # 갈 수 있음
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1

                    if 0 < matrix[nx][ny] < shark_size:    # 먹을 수 있음
                        temp.append((nx, ny, dist[nx][ny]))

# 거리순, x 작은 순, y 작은 순
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            x = i
            y = j
            break

cnt = 0
res = 0

while True:
    fish_left = bfs(x, y, size)

    if len(fish_left) == 0:
        break

    nx, ny, dist = fish_left.pop()

    res += dist
    matrix[x][y], matrix[nx][ny] = 0, 0

    x, y = nx, ny
    cnt += 1

    if cnt == size:
        size += 1
        cnt = 0

print(res)
