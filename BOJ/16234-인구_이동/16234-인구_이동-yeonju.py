import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    temp = []   
    temp.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    visited[nx][ny] = 1
                    temp.append((nx, ny))
                    queue.append((nx, ny))

    return temp


n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0

    for i in range(n):
        for j in range(n):

            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                if len(country) > 1:
                    flag = 1
                    num = sum([arr[x][y] for x, y in country]) // len(country)

                    for x, y in country:
                        arr[x][y] = num
                    # print(arr)

    if flag == 0:
        break
    res += 1

print(res)

# git commit -m "submit : BOJ 16234 인구 이동 (yeonju)"