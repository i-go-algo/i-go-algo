from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0:
                if arr[nx][ny] == 0:
                    queue.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[x][y][wall] + 1

                if arr[nx][ny] == 1 and wall == 0:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][wall] + 1
    return -1


n, m = map(int,input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

print(bfs())
