# git commit -m "submit : BOJ 17837 새로운 게임 2 (yoonseok)"
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = []

for i in range(k) :
    r, c, d = map(int, input().split())
    horse.append([r-1, c-1, d-1])
    chess[r-1][c-1].append(i)

result_turn = 0

def solve(horse_num) :
    x, y, dir = horse[horse_num]
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2 :
        if dir in [0, 2] :
            dir += 1
        elif dir in [1, 3] :
            dir -= 1
        horse[horse_num][2] = dir
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2 :
            return True

    horse_add = []
    for idx, number in enumerate(chess[x][y]) :
        if number == horse_num :
            horse_add.extend(chess[x][y][idx:])
            chess[x][y] = chess[x][y][:idx]
            break

    if board[nx][ny] == 1 : # 빨간색
        horse_add = horse_add[-1::-1] # 말을 거꾸로

    for h in horse_add :
        horse[h][0], horse[h][1] = nx, ny # 말 이동
        chess[nx][ny].append(h) # 말 쌓아 올리기

    if len(chess[nx][ny]) >= 4 :
        return False
    return True

while True :
    flag = False
    if result_turn > 1000 :
        print(-1)
        break

    for l in range(k) :
        if solve(l) == False :
            flag = True
            break

    result_turn += 1
    if flag == True :
        print(result_turn)
        break