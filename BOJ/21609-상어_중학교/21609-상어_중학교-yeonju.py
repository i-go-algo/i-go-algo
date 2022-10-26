from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited, num):
    q = deque()
    q.append((x, y))
    c = board[x][y]
    visited[x][y] = num
    size, r_n = 1, 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == c and visited[nx][ny] == 0:
                    size += 1
                    visited[nx][ny] = num
                    q.append((nx, ny))
                elif board[nx][ny] == 0 and not num in visited[nx][ny]:
                    size += 1
                    r_n += 1
                    visited[nx][ny].append(num)
                    q.append((nx, ny))
    return size, r_n


def fall(x, y):
    stop = False
    for i in range(x + 1, n):
        nx = i
        if board[nx][y] != -2:
            stop = True
            break
    if stop:
        board[nx - 1][y] = board[x][y]
    else:
        board[nx][y] = board[x][y]
    board[x][y] = -2


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score = 0

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                visited[i][j] = []

    num, block = 1, []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and visited[i][j] == 0:
                size, r_n = bfs(i, j, visited, num)
                if size > 1:
                    block.append([size, r_n, i, j, num])
                num += 1
    if len(block) == 0:
        break

    block.sort(key=lambda x:(-x[0], -x[1], -x[2], -x[3]))
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and visited[i][j] == block[0][4]:
                cnt += 1
                board[i][j] = -2
            elif board[i][j] == 0 and block[0][4] in visited[i][j]:
                cnt += 1
                board[i][j] = -2

    score += cnt * cnt
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if board[i][j] >= 0 and board[i+1][j] == -2:
                fall(i, j)

    board = list(map(list, zip(*board)))[::-1]

    for i in range(n - 2, -1, -1):
        for j in range(n):
            if board[i][j] >= 0 and board[i + 1][j] == -2:
                fall(i, j)

print(score)
