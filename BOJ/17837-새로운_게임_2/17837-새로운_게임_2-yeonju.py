dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def move_white(x, y, nx, ny):
    cur = chess[x][y].index(horse)
    top = len(chess[x][y])
    for i in range(cur, top):
        horses[chess[x][y][i]][0] = nx
        horses[chess[x][y][i]][1] = ny
        chess[nx][ny].append(chess[x][y][i])
    for _ in range(top - cur):
        chess[x][y].pop()


def move_red(x, y, nx, ny):
    cur = chess[x][y].index(horse)
    top = len(chess[x][y])
    for i in range(top - 1, cur - 1, -1):
        horses[chess[x][y][i]][0] = nx
        horses[chess[x][y][i]][1] = ny
        chess[nx][ny].append(chess[x][y][i])
    for _ in range(top - cur):
        chess[x][y].pop()


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
horses = dict()

for i in range(k):
    row, col, dir = map(int, input().split())
    chess[row - 1][col - 1].append(i)
    horses[i] = [row - 1, col - 1, dir]

for turn in range(1, 1001):
    for horse in range(k):
        x, y, d = horses[horse]
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 2:
            if arr[nx][ny] == 0:
                move_white(x, y, nx, ny)
            else:
                move_red(x, y, nx, ny)

        else:
            if d == 1 or d == 2:
                d = ((d - 1) ^ 1) + 1
            else:
                d = ((d - 3) ^ 1) + 3
            horses[horse][2] = d
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 2:
                if arr[nx][ny] == 0:
                    move_white(x, y, nx, ny)
                else:
                    move_red(x, y, nx, ny)

        if 0 <= nx < n and 0 <= ny < n and len(chess[nx][ny]) >= 4:
                print(turn)
                exit()

print(-1)
