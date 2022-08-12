import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    arr[nx][ny] += 1


def check_cheese():
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                return 1
    return 0


def remove_cheese():
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
            elif arr[i][j] > 0:
                arr[i][j] = 1
    return


res = 0

while True:
    if not check_cheese():  # 종료 조건: 치즈가 다 사라지면 끝
        print(res)
        break

    visited = [[0 for _ in range(m)] for _ in range(n)]
    bfs((0, 0))   
    remove_cheese()

    res += 1
