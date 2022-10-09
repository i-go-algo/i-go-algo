# git commit -m "submit : BOJ 23288 주사위 굴리기 2 (yoonseok)"
from collections import deque
 
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
 
dy = (-1, 0, 1, 0)
dx = ( 0,-1, 0, 1)
UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
dir = RIGHT
dice = [
    [ -1,  2, -1],
    [  4,  1,  3],
    [ -1,  5, -1],
    [ -1,  6, -1]
]
def move_dice(dir):
    global dice
 
    if dir == RIGHT:
        tmp = dice[1][2]
        dice[1] = [dice[3][1], dice[1][0], dice[1][1]]
        dice[3][1] = tmp
    elif dir == LEFT:
        tmp = dice[1][0]
        dice[1] = [dice[1][1], dice[1][2], dice[3][1]]
        dice[3][1] = tmp
    elif dir == UP:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
    elif dir == DOWN:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp
 
def get_score_by_bfs(sy, sx, B):
    used = [[False] * M for _ in range(N)]
    cnt = 0
    q = deque()
    q.append((sy, sx))
    used[sy][sx] = True
    while q:
        y, x = q.pop()
        cnt += 1
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
 
            if ny < 0 or nx < 0 or ny >= N or nx >= M or used[ny][nx]:
                continue
            if board[ny][nx] == B:
                used[ny][nx] = True
                q.append((ny, nx))
    return cnt * B
 
loc = (0, 0)
result = 0
for i in range(K):
    ny = loc[0] + dy[dir]
    nx = loc[1] + dx[dir]
 
    if ny < 0 or nx < 0 or ny >= N or nx >= M: 
        dir = (dir + 2) % 4 
        ny = loc[0] + dy[dir]
        nx = loc[1] + dx[dir]
 
    loc = (ny, nx)
    move_dice(dir)
    B = board[ny][nx] 
    score = get_score_by_bfs(ny, nx, B)
    result += score

    A = dice[3][1]
    if A > B: dir = (dir - 1) % 4
    elif A < B:dir = (dir + 1) % 4
 
print(result)