import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, x, y, cmd = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
cmd_order = list(map(int, input().split()))
dice = [0 for _ in range(6)]

for i in range(cmd):
    direction = cmd_order[i] - 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    if direction == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        # 2 - 서
    elif direction == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        # 3 - 북
    elif direction == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        # 4 - 남
    elif direction == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])
